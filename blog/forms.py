from django import forms

from blog.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "subject", "text", "email"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "نام شما..."
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-input",
                "placeholder": "email@example.com"
            }),

            "subject": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "موضوع..."
            }),

            "text": forms.Textarea(attrs={
                "class": "form-textarea",
                "placeholder": "پیام شما..."
            }),
        }