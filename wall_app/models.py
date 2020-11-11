from django.db import models
from the_app.models import User
#import the_app.models as user_app
# Create your models here.

class Message(models.Model):
    message = models.TextField()
    owner = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Message object: ID : {self.id} Message : {self.message}, Owner : {self.owner}>\n"


class Comment(models.Model):
    comment = models.TextField()
    owner = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"<Comment object: ID : {self.id}, Comment : {self.comment}, Message : {self.message}, Owner : {self.owner} >\n"