from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    Title = models.CharField(max_length=100)
    Heading = models.CharField(max_length=100)
    para = models.CharField(max_length=100)
    author = models.ForeignKey('author', on_delete=models.CASCADE, null=False)
    tag = (('horror','horror'), ('fiction', 'fiction'), ('science', 'science'),
        ('literature', 'literature'),
        ('blog', 'blog'))
    type = models.CharField(max_length=30, choices=tag, default='blog')

    def __str__(self):
        return self.Title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return self.first_name

