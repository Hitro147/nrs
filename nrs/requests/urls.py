from django.urls import path
from . import views

urlpatterns = [
    path('', views.requests, name = "requests"),
    path('addReq/', views.addReq, name = "addReq"),
    path('upvote/<int:request_id>/', views.upvote, name = "upvote"),
]