from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.mail import send_mail
from .forms import ContactForm
from Django_website import settings

# Create your views here.

def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            send_mail(f"{name} send an email", message, email, [settings.DEFAULT_FROM_EMAIL])
            return render(request, "contact.html", {"form":form, "success":True})
    else:
        raise NotImplementedError
    return render(request, "contact.html", {"form":form})