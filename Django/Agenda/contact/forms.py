from django import forms
from django.core.exceptions import ValidationError
from . import models

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
        # cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )

        return super().clean()
