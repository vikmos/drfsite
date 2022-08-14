from django.contrib import admin

from .models import User, News, Comment
# Register your models here.
admin.site.register(News)
admin.site.register(User)
admin.site.register(Comment)
