from logging import exception
from math import ceil
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.db.models import Q
from products import models, forms


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


def search(request):
    keyword = request.GET.get("keyword", None)
    price = request.GET.getlist("price", None)
    brands = request.GET.getlist("brands", None)
    form = forms.SearchForm(request.GET)

    filter_args = {}
    if form.is_valid():
        q = Q()
        if len(brands) > 0:
            # models.Product.objects.filter(brand__id__in=brands)
            filter_args["brand__id__in"] = brands
        if len(price) > 0:
            if "-100000" in price:
                q.add(Q(released_price__lte=100000), q.OR)
            if "100000-300000" in price:
                q.add(Q(released_price__gte=100000, released_price__lte=300000), q.OR)
            if "300000-500000" in price:
                q.add(Q(released_price__gte=300000, released_price__lte=500000), q.OR)
            if "500000-" in price:
                q.add(Q(released_price__gte=500000), q.OR)
            result = models.Product.objects.filter(q)
        if keyword is not None and keyword != "":
            q.add(
                Q(name_en__contains=keyword)
                | Q(model_number__contains=keyword)
                | Q(brand__name__contains=keyword),
                q.AND,
            )

    result = models.Product.objects.filter(q, **filter_args)
    return render(
        request,
        "products/search.html",
        {"result": result, "keyword": keyword, "price": price, "form": form},
    )


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
