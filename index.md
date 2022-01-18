[About Me]( {{ site.url }}/about.html )

------------

{% for post in site.posts %}
> {{ post.title }}

{{ post.excerpt }}
... [阅读全文]( {{ post.url }} )

Post by {{ post.author }}, {{ post.date | date: "%-d %B %Y" }}

------------------

{% endfor %}
