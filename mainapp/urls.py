from django.urls import path
from .views import upload_file, titanic_list, upload_success, passenger_create_or_update, passenger_delete, passenger_edit

urlpatterns = [
    path('', upload_file, name='upload_file'),
    path('titanic/', titanic_list, name='titanic_list'),
    path('success/', upload_success, name='success'),
    path('passenger/new/', passenger_create_or_update, name='passenger_create'),
    path('passenger/edit/<int:pk>/', passenger_edit, name='passenger_edit'),
    path('passenger/delete/<int:pk>/', passenger_delete, name='passenger_delete'),]
