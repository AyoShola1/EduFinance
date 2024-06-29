from django.contrib import admin
from .models import Invoice, InvoiceItem, Receipt

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('student', 'session', 'term', 'class_for', 'balance_from_previous_term', 'status')
    search_fields = ('student__surname', 'student__firstname', 'session__name', 'term__name', 'class_for__name')
    list_filter = ('status', 'session', 'term', 'class_for')
    ordering = ('student', 'term')

@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'description', 'amount')
    search_fields = ('invoice__student__surname', 'invoice__student__firstname', 'description')
    ordering = ('invoice',)

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'amount_paid', 'date_paid', 'comment')
    search_fields = ('invoice__student__surname', 'invoice__student__firstname', 'comment')
    ordering = ('-date_paid',)
