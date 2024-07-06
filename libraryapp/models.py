from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Books(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    issued=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
