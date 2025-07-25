from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gembot_messages') # we can do with related_name: user.gembot_messages.all() to get all messages by that user.
    question = models.TextField()
    answer = models.TextField()
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"(self.email): {self.question[:20]}"
 