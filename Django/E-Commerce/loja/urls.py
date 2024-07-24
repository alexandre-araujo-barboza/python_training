from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/', include('perfil.urls')),
    path('pedido/', include('pedido.urls')),
    path('', include('produto.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Remover no Deploy
# if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns = [
#        path('__debug__/', include(debug_toolbar.urls)),
#    ] + urlpatterns
