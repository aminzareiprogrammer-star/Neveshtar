from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100,verbose_name='عنوان')
    created = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ انتشار')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='نویسنده')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='دسته بندی',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=90,verbose_name='عنوان')
    body = models.TextField(verbose_name='متن')
    image = models.ImageField(upload_to='images/',verbose_name='تصویر',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ انتشار')
    updated = models.DateTimeField(auto_now=True,verbose_name='تاریخ آخرین بروزرسانی')
    status = models.BooleanField(default=False,verbose_name='وضعیت')
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='نام صفحه'
    )



    def save(self, *args, **kwargs):
        self.slug = slugify(
            self.title,
            allow_unicode=True
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def show_image(self):
        if self.image:
            return format_html(
                '<img src="{}" width="70" height="70">',
                self.image.url
            )
        return "بدون تصویر"


    class Meta:
        ordering = ['-created']
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments',verbose_name='مقاله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',verbose_name='کاربر')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True,verbose_name='در پاسخ به')
    text = models.TextField(verbose_name='متن')
    created = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ انتشار')

    def __str__(self):
        return self.text[:50]

    class Meta:
        ordering = ['created']
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

class Message(models.Model):
    name = models.CharField(max_length=33,verbose_name='نام')
    subject = models.CharField(max_length=100,verbose_name='عنوان')
    text = models.TextField(verbose_name='متن')
    email = models.EmailField(verbose_name='ایمیل')
    created = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ انتشار')

    def __str__(self):
        return self.subject
    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes',verbose_name='نام مقاله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes',verbose_name='نام کاربر')
    created = models.DateTimeField(auto_now_add=True,null=True,verbose_name='زمان لایک')
    def __str__(self):
        return self.user.username
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "article"],
                name="unique_user_article_like"
            )
        ]
        verbose_name = 'لایک مقاله'
        verbose_name_plural = 'لایک های مقاله '
        ordering = ['-created']

class LikeComment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نام کاربر')
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name="likes",verbose_name='نام کامنت')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='زمان لایک')
    class Meta:
        verbose_name = 'لایک کامنت '
        verbose_name_plural = 'لایک های کامنت'
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=["user", "comment"],
                name="unique_user_comment_like"
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.comment}"