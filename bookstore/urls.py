from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('books/', views.books, name='books'),
    path('browse_sort/', views.browse_sort_view, name='browse_sort'),
    path('contact/', views.contact, name='contact'),
    path('reviews/', views.reviews, name='reviews'),
    path('wishlist/', views.wishlist, name='wishlist'),

]
