from django.views.generic import ListView
from django.shortcuts import render
from . import models

# Create your views here.


class StyleListView(ListView):
    model = models.Style
    template_name = "style/style_list.html"
    context_object_name = "styles"
