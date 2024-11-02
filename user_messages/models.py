from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.number} - {self.email} - {self.timestamp}"
