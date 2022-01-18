[About Me]( {{ site.url }}/about.html )

------------

{% for post in site.posts %}
> {{ post.title }}  
{{ post.excerpt }}  
------------------
{{ post.author }} {{ post.time }} [阅读全文]( {{ post.url }} )
{% endfor %}
