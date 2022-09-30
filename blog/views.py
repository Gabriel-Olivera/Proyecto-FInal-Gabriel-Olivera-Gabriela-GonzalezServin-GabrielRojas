from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import CreateView, ListView
from .forms import *
from .models import Blog
from django.urls import reverse_lazy


# class MostrarPostFormView(FormView):
#     template_name = "crear_post.html"
#     form_class = CrearPostForm
#     success_url = reverse_lazy("crear-post")


class CrearPostView(CreateView):
    model = Blog
    template_name = "crear_post.html"
    fields = ["titulo", "cuerpo"]
    success_url = reverse_lazy("listar-post")


class ListarPostViews(ListView):
    model = Blog
    # queryset = Blog.objects.all()
    template_name = "listar_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["obj"] = self.get_queryset()
        return context
