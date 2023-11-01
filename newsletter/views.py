from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import NewsletterSignup
from .forms import NewsletterForm


def newsletter(request):
    """
    Newsletter mailing list
    """
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            member = form.save()
            messages.info(request, 'You have successfully joined GamerOnBoard \
                          mailing list!')

            user_email = get_object_or_404(NewsletterSignup,
                                           email=member.email)
            subject = render_to_string(
                'newsletter/newsletter_subject.txt')
            body = render_to_string(
                'newsletter/newsletter_body.txt',
                {'contact_email': settings.DEFAULT_FROM_EMAIL})

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [user_email]
            )

            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request, 'Sorry, there was a glitch! \
                           Please ensure the form is valid or you \
                           are not already signed up!')

    context = {
            'newsletter_form': form,
        }

    return redirect(request.META.get('HTTP_REFERER', '/'))
