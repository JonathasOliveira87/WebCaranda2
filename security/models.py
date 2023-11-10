from django.db import models

class SecurityList(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.title},{self.text}'
    
