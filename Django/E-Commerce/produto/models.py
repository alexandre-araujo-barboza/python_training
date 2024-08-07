from django.db import models
from django.conf import settings
from django.utils.text import slugify
from utils.onfilters import price_format
from PIL import Image
import os
import shortuuid
class Produto(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255, verbose_name='descrição curta')
    descricao_longa = models.TextField(verbose_name='descrição longa')
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField(verbose_name='preço')
    preco_marketing_promocional = models.FloatField(default=0, blank=True, null=True, verbose_name='preço promoção')
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
            ('S', 'Simples'),
        )
    )
    estoque = models.PositiveIntegerField(default=0, blank=True, null=True)

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size
        if original_width <= new_width:
            img_pil.close()
            return
        new_height = round((new_width * original_height) / original_width)
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50,
        )
    
    def format_price_marketing(self):
        return price_format(self.preco_marketing)
    format_price_marketing.short_description = 'Preço'
    
    def format_price_marketing_promotional(self):
        return price_format(self.preco_marketing_promocional)
    format_price_marketing_promotional.short_description = 'Preço promoção'
    
    def save(self, *args, **kwargs):
        if not self.id :
            slug = f'{slugify(self.nome)}-{shortuuid.uuid()}'
        else:
            slug = f'{slugify(self.nome)}-{self.id}'
        self.slug = slug
        super().save(*args, **kwargs)
        max_image_size = 800 
        if self.imagem:
            self.resize_image(self.imagem, max_image_size) 

    def __str__(self):
        return self.nome

class Variacao(models.Model):
    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
    
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField(verbose_name='preço')
    preco_promocional = models.FloatField(default=0, blank=True, null=True, verbose_name='preço promocional')
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome
    
