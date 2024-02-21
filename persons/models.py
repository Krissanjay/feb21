from datetime import datetime

from django.db import models
from django.utils.text import slugify

# Create your models here.
from django.contrib.auth.models import User

from django.db import models
from datetime import datetime


# Create your models here.



class Movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    release_date=models.DateField()
    actors=models.CharField(max_length =100)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    category= models.CharField(max_length = 15)
    img=models.ImageField(upload_to='gallery')
    trailer = models.URLField(blank=True, null=True)
    favorite=models.ManyToManyField(User,related_name='favorite',blank=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.movie.name, self.commenter_name)


class CartItem(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quantity} x {self.movie.name}'

