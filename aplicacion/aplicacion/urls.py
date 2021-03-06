"""aplicacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Añadido para que funcione el path desarrollo
from django.conf.urls import include, url
from django.contrib import admin

#cosas para la imagen (ImageField)
from django.conf import settings
from django.conf.urls.static import static # para + static de visualizar MEDIA_URL
from django.views.static import serve
#------
from desarrollo import views #en el segundo url comentado, me hace falta este import(sepa que views estamos utilizando)
# from django.conf.urls import handler404

urlpatterns = [
    url(r'^$', views.iniciar, name='iniciar'), # UNA forma de hacer lo mismo que las dos lineas anteriores (SI SOLO PONGO url: http://localhost:8080) se va login.html
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  #p6
    path('desarrollo/', include('desarrollo.urls')), #quito el / pk se lo añado en desarollo/urls.py
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # esta linea es para que pueda poner la ruta completa de las imagenes en el navegador :http://127.0.0.1:8000/media/usuarios/name_image.jpg

#cosas para la imagen (ImageField)
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',serve, {
            'document_root' : settings.MEDIA_ROOT,
        }),
    ]
# OTRA MANERA DE HACER LO MISMO QUE ARRIBA
# if settings.DEBUG: 
#         urlpatterns += static(settings.MEDIA_URL, 
#                               document_root=settings.MEDIA_ROOT) 



# handler404 = 'desarrollo.views.handler404'



