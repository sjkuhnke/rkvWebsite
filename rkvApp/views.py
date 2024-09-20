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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not name or not email or not subject or not message:
            return render(request, 'contact.html', {'error': 'All fields are required.'})

        email_subject = 'New Contact Submission: ' + subject
        email_body = render_to_string('contact_email.txt', {
            'name': name,
            'email': email,
            'message': message,
        })

        email_message = EmailMessage(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            ['info@rkvideos-co.com']
        )

        email_message = EmailMessage(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            ['shaejk29@gmail.com']
        )

        try:
            email_message.send()
            return render(request, 'contact.html',
                          {'success': 'Thank you for your message. We will get back to you shortly.'})
        except Exception as e:
            return render(request, 'contact.html', {'error': f'An error occurred: {str(e)}'})

    return render(request, 'contact.html')


def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)
