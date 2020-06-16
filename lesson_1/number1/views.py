from django.shortcuts import render

from number1.models import User


def number1_page(request):
    return render(request, 'index.html', {'users': User.objects.all()})
