from django.urls import path
from .views import render_posts, post_detail

app_name="blog"

urlpatterns = [
    path('', render_posts, name='posts'),  # Agrega una coma aquí
    path("<int:post_id>", post_detail, name='post_detail'),  # Agrega un nombre para la segunda ruta
]
