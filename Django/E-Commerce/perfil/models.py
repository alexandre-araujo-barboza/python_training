from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from utils.validacpf import valida_cpf
import re
class Perfil(models.Model):
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
        
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='usuário')
    idade   = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, help_text='somente números')
    endereco = models.CharField(max_length=50, verbose_name='endereço')
    numero   = models.CharField(max_length=5, verbose_name='número')
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cep    = models.CharField(max_length=8)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=2,
        default='SP',
        choices = (
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )
    
    def __str__(self):
        return f'{self.usuario}'             
   
    def clean(self):
        error_messages = {}
        cpf_send = self.cpf or None
        cpf_safe = None
        perfil   = Perfil.objects.filter(cpf = cpf_send).first()
        if (perfil):
            cpf_safe = perfil.cpf
            if cpf_safe is not None and self.pk != perfil.pk:
                error_messages['cpf'] = 'CPF já existe'

        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido'
        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8: 
            error_messages['cep'] = 'CEP inválido, digite os 8 números'
        if error_messages:
            raise ValidationError(error_messages)        
 