from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    
class Contact(models.Model):
    whatsapp = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address}, {self.whatsapp}, {self.lat}, {self.lng}"

