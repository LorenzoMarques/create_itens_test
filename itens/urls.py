from django.urls import path
from . import views

urlpatterns = [
    path("itens/", views.ListCreateItemView.as_view()),
    path("itens/<pk>/", views.RetrieveUpdateItemView.as_view())
]