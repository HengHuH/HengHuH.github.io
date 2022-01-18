[About Me]( {{ site.url }}/about.html )

------------

{% for post in site.posts %}
> <p align="left"><big>{{ post.title }}</big></p>

{{ post.excerpt }}
[阅读全文]( {{ post.url }} )

------------------

<p align="right"><small>Post by {{ post.author }}, {{ post.date | date: "%-d %B %Y" }}</small></p>

{% endfor %}
