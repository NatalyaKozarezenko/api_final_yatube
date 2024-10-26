from django.contrib.auth import get_user_model
from django.db import models

from yatube_api.settings import LOOK_LEN_TXT

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(r'^[0-9a-zA-Z]+$', max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True
    )

    def __str__(self):
        return (
            f'{self.text[:LOOK_LEN_TXT]} {self.pub_date} {self.author}'
            f'{self.group}'
        )


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        default_related_name = 'comments'


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follows'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followings'
    )
