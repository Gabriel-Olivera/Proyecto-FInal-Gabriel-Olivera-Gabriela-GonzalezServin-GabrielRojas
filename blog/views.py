from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import *
from .models import Blog
from django.urls import reverse_lazy


# class MostrarPostFormView(FormView):
#     template_name = "crear_post.html"
#     form_class = CrearPostForm
#     success_url = reverse_lazy("crear-post")


class ListarPostViews(ListView):
    model = Blog
    # queryset = Blog.objects.all()
    template_name = "listar_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["obj"] = self.get_queryset()
        return context


class LeerPostViews(DetailView):
    model = Blog
    template_name = "leer_post.html"


class CrearPostView(CreateView):
    model = Blog
    template_name = "crear_post.html"
    fields = ["titulo", "subtitulo", "cuerpo", "imagen"]
    success_url = reverse_lazy("listar_post")

class EditarPostViews(UpdateView):
    model=Blog
    template_name='editar_post.html'
    fields=["titulo", "subtitulo", "cuerpo", "imagen"]
    success_url = reverse_lazy("listar_post")

class BorrarPostViews(DeleteView):
    model=Blog
    template_name='borrar_post.html'
    success_url = reverse_lazy("listar_post")

