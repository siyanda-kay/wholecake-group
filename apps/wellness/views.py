from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from apps.leads.forms import ConsultationForm


def index(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            obj = form.save()
            _notify_consultation(obj)
            messages.success(request, 'Thank you! Our team will contact you within one business day.')
            return redirect('wellness:index')
    else:
        form = ConsultationForm()
    return render(request, 'wellness/index.html', {'consultation_form': form})


def _notify_consultation(obj):
    try:
        recipient = getattr(settings, 'NOTIFICATION_EMAIL', settings.DEFAULT_FROM_EMAIL)
        send_mail(
            subject=f'[WHOLECAKE] New Consultation Request — {obj.company}',
            message=(
                f'New consultation request received.\n\n'
                f'Name: {obj.name}\n'
                f'Company: {obj.company}\n'
                f'Email: {obj.email}\n'
                f'Phone: {obj.phone}\n'
                f'Total Employees: {obj.num_employees}\n'
                f'Female Employees: {obj.num_female_employees}\n'
                f'Message: {obj.message or "N/A"}\n'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            fail_silently=True,
        )
    except Exception:
        pass
