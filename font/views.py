from django.shortcuts import render

# Create your views here.
def visit(request):
    return render(request, 'font/visit.html', {})