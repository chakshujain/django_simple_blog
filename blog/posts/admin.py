from django.contrib import admin

# Register your models here.
from posts.models import Post,Author
admin.site.register(Post)
admin.site.register(Author)
