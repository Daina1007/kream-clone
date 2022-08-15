# from urllib import request
from django.shortcuts import redirect, render, resolve_url
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from . import forms
from django.urls import reverse_lazy


class SignUpView(FormView):
    form_class = forms.SignUpForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("products:list")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    form_class = forms.LoginForm
    template_name = "users/login.html"
    success_url = reverse_lazy("products:list")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)
            # return redirect(resolve_url("products:list"))
        return super().form_valid(form)


# def login_view(request):
#     if request.method == "GET":
#         pass
#     if request.method == "POST":
#         email = request.POST.get("email")
#         # 괄호 안 이메일은 html이메일의 id를 의미함.
#         password = request.POST.get("password")
#         user = authenticate(request, username=email, password=password)
#         print(user)

#         if user is not None:
#             login(request, user)
#             return redirect(resolve_url("products:list"))

#     return render(
#         request,
#         "users/login.html",
#     )


def logout_view(request):
    logout(request)
    return redirect(resolve_url("users:login"))
