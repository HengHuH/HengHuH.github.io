# -*- coding: utf-8 -*-

"""HengHuH.github.io 的构建脚本。"""

import os
from datetime import date
import yaml
from bs4 import BeautifulSoup as bs
from urllib import parse


root = os.path.dirname(os.path.abspath(__file__))
root_url = "https://henghuh.github.io"


class Page:
    def __init__(self) -> None:
        self.name = ""
        self.addr = ""
        self.url = ""
        self.title = ""
        self.content = ""
        self.published = True

    @staticmethod
    def extract_meta_content(path):
        meta = {}
        content = ""
        with open(path, "r", encoding="utf-8") as f:
            fc = f.read()
            fc = fc.strip()
            if fc.startswith("---"):
                fc = fc[3:]
                idx = fc.find("---")
                meta = yaml.safe_load(fc[:idx])
                content = str.strip(fc[idx + 3 :])
            else:
                raise ValueError(f"{path} is not a valid page file, missing meta data")

        return meta, content

    def load(self, path):
        assert os.path.exists(path), f"{path} not exists"
        basename = os.path.basename(path)
        self.name, _ = os.path.splitext(basename)
        self.addr = self.name + ".html"
        self.url = parse.urljoin(root_url, self.addr)
        meta, self.content = self.extract_meta_content(path)
        self.title = meta.get("title", self.name)
        self.published = meta.get('published', True)


class Post(Page):
    def __init__(self) -> None:
        super(Post, self).__init__()
        self.date = None

    def load(self, path):
        assert os.path.exists(path), f"{path} not exists"
        basename = os.path.basename(path)
        fname, _ = os.path.splitext(basename)
        fns = fname.split("-")
        assert len(fns) >= 4, f"{path} is not a valid post file"
        self.name = "-".join(fns[3:])
        self.addr = os.path.join(fns[0], fns[1], self.name + ".html")
        self.url = parse.urljoin(root_url, self.addr)
        meta, self.content = self.extract_meta_content(path)
        self.date = meta.get('date', "-".join(fns[0:3]))
        self.title = meta.get("title", self.name)
        self.published = meta.get('published', True)


class Site:
    def __init__(self, root) -> None:
        self.root = root
        self._posts = set()
        self._pages = set()

    def add_post(self, post):
        self._posts.add(post)

    @property
    def posts(self):
        return self._posts

    def add_page(self, page):
        self._pages.add(page)

    @property
    def pages(self):
        return self._pages


class Builder:
    def __init__(self, site) -> None:
        self._site = site

        with open(os.path.join(root, "page_template.html"), "r", encoding="utf-8") as f:
            self.page_temp = f.read()

    def fillin_content(self, content):
        content = content.replace("{{date}}", str(date.today()))

        alllinks = []
        for post in sorted(self._site.posts, key=lambda x: (x.date), reverse=True):
            alllinks.append(f'<a href="{post.addr}">{post.title}</a>')

        content = content.replace("{{site.pages}}", "<br>\n".join(alllinks))
        return content

    def build(self):
        os.makedirs(self._site.root, exist_ok=True)

        for post in self._site.posts:
            abspath = os.path.join(self._site.root, post.addr)
            dirname = os.path.dirname(abspath)
            os.makedirs(dirname, exist_ok=True)

            with open(abspath, "w", encoding="utf-8") as f:
                posthtml = self.page_temp.replace("{{page.title}}", post.title)
                content = self.fillin_content(post.content)
                content += f'<hr/><font size="-1">发布于 {post.date}</font><br>\nHeng - <a href="https://henghuh.github.io">https://henghuh.github.io</a>'

                posthtml = posthtml.replace("{{page.content}}", content)
                f.write(bs(posthtml, "html.parser").prettify())
                print(f"build post: {post.addr} --- DONE")

        for page in self._site.pages:
            abspath = os.path.join(self._site.root, page.addr)
            with open(abspath, "w", encoding="utf-8") as f:
                pagecontent = self.fillin_content(page.content)
                pagehtml = self.page_temp.replace("{{page.title}}", page.title)
                pagehtml = pagehtml.replace("{{page.content}}", pagecontent)
                f.write(bs(pagehtml, "html.parser").prettify())
                print(f"build page: {page.addr} --- DONE")


if __name__ == "__main__":
    site = Site(os.path.join(root, "build"))

    for fname in os.listdir(os.path.join(root, "_posts")):
        fpath = os.path.join(root, "_posts", fname)
        post = Post()
        post.load(fpath)
        if post.published:
            site.add_post(post)

    for fname in os.listdir(root):
        if not fname.endswith(".page"):
            continue
        fpath = os.path.join(root, fname)
        page = Page()
        page.load(fpath)
        if page.published:
            site.add_page(page)

    builder = Builder(site)
    builder.build()
