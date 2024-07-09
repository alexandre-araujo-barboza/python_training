from django import forms
from django.core.exceptions import ValidationError
from . import models

def repeat_chars(string: str):
    if len(string) > 2:
        for i in range(len(string)):
            if (i >= 2):
                string[i] == string[i - 1] and \
                string[i] == string[i - 2]
                return True
    return False

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'smallest',
                'placeholder': 'digite seu nome',
            }
        ),
        label='Nome',
        help_text='Apenas letras (com acentuação).',
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'smallest',
                'placeholder': 'digite seu sobrenome',
            }
        ),
        label='Sobrenome',
        help_text='Letras (com acentuação) e espaços.',
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'smallest',
                'placeholder': 'digte seu telefone.',
            }
        ),
        label='Telefone',
        help_text='ex: +55(21)99506-8649',
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Aqui veio do init',
        # })

    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }
        
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

        if first_name == str.upper(first_name):
            self.add_error(
                'first_name',
                ValidationError(
                    'Não use todos os caracteres com maiúsculas no nome.',
                    code='invalid'
                )
            )

        if (repeat_chars(first_name)):
            self.add_error(
                'first_name',
                ValidationError(
                    'Não use caracteres repetidos no nome.',
                    code='invalid'
                )
            )

        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
         
        if len(last_name) < 3:
            self.add_error(
                'last_name',
                ValidationError(
                    'O sobrenome é muito curto.',
                    code='invalid'
                )
            )
         
        if last_name == str.upper(last_name):
            self.add_error(
                'last_name',
                ValidationError(
                    'Não use todos os caracteres com maiúsculas no sobrenome.',
                    code='invalid'
                )
            )
        
        if (repeat_chars(last_name)):
            self.add_error(
                'last_name',
                ValidationError(
                    'Não use caracteres repetidos no sobrenome.',
                    code='invalid'
                )
            )
            
        return last_name
