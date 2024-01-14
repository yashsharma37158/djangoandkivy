from django.db import models

# Create your models here.
# myapp/models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def _str_(self):
        return self.name