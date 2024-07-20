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
        widget = forms.PasswordInput(attrs={'value': '      '}),
        label = 'Senha',
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
        validation = {} 
        
        # verifica usuário
        if (str(data['username'])) != str(self.username): 
            user_db = User.objects.filter(username = data['username']).first()       
            if (user_db):
                validation['username'] = "Esse usuário já existe"
        
        # verifica email
        mail_db = User.objects.filter(email = data['email']).first()
        if mail_db and str(mail_db.username) != str(self.username):
            validation['email'] = "Esse e-mail já existe"
        
        # verifica senha
        if data['password'] != '      ' and data['password_confirm'] != '':
            if str(data['password']) != str(data['password_confirm']): 
                validation['password_confirm'] = "Senhas não são idênticas"
            
            if len(data['password']) < 6:
                validation['password'] = "Tamanho mínimo da senha são 6 caracteres"
        
        # novo usuário
        if not self.username:
            if data['password'] == '      ':
                validation['password'] = 'Senha é obrigatória'
            if data['email'] == '':
                validation['email'] = 'E-mail é obrigatório'
        
        # mostra erros
        if validation:
            raise(forms.ValidationError(validation))
