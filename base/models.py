from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#null and blank permettono al momento della creazione della task che il valore possa essere nullo o vuoto
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title #imposta il titolo dell'elemento nel databse
    
    class Meta:
        ordering = ["complete"] #ordina gli elementi in base al complete


