from django.db import models

class feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    feedback = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
