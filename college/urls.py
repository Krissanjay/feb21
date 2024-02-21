from . import views
from django.urls import path
app_name='college'
urlpatterns = [
    path('',views.demo,name='demo'),
    # path('register/',views.register,name='register'),
    # path('login/',views.login,name='login')
    # path('add/',views.addition,name='addition')
]
