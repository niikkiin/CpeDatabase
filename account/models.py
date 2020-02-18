from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # additional
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    def __str__(self):
        return self.user.username

class Log(models.Model):

    user        = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    action      = models.TextField()
    created_at  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.action


# class LogManager(models.Manager):
#     def create_log(self, account):
        

    # def update_log(self):

    # def delete_log(self):
    