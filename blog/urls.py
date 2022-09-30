from .views import CrearPostView, ListarPostViews
from django.urls import path

urlpatterns = [
    path("crear/post/", CrearPostView.as_view(), name="crear-post"),
    path("mostrar/post", ListarPostViews.as_view(), name="listar-post"),
]
