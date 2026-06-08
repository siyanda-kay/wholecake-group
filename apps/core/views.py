from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from apps.leads.forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save()
            _notify_contact(obj)
            messages.success(request, 'Message received! We will get back to you shortly.')
            return redirect('core:home')
    else:
        form = ContactForm()
    return render(request, 'core/home.html', {'contact_form': form})


def about(request):
    return render(request, 'core/about.html')


def _notify_contact(obj):
    try:
        recipient = getattr(settings, 'NOTIFICATION_EMAIL', settings.DEFAULT_FROM_EMAIL)
        send_mail(
            subject=f'[WHOLECAKE] New Contact Message — {obj.name}',
            message=(
                f'New contact message received.\n\n'
                f'Name: {obj.name}\n'
                f'Email: {obj.email}\n'
                f'Phone: {obj.phone or "N/A"}\n\n'
                f'Message:\n{obj.message}\n'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            fail_silently=True,
        )
    except Exception:
        pass
