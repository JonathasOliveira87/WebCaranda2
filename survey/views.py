from django.shortcuts import render
from .models import GoogleFormLink
from django.contrib.auth.decorators import login_required


@login_required 
def survey(request):
    try:
        latest_google_form_link = GoogleFormLink.objects.latest('id')
        form_url = str(latest_google_form_link.link)
        votar = bool(form_url)
    except GoogleFormLink.DoesNotExist:
        form_url = ""
        votar = False
    # Você pode passar a variável 'votar' para o modelo para exibir no seu template
    return render(request, 'survey.html', {'votar': votar, 'form_url': form_url})