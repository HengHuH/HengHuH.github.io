[About Me]( {{ site.url }}/about.html )

------------

{% for post in site.posts %}
> <big>{{ post.title }}</big>

{{ post.excerpt }}
[阅读全文]( {{ post.url }} )

<small>Post by {{ post.author }}, {{ post.date | date: "%-d %B %Y" }}</small>

------------------

{% endfor %}
