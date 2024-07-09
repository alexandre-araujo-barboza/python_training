from django.shortcuts import render
from django.contrib import messages
from contact.forms import RegisterForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado com êxito')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )
