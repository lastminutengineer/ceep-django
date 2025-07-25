from django.shortcuts import render
from .models import ContactMessage  # Import the model

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')

def project(request):
    return render(request, 'project.html')

def feature(request):
    return render(request, 'feature.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the form data into the database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        # You can pass a success flag to show a confirmation message in the template
        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')

# Optional custom 404 page handler
def custom_404(request, exception):
    return render(request, '404.html', status=404)
