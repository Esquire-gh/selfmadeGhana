from django.contrib import admin
from .models import Article, Comment, Discussion, Suggestion

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Discussion)
admin.site.register(Suggestion)