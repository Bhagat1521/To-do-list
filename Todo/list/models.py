from django.db import models

# Create your models here.
class task(models.Model):
    ID = models.CharField(max_length=20, primary_key=True)
    Task = models.CharField(max_length=70)
    
    def __str__(self):
        return self.Task
    