[About Me]( {{ site.url }}/about.html )

------------

{% for post in site.posts %}
> {{ post.title }}

{{ post.excerpt }}  
...

Post by: {{ post.author }}, {{ page.date | date: "%-d %B, %Y" }}  
[阅读全文]( {{ post.url }} )

------------------
{% endfor %}
