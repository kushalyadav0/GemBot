from django.db import models

# Create your models here.
class Chat(models.Model):
    question = models.CharField(max_length=254, blank=True, null=True)
    answer = models.TextField()
    date_asked = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question
 