
from django.forms import inlineformset_factory, modelformset_factory
from django import forms
from django_select2.forms import Select2Widget
from .models import Invoice, InvoiceItem, Receipt


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['student', 'session', 'term']
        widgets = {
            'student': Select2Widget,
        }

InvoiceItemFormset = inlineformset_factory(
    Invoice, InvoiceItem, fields=["description", "amount"], extra=1, can_delete=True
)

InvoiceReceiptFormSet = inlineformset_factory(
    Invoice,
    Receipt,
    fields=("amount_paid", "date_paid", "comment"),
    extra=0,
    can_delete=True,
)

Invoices = modelformset_factory(Invoice, exclude=(), extra=4)


