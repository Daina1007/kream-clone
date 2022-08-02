from math import ceil
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.utils import timezone


class ProductListView(ListView):
    model = models.Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    paginate_by = 13
    ordering = ["created"]
    paginate_orphans = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        context["daina"] = "Daina의 프로젝트"
        return context


# django templates만을 사용해서

# Create your views here.
# def product_list(request):
#     page = int(request.GET.get("page", 1))
# page_size = 13
# limit = page_size * page
# offset = limit - page_size
# page_count = ceil(models.Product.objects.count() / page_size)
# if page > page_count:
#     return redirect("/products")
# 파이썬만 사용해서


# product_list = models.Product.objects.all()
# paginator = Paginator(product_list, 13)
# products = paginator.get_page(page)
# 파이썬+장고


# return render(
#     request,
#     "product_list.html",
#     {
#         "products": products,
#         "page": page,
#     },
# )
