from django.conf import settings


def site_settings(request):
    return {
        'GA_ID': getattr(settings, 'GOOGLE_ANALYTICS_ID', ''),
        'SITE_NAME': 'WHOLECAKE GROUP',
        'SITE_EMAIL': getattr(settings, 'CONTACT_EMAIL', 'info@wholecakegroup.co.za'),
        'SITE_PHONE': getattr(settings, 'CONTACT_PHONE', ''),
    }
