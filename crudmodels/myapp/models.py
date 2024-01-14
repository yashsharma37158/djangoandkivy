from django.db import models

# Create your models here.
# myapp/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()

    def _str_(self):
        return self.title