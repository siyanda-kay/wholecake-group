from django import forms
from .models import ConsultationRequest, ContactMessage

_INPUT = 'form-input'
_TEXTAREA = 'form-input resize-none'


class HoneypotMixin:
    def clean_website_url(self):
        if self.cleaned_data.get('website_url'):
            raise forms.ValidationError('Invalid submission.')
        return ''


class ConsultationForm(HoneypotMixin, forms.ModelForm):
    website_url = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'tabindex': '-1', 'autocomplete': 'off'}))

    class Meta:
        model = ConsultationRequest
        fields = ['name', 'company', 'email', 'phone', 'num_employees', 'num_female_employees', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Your full name', 'autocomplete': 'name'}),
            'company': forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Company name', 'autocomplete': 'organization'}),
            'email': forms.EmailInput(attrs={'class': _INPUT, 'placeholder': 'Work email address', 'autocomplete': 'email'}),
            'phone': forms.TextInput(attrs={'class': _INPUT, 'placeholder': '+27 ...', 'autocomplete': 'tel'}),
            'num_employees': forms.NumberInput(attrs={'class': _INPUT, 'placeholder': 'e.g. 250', 'min': '1'}),
            'num_female_employees': forms.NumberInput(attrs={'class': _INPUT, 'placeholder': 'e.g. 120', 'min': '1'}),
            'message': forms.Textarea(attrs={'class': _TEXTAREA, 'placeholder': 'Additional requirements or questions (optional)', 'rows': '3'}),
        }
        labels = {
            'num_employees': 'Total Employees',
            'num_female_employees': 'Female Employees',
            'message': 'Additional Notes',
        }


class ContactForm(HoneypotMixin, forms.ModelForm):
    website_url = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'tabindex': '-1', 'autocomplete': 'off'}))

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Your name', 'autocomplete': 'name'}),
            'email': forms.EmailInput(attrs={'class': _INPUT, 'placeholder': 'Email address', 'autocomplete': 'email'}),
            'phone': forms.TextInput(attrs={'class': _INPUT, 'placeholder': 'Phone number (optional)', 'autocomplete': 'tel'}),
            'message': forms.Textarea(attrs={'class': _TEXTAREA, 'placeholder': 'How can we help you?', 'rows': '4'}),
        }
