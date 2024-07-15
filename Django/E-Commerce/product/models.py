from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to='product_images/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    price_marketing = models.FloatField()
    price_marketing_promocional = models.FloatField(default=0)
    type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variable'),
            ('S', 'Simple'),
        )
    )
    
    @staticmethod
    def resize_image(img, new_with=800):
        print(img.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800 

        if self.image:
            self.resize_image(self.image, max_image_size) 

    def __str__(self):
        return self.name
    
"""
        Variacao:
            nome - char
            produto - FK Produto
            preco - Float
            preco_promocional - Float
            estoque - Int
"""
