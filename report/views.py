from django.shortcuts import render
from .models import Reportfile
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required 
def report(request):
    items = Reportfile.objects.all().order_by('-id')
    return render(request, 'report.html', {'itens': items})


@login_required 
def download_file(request, file_id):
    my_file = get_object_or_404(Reportfile, pk=file_id)
    file_path = my_file.file.path
    response = FileResponse(open(file_path, 'rb'))
    return response

