from django.core.mail import send_mail
from django.conf import settings
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adoptly.settings')
django.setup()

try:
    send_mail(
        subject='Test Email from Adoptly',
        message='This is a test email to verify your Mailjet configuration.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['daniela.danila2003@gmail.com'],  # Replace with your email
        fail_silently=False,
    )
    print("Test email sent successfully!")
except Exception as e:
    print(f"Error sending email: {str(e)}")
