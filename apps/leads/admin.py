from django.contrib import admin
from .models import ConsultationRequest, ContactMessage


@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'phone', 'num_employees', 'num_female_employees', 'created_at', 'is_contacted')
    list_filter = ('is_contacted', 'created_at')
    search_fields = ('name', 'company', 'email')
    ordering = ('-created_at',)
    list_editable = ('is_contacted',)
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Contact Details', {'fields': ('name', 'company', 'email', 'phone')}),
        ('Programme Details', {'fields': ('num_employees', 'num_female_employees', 'message')}),
        ('Status', {'fields': ('is_contacted', 'created_at')}),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)
    list_editable = ('is_read',)
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
