# from urllib import request
import os
from uuid import uuid4
import requests
from pydoc import resolve
from django.shortcuts import redirect, render, resolve_url
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from django.urls import reverse_lazy
from . import forms, models
import string
import random


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


def kakao_login(request):
    REST_API_KEY = os.environ.get("KAKAO_REST_API_KEY")
    REDIRECT_URI = "http://127.0.0.1:8000/users/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code"
    )


class KakaoException(Exception):
    pass


def kakao_callback(request):
    try:
        code = request.GET.get("code")
        client_id = os.environ.get("KAKAO_REST_API_KEY")
        redirect_url = "http://127.0.0.1:8000/users/login/kakao/callback"
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_url={redirect_url}&code={code}"
        )
        token_json = token_request.json()
        error = token_json.get("error", None)
        if error is not None:
            raise KakaoException()
        access_token = token_json.get("access_token")
        profile_request = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()
        kakao_account = profile_json.get("kakao_account")
        email = kakao_account.get("email", None)

        if email is None:
            email = f"{uuid4().hex}@kakao.com"

        nickname = kakao_account.get("profile").get("nickname")
        profile_image = kakao_account.get("profile").get("profile_image_url")

        try:
            user = models.User.objects.get(email=email)
        except models.User.DoesNotExist:
            _LENGTH = 8
            string_pool = string.digits
            result = ""
            for i in range(_LENGTH):
                result += random.choice(string_pool)
            user = models.User.objects.create(
                username=email,
                email=email,
                first_name=nickname,
                phone_number=f"010{result}",
            )
            user.set_unusable_password()
            user.save()
        login(request, user)
        return redirect(resolve_url("products:list"))

    except KakaoException:
        return redirect(resolve_url("users:login"))
