from django.shortcuts import render

# Create your views here.

def contactUs(request):
    template_name = 'contact_us/contact.html'
    return render(request, template_name)