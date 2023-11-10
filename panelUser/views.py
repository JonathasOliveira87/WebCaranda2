from django.shortcuts import render, redirect
from .models import profileManager
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UpdatePhoneForm, UpdateMoradorForm, UpdateDonoForm, UpdateCasaForm, UpdateCarroForm , UpdateMotoForm, UpdatePetForm, UpdatePhotoForm


@login_required
def panelUser(request):
    items = profileManager.objects.get(user=request.user)
    return render(request, 'panelUser.html', {'itens':items})


@login_required
def update_email(request):
    items = profileManager.objects.get(user=request.user)
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            request.user.email = email
            request.user.save()
            messages.success(request, 'Seu email foi atualizado com sucesso.')
            return render(request, 'panelUser.html', {'itens':items})
        else:
            messages.error(request, 'Não foi possivel atualizar seu email.')
    return render(request, 'panelUser.html', {'itens':items})


@login_required
def update_phone(request):
    items = profileManager.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdatePhoneForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu telefone foi atualizado com sucesso.')
            return redirect('painel')
        else:
            messages.error(request, 'Os dados são válidos, digite apenas números')
    else:
        form = UpdatePhoneForm(instance=items)
    return render(request, 'panelUser.html', {'itens': items, 'form': form})


@login_required
def update_morar(request):
    items = profileManager.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateMoradorForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            messages.success(request, 'Atualizado com sucesso, que bom ter você aqui!')
            return redirect('painel')
        else:
            messages.error(request, 'Opção inválida, apenas "Sim" ou "Não" é permitido!')
    else:
        form = UpdatePhoneForm(instance=items)
    return render(request, 'panelUser.html', {'itens': items, 'form': form})


@login_required
def update_dono(request):
    items = profileManager.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateDonoForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            messages.success(request, 'Atualizado com sucesso!')
            return redirect('painel')
        else:
            messages.error(request, 'Opção inválida, apenas "Sim" ou "Não" é permitido!')
    else:
        form = UpdatePhoneForm(instance=items)
    return render(request, 'panelUser.html', {'itens': items, 'form': form})


@login_required
def update_casa(request):
    items = profileManager.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateCasaForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            messages.success(request, 'Número da casa atualizado com sucesso!')
            return redirect('painel')
        else:
            messages.error(request, 'Os dados são válidos, digite apenas números')
    else:
        form = UpdatePhoneForm(instance=items)
    return render(request, 'panelUser.html', {'itens': items, 'form': form})


@login_required
def update_carro(request):
    items = profileManager.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateCarroForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carro cadastrado com sucesso!')
            return redirect('painel')
        else:
            print(form.errors)  # Adicione esta linha para imprimir erros no console
            messages.error(request, 'Algo deu errado contate o ADM!')
    else:
        form = UpdatePhoneForm(instance=items)
    return render(request, 'panelUser.html', {'itens': items, 'form': form})


@login_required
def update_moto(request):
    items = profileManager.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateMotoForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            messages.success(request, 'Moto cadastrado com sucesso!')
            return redirect('painel')
        else:
            print(form.errors)  # Adicione esta linha para imprimir erros no console
            messages.error(request, 'Algo deu errado contate o ADM!')
    else:
        form = UpdatePhoneForm(instance=items)
    return render(request, 'panelUser.html', {'itens': items, 'form': form})


@login_required
def update_pet(request):
    items = profileManager.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdatePetForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            messages.success(request, 'Atualizado com sucesso!')
            return redirect('painel')
        else:
            print(form.errors)  # Adicione esta linha para imprimir erros no console
            messages.error(request, 'Opção inválida, apenas "Sim" ou "Não" é permitido!')
    else:
        form = UpdatePhoneForm(instance=items)
    return render(request, 'panelUser.html', {'itens': items, 'form': form})



@login_required
def update_photo(request):
    items = profileManager.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdatePhotoForm(request.POST, request.FILES, instance=items)
        if form.is_valid():
            new_photo = request.FILES.get('new_photo')  # Obtém o arquivo enviado pelo campo de entrada de arquivo
            if new_photo:
                items.profile_pic = new_photo  # Atualize a imagem de perfil
                items.save()
                messages.success(request, 'Foto atualizada com sucesso!')
                return redirect('painel')
        else:
            print(form.errors)  # Adicione esta linha para imprimir erros no console
            messages.error(request, 'Falha ao enviar foto!')
    else:
        form = UpdatePhotoForm(instance=items)
    
    return render(request, 'panelUser.html', {'itens': items, 'form': form})





