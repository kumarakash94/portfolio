from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 rounded-md'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 rounded-md'}),
            'message': forms.Textarea(attrs={'class': 'w-full px-4 py-2 rounded-md', 'rows': 4}),
        }