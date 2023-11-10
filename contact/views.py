from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages


def contact(request):
    #buscando todos os contatos
    contacts = Contact.objects.all()

    # Condicional para enviar mensagens para o email do adm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        try:
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                
                # Enviar e-mail para o administrador
                send_mail(
                    f'Nova mensagem de {name}',
                    message,
                    email,
                    ['jrobisondeoliveira@gmail.com'],  # Substitua pelo e-mail do administrador
                    fail_silently=False,
                )
                form.save()  # Salve a mensagem no banco de dados

                return redirect('contato')  # Redirecione para a página de contato
        except Exception as e:
            # Se ocorrer algum erro, mostre uma mensagem de erro
            messages.error(request, f'Erro ao enviar mensage. {e}.')
    else:
        form = ContactForm()



    return render(request, 'contact.html', {'contacts': contacts})
