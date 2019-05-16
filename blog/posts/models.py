from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    author = models.ForeignKey('Author',on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f"{self.slug}/"

    def get_update_url(self):
        return f"update/"

    def get_delete_url(self):
        return f"delete/"

class Author(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    email = models.EmailField()
    phone_no = models.IntegerField()

    def __str__(self):
        return self.user.username
