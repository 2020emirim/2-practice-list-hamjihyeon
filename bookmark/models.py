from django.db import models


class Bookmark(models.Model):
    site_name = models.CharField(max_length=20)
    url = models.URLField('site URL')

    def __str__(self):
        return "제목 : "+ self.site_name + ", URL : "+self.url