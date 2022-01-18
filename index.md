[About Me]( {{ site.url }}/about.html )

---

{% for post in site.posts %}
> <big>{{ post.title }}</big>

{{ post.excerpt }}
[_阅读全文_]( {{ post.url }} )

---

<p align="right"><small>Post by {{ post.author }}, {{ post.date | date: "%-d %B %Y" }}</small></p>

{% endfor %}
