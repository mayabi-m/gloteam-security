from django.shortcuts import render, redirect
from .models import NewsletterSubscriber
from .forms import NewsletterForm, ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request, 'main/about.html')
def service(request):
    return render(request, 'main/service.html')
def guard(request):
    return render(request, 'main/guard.html')
def blog(request):
    return render(request, 'main/blog.html')
def single(request):
    return render(request, 'main/single.html')
def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Prevent duplicate entries manually (optional if using unique=True)
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                form.save()
                messages.success(request, "Subscribed successfully!")
            else:
                messages.warning(request, "You are already subscribed.")
        else:
            messages.error(request, "Invalid email address.")
    return redirect(request.META.get('HTTP_REFERER', '/'))  # stay on the same page


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"From: {name} <{email}>\n\n{message}"

        try:
            send_mail(
                subject=subject,
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            messages.success(request, "Message sent successfully!")
        except Exception as e:
            messages.error(request, f"Error sending message: {e}")

        return redirect('main:contact')  # or wherever you want to go

    return render(request, 'main/contact.html')


