# -*- coding: utf-8 -*-

"""HengHuH.github.io 的构建脚本。

依赖：python3, yaml, markdown
"""

import os
from datetime import date
import yaml
import markdown
from bs4 import BeautifulSoup as bs
from urllib import parse


root = os.path.dirname(os.path.abspath(__file__))
root_url = "https://henghuh.github.io"


class Post:
    def __init__(self) -> None:
        self.year = "2024"
        self.month = "01"
        self.day = "01"
        self.name = ""

        self.addr = ""
        self.url = ""
        self.title = ""
        self.content = ""

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

        with open(path, "r", encoding="utf-8") as f:
            fc = f.read()
            fc = fc.strip()
            if fc.startswith("---"):
                fc = fc[3:]
                idx = fc.find("---")
                meta = yaml.safe_load(fc[:idx])
                self.title = meta["title"]
                self.content = markdown.markdown(fc[idx + 3 :])
            else:
                raise ValueError(f"{path} is not a valid post file, missing meta data")


class Site:
    def __init__(self) -> None:
        self._posts = set()

    def add_post(self, post):
        self._posts.add(post)

    @property
    def posts(self):
        return self._posts


class Builder:
    def __init__(self, site) -> None:
        self._site = site

        with open(os.path.join(root, "post_page"), 'r', encoding='utf-8') as f:
            self.post_page = f.read()

        with open(os.path.join(root, 'index_page'), 'r', encoding="utf-8") as f:
            self.index_page = f.read()

    def build(self):
        alllinks = []
        for post in sorted(self._site.posts, key=lambda x: (x.year, x.month, x.day), reverse=True):
            abspath = os.path.join(root, post.addr)
            dirname = os.path.dirname(abspath)
            os.makedirs(dirname, exist_ok=True)

            with open(abspath, "w", encoding="utf-8") as f:
                posthtml = self.post_page.replace("{{post.title}}", post.title)
                posthtml = posthtml.replace("{{post.content}}", post.content)
                f.write(bs(posthtml, 'html.parser').prettify())

            print(f"build post: {post.addr} --- DONE")
            alllinks.append(f"<a href=\"{post.addr}\">{post.title}</a>")

        with open(os.path.join(root, 'index.html'), 'w', encoding='utf-8') as f:
            content = self.index_page.replace("{{allposts}}", "<br>\n".join(alllinks))
            content = content.replace("{{date}}", str(date.today()))
            f.write(bs(content, 'html.parser').prettify())

        print("write index page --- DONE.")


if __name__ == "__main__":
    site = Site()

    for fname in os.listdir(os.path.join(root, "_posts")):
        fpath = os.path.join(root, "_posts", fname)
        post = Post()
        post.load(fpath)
        site.add_post(post)

    builder = Builder(site)
    builder.build()
