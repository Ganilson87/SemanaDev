from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Publication(models.Model):
    titulo = models.CharField(max_length=50, blank=False)
    descricao = models.TextField(max_length=1000, blank=False)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return (f' {self.titulo} - {self.user.first_name}  {self.user.last_name}')
