from django import forms
from blog.models import Article
from .models import NewsletterSubscriber

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'category', 'body', 'image']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'عنوانی جذاب و واضح انتخاب کنید...',
                'maxlength': '90',
            }),

            'category': forms.Select(attrs={
                'class': 'form-select',
            }),

            'body': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'محتوای کامل مقاله را اینجا بنویسید...',
                'style': 'min-height:220px',
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-input',
            }),
        }


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = NewsletterSubscriber
        fields = ['email']

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'ایمیل خود را وارد کنید',
                }
            )
        }