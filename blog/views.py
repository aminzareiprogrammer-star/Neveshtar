from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Article, Category, Comment,Message,Like,LikeComment
from django.core.paginator import Paginator
from django.http import JsonResponse
from .forms import MessageForm
from django.db.models import Q
from django.contrib import messages
def blog(request):
    articles = Article.objects.filter(status=True)
    categories = Category.objects.all()

    if request.GET.get('my_articles') == '1':
        if request.user.is_authenticated:
            articles = articles.filter(author=request.user)

    paginator = Paginator(articles, 9)
    page_number = request.GET.get("page")
    articles = paginator.get_page(page_number)

    return render(request, "blog/blog.html", {
        "articles": articles,
        "categories": categories,
    })

def article(request, slug):
    article = get_object_or_404(
        Article,
        slug=slug,
        status=True
    )

    if request.method == "POST":

        if not request.user.is_authenticated:
            return redirect("login")

        text = request.POST.get("text", "").strip()
        parent_id = request.POST.get("parent_id")

        if text:
            parent = None
            if parent_id:
                parent = get_object_or_404(Comment, id=parent_id, article=article)

            Comment.objects.create(
                text=text,
                article=article,
                user=request.user,
                parent=parent,
            )
        return redirect("blog:article", slug=slug)

    return render(request, "blog/article.html", {"article": article})


def category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    articles = Article.objects.filter(
        category=category,
        status=True
    )

    paginator = Paginator(articles, 9)
    page_number = request.GET.get("page")
    articles = paginator.get_page(page_number)

    return render(request, "blog/blog.html", {
        "articles": articles,
        "current_category": category,
    })
def search(request):
    query = request.GET.get('q', '').strip()

    articles = Article.objects.filter(status=True)

    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)
        )

    paginator = Paginator(articles, 9)
    page_number = request.GET.get("page")
    articles = paginator.get_page(page_number)

    return render(request, 'blog/blog.html', {
        'articles': articles,
        'query': query,
    })
def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "پیام شما با موفقیت ارسال شد."
            )
            return redirect("blog:contact")

    else:
        form = MessageForm()

    return render(
        request,
        "blog/contact.html",
        {"form": form}
    )
@login_required
def like_view(request, slug, id):

    if request.method != "POST":
        return JsonResponse(
            {
                "success": False,
                "message": "درخواست نامعتبر است."
            },
            status=400
        )

    article = get_object_or_404(
        Article,
        id=id,
        slug=slug,
        status=True
    )

    like, created = Like.objects.get_or_create(
        user=request.user,
        article=article
    )

    if created:
        liked = True
    else:
        like.delete()
        liked = False

    return JsonResponse({
        "success": True,
        "liked": liked,
        "count": article.likes.count()
    })
@login_required
def like_comment(request, comment_id):

    if request.method != "POST":
        return JsonResponse({
            "success": False,
            "message": "درخواست نامعتبر است."
        }, status=400)

    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return JsonResponse({
            "success": False,
            "message": "کامنت پیدا نشد."
        }, status=404)

    like = LikeComment.objects.filter(
        user=request.user,
        comment=comment
    ).first()

    if like:
        # برداشتن لایک
        like.delete()
        liked = False
    else:
        # ثبت لایک
        LikeComment.objects.create(
            user=request.user,
            comment=comment
        )
        liked = True

    count = LikeComment.objects.filter(
        comment=comment
    ).count()

    return JsonResponse({
        "success": True,
        "liked": liked,
        "count": count
    })

@login_required
def my_articles(request):
    articles = Article.objects.filter(author=request.user)

    return render(request, 'blog/blog.html', {
        'articles': articles
    })