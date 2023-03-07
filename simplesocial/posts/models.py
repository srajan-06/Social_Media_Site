from django.db import models
from django.conf import settings
from django.urls import reverse

import misaka

from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model() #For Getting the current uset logged into the session

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True) #For automatically connecting the date to the posts
    message = models.TextField()
    message_html = models.TextField(editable = False) #Bcoz the misaka coverted one is the finalised message without odds...
    group = models.ForeignKey(Group,related_name='posts',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = self.message
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})

    class Meta():
        ordering = ['-created_at']
        unique_together = ['user','message'] #Every message is uniquely linked to the user
