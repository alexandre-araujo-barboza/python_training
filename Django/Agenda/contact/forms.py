from django import forms
from django.core.exceptions import ValidationError
from . import models
       
    
class ContactForm(forms.ModelForm):
    
    def repeat_chars(self, string: str):
        if len(string) > 2:
            for i in range(len(string)):
                if (i >= 2):
                    if  string[i] == string[i - 1] and string[i - 1] == string[i - 2] :
                        return True
        return False

    def has_special_chars(self, string: str) :
        for char in string:
            if not char.isalpha() and not char.isdigit() and not char.isspace():
               if char != ".":
                  return True
        return False         

    def has_numbers(self, string: str):
        for char in string:
            if char.isdigit() :
                return True
        return False
     
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'smallest',
                'placeholder': 'digite seu nome',
            }
        ),
        label='Nome',
        help_text='Apenas letras (com acentuação)',
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'smallest',
                'placeholder': 'digite seu sobrenome',
            }
        ),
        label='Sobrenome',
        help_text='Letras (com acentuação) e espaços',
    )
    last_name.required = False

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'smallest',
                'placeholder': 'digte seu telefone',
            }
        ),
        label='Telefone',
        help_text='ex: +55(21)99506-8649',
    )
    
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'smallest',
                'placeholder': 'digte seu e-mail',
            }
        ),
        label='E-mail',
        help_text='digite um formato válido de e-mail',
    )
    email.required = False
    
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'smallest',
                'placeholder': 'entre com uma descrição',
            }
        ),
        label='Descrição',
        help_text='entre com informações adicionais (opcional)',
    )
    description.required = False

    '''
    category = forms.ChoiceField(
        label='Categoria',
        help_text='categoria do contato (opcional)',
    )
    '''
    
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        label='Imagem',
    )
    picture.required = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            'picture',
        )
        
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo.',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        
        return super().clean()
         
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if len(first_name) < 3:
            self.add_error(
                'first_name',
                ValidationError(
                    'O nome é muito curto.',
                    code='invalid'
                )
            )

        if first_name == str.upper(first_name) and str.isalpha(first_name):
            self.add_error(
                'first_name',
                ValidationError(
                    'Não use todos os caracteres com maiúsculas no nome.',
                    code='invalid'
                )
            )

        if self.repeat_chars(first_name):
            self.add_error(
                'first_name',
                ValidationError(
                    'Não use caracteres repetidos no nome.',
                    code='invalid'
                )
            )
        
        if self.has_special_chars(first_name) :
            self.add_error(
                'first_name',
                ValidationError(
                    'Não use caracteres especiais no nome.',
                    code='invalid'
                )
            )
        
        if self.has_numbers(first_name) :
            self.add_error(
                'first_name',
                ValidationError(
                    'Não use números no nome.',
                    code='invalid'
                )
            )

        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
         
        if len(last_name) < 3 and len(last_name) > 0:
            self.add_error(
                'last_name',
                ValidationError(
                    'O sobrenome é muito curto.',
                    code='invalid'
                )
            )
         
        if last_name == str.upper(last_name) and str.isalpha(last_name):
            self.add_error(
                'last_name',
                ValidationError(
                    'Não use todos os caracteres com maiúsculas no sobrenome.',
                    code='invalid'
                )
            )
        
        if self.repeat_chars(last_name):
            self.add_error(
                'last_name',
                ValidationError(
                    'Não use caracteres repetidos no sobrenome.',
                    code='invalid'
                )
            )
        
        if self.has_special_chars(last_name) :
            self.add_error(
                'last_name',
                ValidationError(
                    'Não use caracteres especiais no sobrenome.',
                    code='invalid'
                )
            )
        
        if self.has_numbers(last_name) :
            self.add_error(
                'last_name',
                ValidationError(
                    'Não use números no sobrenome.',
                    code='invalid'
                )
            )
    
        return last_name
