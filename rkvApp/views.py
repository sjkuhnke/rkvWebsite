import requests
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def documentary(request):
    return render(request, 'documentary.html')


def show(request):
    return render(request, 'show.html')


def projects(request):
    return render(request, 'projects.html')


def contact(request):
    recaptcha_site_key = settings.GOOGLE_RECAPTCHA_SITE_KEY

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recaptcha_response = request.POST.get('g-recaptcha-response')

        if not name or not email or not subject or not message:
            return render(request, 'contact.html', {
                'error': 'All fields are required.',
                'recaptcha_site_key': recaptcha_site_key
            })

        recaptcha_verify_url = 'https://www.google.com/recaptcha/api/siteverify'
        recaptcha_data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        recaptcha_result = requests.post(recaptcha_verify_url, data=recaptcha_data)
        recaptcha_result_json = recaptcha_result.json()

        if not recaptcha_result_json['success']:
            return render(request, 'contact.html', {
                'error': 'reCAPTCHA validation failed. Please try again.',
                'recaptcha_site_key': recaptcha_site_key
            })

        email_subject = 'New Contact Submission: ' + subject
        email_body = render_to_string('contact_email.txt', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        })

        email_message1 = EmailMessage(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            ['info@rkvideos-co.com']
        )

        email_message2 = EmailMessage(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            ['shaejk29@gmail.com']
        )

        try:
            email_message1.send()
            email_message2.send()
            return render(request, 'contact.html', {
                'success': 'Thank you for your message. We will get back to you shortly.',
                'recaptcha_site_key': recaptcha_site_key
            })
        except Exception as e:
            return render(request, 'contact.html', {
                'error': f'An error occurred: {str(e)}',
                'recaptcha_site_key': recaptcha_site_key
            })

    return render(request, 'contact.html', {
        'recaptcha_site_key': recaptcha_site_key
    })


def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)
