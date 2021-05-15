from django.db import models

# Create your models here.


class todo(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=1000)
    isdone = models.BooleanField(default=False)

    def __str__(self):
        return self.title
