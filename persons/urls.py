from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('profile', views.profile, name='profile'),
    path('index', views.index, name='index'),
    path('message', views.message, name='message'),
    path('message', views.message, name='message'),
    path('add/',views.add_movie,name='add_movie'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('profile', views.profile, name='profile'),
    path('category', views.category, name='category'),
    path('thriller', views.thriller, name='thriller'),
    path('drama', views.drama, name='drama'),
    path('horror', views.horror, name='horror'),
    path('adventure', views.adventure, name='adventure'),
    path('scifi', views.scifi, name='scifi'),
    path('action', views.action, name='action'),
    path('update_user', views.update_user, name='update_user'),
    path('update_password', views.update_password, name='update_password'),
    path('movie_list', views.movie_list, name='movie_list'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('movie/<int:pk>/add_comment', views.add_comment, name='add_comment'),
    path('movie/<int:pk>/delete_comment', views.delete_comment, name='delete_comment'),
    path('search/', views.searchBar, name='search'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:movie_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('add_to_fav/<int:id>', views.add_to_fav, name='add_to_fav'),
    # path('fav_list', views.fav_list, name='fav_list'),
    # path('remove_fav/<int:product_id>/',views.remove_fav,name='remove_fav'),
    # path('full_remove/<int:product_id>/', views.full_remove, name='full_remove')
]