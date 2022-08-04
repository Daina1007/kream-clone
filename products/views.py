from logging import exception
from math import ceil
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.utils import timezone


class ProductDetail(DetailView):
    model = models.Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


def detail(request, pk):

    product = models.Product.objects.get(id=pk)
    print(product)
    return render(request, "products/detail.html", {"product": product})

    # try:
    #     product = models.Product.objects.get(id=pk)
    #     return render(request, "products/detail.html", {"product": product})
    # except models.Product.DoesNotExist:
    #     return redirect("/products")
    # except Exception:
    #     return redirect("/products")

    # 예외잡기


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

# def product_list(request):
#   page = int(request.GET.get("page", 1))
#   page_size = 13
#   limit = page_size * page
#   offset = limit - page_size
#   products = models.Product.objects.all()[offset:limit]
#   page_count = ceil(models.Product.objects.count() / page_size)
#   if page > page_count:
#     return redirect("/products")

#   if문 페이지가 마지막 페이지를 넘는다면 1페이지로 넘기는 것을 의미
#   파이썬만 사용해서


# product_list = models.Product.objects.all()
# paginator = Paginator(product_list, 13)
# products = paginator.get_page(page)

# get_page다음 괄호안에 page는 url에 적힌 page를 의미?

# 파이썬+장고


# return render(
#     request,
#     "product_list.html",
#     {
#         "products": products,
#         "page": page,
#     },
# )
