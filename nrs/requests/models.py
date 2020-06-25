from django.db import models

# Create your models here.

class RequestItem(models.Model):
    content = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.content