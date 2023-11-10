from django.shortcuts import render
from .models import SecurityList
from django.contrib.auth.decorators import login_required


@login_required 
def security(request):
    items = SecurityList.objects.all().order_by('-id')
    return render(request, 'security.html', {'itens': items})