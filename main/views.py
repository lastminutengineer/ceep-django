from django.shortcuts import render
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
    return render(request, 'contact.html')
# Optional custom 404 page handler
def custom_404(request, exception):
    return render(request, '404.html', status=404)
