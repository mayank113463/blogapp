from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    #here timezone.now() is a function but we dont want to run function we just want to call that function
    date_posted = models.DateTimeField(default = timezone.now) #create or update time and date
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
