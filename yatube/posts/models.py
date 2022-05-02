from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=300)  # название группы
    slug = models.SlugField(
        primary_key=True,
        max_length=100,
        unique=True,
        blank=False,
        )
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        max_length=200,
        on_delete=models.CASCADE,
        related_name='group_name'
    )

    class Meta:
        ordering = ['-pub_date']
