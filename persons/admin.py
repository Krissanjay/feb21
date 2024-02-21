from django.contrib import admin

# Register your models here.


# Register your models here.

from .models import Movie
from .models import Comment
from .models import CartItem



admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(CartItem)



