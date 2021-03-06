from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}"

class Post(models.Model):
    writed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posted", null=False)
    post_message = models.TextField(max_length=150)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.id} {self.writed_by} ${self.post_message} // {self.timestamp} "
    
    def serialize(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "post_message": self.post_message
        }

class Like(models.Model):
    like_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    like_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, related_name="like_post")
    
    class Meta:
        unique_together = ('like_user', 'like_post')
    
    def __str__(self):
        return f"{self.like_user} puso like a {self.like_post}"

class Following(models.Model):
    influencer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followed" ,null=False)
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following", null=False)
    
    class Meta:
        unique_together = ('follower', 'influencer')

    def __str__(self):
        return f"{self.follower.id} sigue a {self.influencer.id}"
