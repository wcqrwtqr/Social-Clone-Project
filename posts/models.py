from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka
from groups.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
#Post model.py

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts') #TODO on_delete will be requested later
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    groups = models.ForeignKey(Group,related_name='posts',null=True,blank=True)

    def __str__(self):
        return self.message

    def save(self, *args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk}) #TODO check on the user.username it might have some issues
    class Meta:
        ordering = ['-created_at']
        unique_together = ('user','message')







