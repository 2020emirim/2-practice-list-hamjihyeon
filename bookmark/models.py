from django.db import models
from django.urls import reverse


class Bookmark(models.Model):
    site_name = models.CharField(max_length=20)
    url = models.URLField('site URL')

    def __str__(self):
        return "제목 : " + self.site_name + ", URL : " + self.url

    def get_absolute_url(self):
        return reverse('bookmark:detail', kwargs={'pk': self.id})  # {% url 'bookmark:detail', pk=bookmark.id %}
