from django.db import models
from django.contrib import admin

class BQBlog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:
        ordering = ('-timestamp',)


class BQBlogAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(BQBlog, BQBlogAdmin)
