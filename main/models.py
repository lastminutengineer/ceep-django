from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)                # User's name
    email = models.EmailField()                            # User's email
    subject = models.CharField(max_length=200)             # Message subject
    message = models.TextField()                            # The message body
    created_at = models.DateTimeField(auto_now_add=True)   # Timestamp when message was created

    def __str__(self):
        return f"{self.name} - {self.subject}"
