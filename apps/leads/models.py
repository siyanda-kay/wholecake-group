from django.db import models


class ConsultationRequest(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    num_employees = models.PositiveIntegerField(verbose_name='Number of employees')
    num_female_employees = models.PositiveIntegerField(verbose_name='Number of female employees')
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_contacted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Consultation Request'
        verbose_name_plural = 'Consultation Requests'

    def __str__(self):
        return f"{self.name} — {self.company} ({self.email})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} ({self.email})"
