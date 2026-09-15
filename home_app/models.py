from django.db import models

# Create your models here.
class NewsletterSubscriber(models.Model):
    email = models.EmailField(
        unique=True,
        verbose_name="ایمیل"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ عضویت"
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "عضو مقالات برگزیده"
        verbose_name_plural = "اعضای مقالات برگزیده"