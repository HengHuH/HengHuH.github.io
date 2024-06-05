# -*- coding: utf-8 -*-

"""HengHuH.github.io 的构建脚本。

依赖：python3, yaml
"""

import os
from datetime import date
import yaml
import shutil
from bs4 import BeautifulSoup as bs
from urllib import parse


root = os.path.dirname(os.path.abspath(__file__))
outdir = os.path.join(root, "build")
root_url = "https://henghuh.github.io"


class Page:
    def __init__(self) -> None:
        self.name = ""
        self.addr = ""
        self.url = ""
        self.title = ""
        self.content = ""

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
        self.title = meta["title"]


class Post(Page):
    def __init__(self) -> None:
        self.year = "2024"
        self.month = "01"
        self.day = "01"

    def load(self, path):
        assert os.path.exists(path), f"{path} not exists"
        basename = os.path.basename(path)
        fname, _ = os.path.splitext(basename)
        fns = fname.split("-")
        assert len(fns) >= 4, f"{path} is not a valid post file"
        self.year = fns[0]
        self.month = fns[1]
        self.day = fns[2]
        self.name = "-".join(fns[3:])
        self.addr = os.path.join(self.year, self.month, self.name + ".html")
        self.url = parse.urljoin(root_url, self.addr)
        meta, self.content = self.extract_meta_content(path)
        self.title = meta["title"]


class Site:
    def __init__(self) -> None:
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

    def build(self):
        alllinks = []
        for post in sorted(
            self._site.posts, key=lambda x: (x.year, x.month, x.day), reverse=True
        ):
            abspath = os.path.join(outdir, post.addr)
            dirname = os.path.dirname(abspath)
            os.makedirs(dirname, exist_ok=True)

            with open(abspath, "w", encoding="utf-8") as f:
                posthtml = self.page_temp.replace("{{page.title}}", post.title)
                posthtml = posthtml.replace("{{page.content}}", post.content)
                f.write(bs(posthtml, "html.parser").prettify())

            print(f"build post: {post.addr} --- DONE")
            alllinks.append(f'<a href="{post.addr}">{post.title}</a>')

        for page in self._site.pages:
            abspath = os.path.join(outdir, page.addr)
            with open(abspath, "w", encoding="utf-8") as f:
                pagecontent = page.content.replace(
                    "{{site.pages}}", "<br>\n".join(alllinks)
                )
                pagecontent = pagecontent.replace("{{date}}", str(date.today()))
                pagehtml = self.page_temp.replace("{{page.title}}", page.title)
                pagehtml = pagehtml.replace("{{page.content}}", pagecontent)
                f.write(bs(pagehtml, "html.parser").prettify())
                print(f"build page: {page.addr} --- DONE")


if __name__ == "__main__":
    site = Site()

    for fname in os.listdir(os.path.join(root, "_posts")):
        fpath = os.path.join(root, "_posts", fname)
        post = Post()
        post.load(fpath)
        site.add_post(post)

    for fname in os.listdir(root):
        if not fname.endswith(".page"):
            continue
        fpath = os.path.join(root, fname)
        page = Page()
        page.load(fpath)
        site.add_page(page)

    builder = Builder(site)
    builder.build()
