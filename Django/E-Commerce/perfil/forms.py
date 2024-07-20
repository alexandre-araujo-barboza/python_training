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
    )
    password_confirm = forms.CharField(
        required = False,
        widget = forms.PasswordInput(),
        label = 'Repetir senha',
    )
    def __init__(
            self,
            username = None,
            password = None,
            email    = None,
            *args,
            **kwargs):
        super().__init__(*args, **kwargs)
        self.username = username
        self.password = password
        self.email    = email
    
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
        
        
        """
        if (data['username']) != self.usuario: # username changed  
            print(self.usuario)
        
        if (data['password']) != self.password: # password changed  
            print(self.password)
        
        if (data['email']) != self.email: # email changed  
            print(self.email)
        """

        #print(data.username)
        #print(cleaned.username)
        
        """
        validation_error_messages = {}
        user_data  = cleaned.data['username']
        email_data = cleaned.data['email']
        pass_data  = cleaned.data['pasword']
        pass2_data = cleaned.data['pasword_confirm']
        usuario_db = User.objects.filter(usuario=user_data).first()
        enail_db = User.objects.filter(email=email_data).first()
        
        error_msg_user_exists = 'Usuário já existe'
        error_msg_email_exists = 'E-mail já existe'
        error_msg_pass_not_match = 'Senhas não correspondem'
        error_msg_pass_is_short = 'Senha mínima é de (6) caracteres'

        # Usuário Logado - Atualizar
        if self.usuario:
            pass

        # Usuário não logado - Cadastrar
        else:
            pass

        if validation_error_messages:
            raise(forms.ValidationError(validation_error_messages))
        """
        