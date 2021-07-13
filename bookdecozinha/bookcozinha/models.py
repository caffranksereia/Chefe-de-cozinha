from django.db import models

# Create your models here.
class Todo(models.Model):
    todo = models.TextField(max_length= 150)
    title_todo = models.CharField(max_length=60)
    edit = models.BooleanField()
    delete = models.BooleanField()
    data = models.DateField(auto_now=True)



