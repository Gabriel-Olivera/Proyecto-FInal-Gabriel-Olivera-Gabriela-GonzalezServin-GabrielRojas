from .views import CrearPostView, ListarPostViews, LeerPostViews, EditarPostViews, BorrarPostViews
from django.urls import path

urlpatterns = [
    path("", ListarPostViews.as_view(), name="listar_post"),
    path("leer_post/<int:pk>",LeerPostViews.as_view(), name="leer_post"),
    path("crear_post/", CrearPostView.as_view(), name="crear_post"),
    path("listar_post/", ListarPostViews.as_view(), name="listar_post"),
    path("editar_post/<int:pk>",EditarPostViews.as_view(), name="editar_post"),
    path("borrar_post/<int:pk>",BorrarPostViews.as_view(), name="borrar_post"),
]
