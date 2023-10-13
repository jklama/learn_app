from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name ="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('create_form/', views.create_form,name="create_form"),
    path('update_room/<str:pk>/', views.updateRoom,name="update_room"),
]
