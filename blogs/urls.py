from django.urls import path

from blogs.views import posts, post_detail

urlpatterns = [
    path('single-post/<int:pk>/', post_detail, name='single_post'),
    path('', posts, name='posts'),

]