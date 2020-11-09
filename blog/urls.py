from django.urls import path
from . import views



urlpatterns = [
    path("", views.blog, name="Blog"),
    path("categorias/<int:categoria_id>/", views.categoria, name="categoria" )
]


