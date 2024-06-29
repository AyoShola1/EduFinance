from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import pdfkit  # Assuming you're using pdfkit for PDF generation
import pdfkit
from django.template.loader import render_to_string


def send_invoice_email(student, invoice):
    # Ensure the student has a parent email
    if not student.parent_email:
        return  # or handle this case as needed

    # Generate PDF content
    pdf_content = pdfkit.from_string(render_to_string('invoice_template.html', {'invoice': invoice}), False)

    # Define email subject and message
    subject = f'Invoice for {student.surname} {student.firstname}'
    message = render_to_string('invoice_email_template.html', {'student': student, 'invoice': invoice})
    
    # Create the email
    email = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [student.parent_email]
    )
    
    # Attach the PDF
    email.attach(f'Invoice_{invoice.pk}.pdf', pdf_content, 'application/pdf')

    # Send the email
    email.send()



def generate_invoice_pdf(invoice):
    context = {
        'student': invoice.student,
        'invoice': invoice,
        'items': invoice.invoiceitem_set.all(),
        'total_payable': invoice.total_amount_payable(),
        'total_paid': invoice.total_amount_paid(),
        'balance': invoice.balance(),
    }
    template_path = 'finance/invoice_template.html'
    html = render_to_string(template_path, context)
    pdf = pdfkit.from_string(html, False)
    return pdf
