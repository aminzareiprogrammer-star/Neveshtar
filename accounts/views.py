from django.contrib.auth import  login, logout
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm, UserEditForm ,ProfileImageForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            login(request, form.cleaned_data["user"])
            return redirect("home")

    else:
        form = LoginForm()

    return render(request, "home_app/index.html", {
        "form": form
    })

def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            messages.success(
                request,
                "ثبت‌نام با موفقیت انجام شد."
            )

            return redirect("home")

        messages.error(
            request,
            "اطلاعات وارد شده صحیح نیست."
        )

        return redirect("home")

    return redirect("home")

@login_required
def edit_view(request):
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "اطلاعات شما با موفقیت ویرایش شد."
            )
        else:
            messages.error(
                request,
                "اطلاعات وارد شده صحیح نیست."
            )

    return redirect("home")

@login_required
def profile_image_view(request):
    profile_obj, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = ProfileImageForm(
            request.POST,
            request.FILES,
            instance=profile_obj
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "تصویر پروفایل با موفقیت ذخیره شد."
            )

    return redirect("home")

def logout_view(request):
    logout(request)
    messages.success(request, "👋 به سلامت!")
    return redirect("home")