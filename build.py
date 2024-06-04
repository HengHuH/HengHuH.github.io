# -*- coding: utf-8 -*-

"""HengHuH.github.io 的构建脚本。

依赖：python3, yaml, markdown
"""

import os
import yaml
import markdown
from urllib import parse


root = os.path.dirname(os.path.abspath(__file__))
root_url = "https://henghuh.github.io"

post_template = """<!DOCTYPE html>
<html>

<head>
    <meta content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{post.title}}</title>
</head>

<body>
    {{post.content}}
    <hr>
    Heng - <a href="https://henghuh.github.io">https://henghuh.github.io</a>
</body>

</html>
"""

index_page = """<!DOCTYPE html>
<html>

<head>
    <meta content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heng's Home Page</title>
</head>

<body>
    <div align="right">
        <a href="https://github.com/HengHuH">GitHub Page</a>
    </div>
    <h2>工作</h2>
    <h2>Post</h2>
    {{allposts}}
    <hr>
    联系我: huangxinghuh@163.com<br>
    <font size="-1">最近更新: 2024-3-30</font-size>
</body>

</html>"""


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
        self.name = " ".join(fns[3:])
        self.addr = os.path.join(self.year, self.month, self.day, self.name + ".html")
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

    def build(self):
        alllinks = []
        for post in sorted(self._site.posts, key=lambda x: (x.year, x.month, x.day)):
            abspath = os.path.join(root, post.addr)
            dirname = os.path.dirname(abspath)
            os.makedirs(dirname, exist_ok=True)

            with open(abspath, "w", encoding="utf-8") as f:
                posthtml = post_template.replace("{{post.title}}", post.title)
                posthtml = post_template.replace("{{post.content}}", post.content)
                f.write(posthtml)

            print(f"build post: {post.addr} --- DONE")
            alllinks.append(f"<a href=\"{post.addr}\">{post.name}</a>")

        with open(os.path.join(root, 'index.html'), 'w', encoding='utf-8') as f:
            content = index_page.replace("{{allposts}}", "<br>\n".join(alllinks))
            f.write(content)

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