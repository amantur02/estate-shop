from django.urls import path

from blogs.views import posts, post_detail, create_post, post_update, my_posts, post_delete

urlpatterns = [
    path('create-post/', create_post, name='create_post'),
    path('single-post/<int:pk>/', post_detail, name='single_post'),
    path('update-post/<int:pk>/', post_update, name='update_post'),
    path('delete-post/<int:pk>/', post_delete, name='delete_post'),
    path('my-posts/', my_posts, name='my_posts'),
    path('', posts, name='posts'),

]