from django.shortcuts import render,redirect
from blog.models import Article,Category
from home_app.models import NewsletterSubscriber
from accounts.forms import UserEditForm
from .forms import ArticleForm,NewsletterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def home(request):
    edit_form = None

    if request.user.is_authenticated:
        edit_form = UserEditForm(instance=request.user)



    return render(request, "home_app/index.html", {
        "edit_form": edit_form,
    })

def about(request):
    return render(request, 'home_app/about.html')

def blog(request):
    articles = Article.objects.filter(status=True)
    return render(request, "blog/blog.html", {
        "articles": articles
    })

@login_required
def add_article(request):

    if request.method == 'POST':

        form = ArticleForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            article = form.save(commit=False)



            # بررسی تکراری بودن slug
            if Article.objects.filter(
                slug=article.slug
            ).exists():

                form.add_error(
                    'title',
                    'مقاله‌ای با این عنوان قبلاً وجود دارد.'
                )

            else:
                article.author = request.user
                article.status = True
                article.save()

                return redirect(
                    'blog:article',
                    slug=article.slug
                )

    else:
        form = ArticleForm()

    categories = Category.objects.all()

    return render(
        request,
        'home_app/index.html',
        {
            'form': form,
            'categories': categories,
        }
    )
def newsletter_subscribe(request):

    if request.method == "POST":

        form = NewsletterForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']

            if NewsletterSubscriber.objects.filter(email=email).exists():

                messages.warning(
                    request,
                    "این ایمیل قبلاً عضو مقالات برگزیده شده است."
                )

            else:

                form.save()

                messages.success(
                    request,
                    "عضویت شما با موفقیت انجام شد."
                )

        return redirect('about')

    return redirect('about')

def faq(request):
    return render(request, "home_app/faq.html")


def privacy(request):
    return render(request, "home_app/privacy.html")


def terms(request):
    return render(request, "home_app/terms.html")