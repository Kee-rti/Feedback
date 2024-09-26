from django import forms
from .models import feedback


class feedbackform(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['name', 'email','feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
