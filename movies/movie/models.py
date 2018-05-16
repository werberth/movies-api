from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    year = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        '{0} [{1}]'.format(self.title, self.year)
