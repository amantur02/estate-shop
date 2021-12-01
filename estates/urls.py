from django.urls import path
from .views import main_page, all_properties, new_properties, rent_properties, sale_properties, estate_detail

urlpatterns = [
    path('single-detail/<int:pk>/', estate_detail, name='estate_detail'),
    path('properties/', all_properties, name='properties'),
    path('new-properties/', new_properties, name='new_properties'),
    path('rent-properties/', rent_properties, name='rent_properties'),
    path('sale-properties/', sale_properties, name='sale_properties'),
    path('', main_page, name='main_page'),

]
