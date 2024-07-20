from django.contrib.auth.models import User
from django import forms
from . import models

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        field = '__all__'
        exclude = ('usuario',)

class UserForm(forms.ModelForm):
    password = forms.CharField(
        required = False,
        widget = forms.PasswordInput(),
        label = 'Senha',
        initial = 0,
    )
    password_confirm = forms.CharField(
        required = False,
        widget = forms.PasswordInput(),
        label = 'Repetir senha',
    )
    def __init__(self, username = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = username
        
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password',
            'password_confirm',
            'email',
        )
        
    def clean(self, *args, **kwargs):
        data = self.data
        messages = []
        if (data['username']) != self.username: # usuário mudou  
           user_db = User.objects.filter(username=self.username).first()       
           if (user_db):
               messages.append("Esse usuário já existe") 
        mail_db = User.objects.filter(email=data['email']).first()
        if mail_db and mail_db.username != self.username: # email existe
            messages.append("Esse e-mail já existe") 
        