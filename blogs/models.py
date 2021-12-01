from django.db import models

from users.models import Profile


class Category(models.Model):
    COLOR_CHOICES = (
        ('grey', 'grey'),
        ('red', 'red'),
        ('aqua', 'aqua'),
        ('yellow', 'yellow'),
        ('pink', 'pink'),
        ('green', 'green'),
    )

    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                               blank=True, null=True)
    title = models.CharField(max_length=40)
    heading = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='blogs')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True,
                               related_name='replies', on_delete=models.CASCADE, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # sort comments in chronological order by default
        ordering = ('date_created',)

    def __str__(self):
        return 'Comment by {}'.format(self.post.title)
