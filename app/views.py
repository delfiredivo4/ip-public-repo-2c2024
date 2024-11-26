# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .layers.services.services import getAllImages

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
def home(request):
    images = getAllImages()
    favourite_list = []

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })

#<!-- BUSCADOR, para el buscador tenemos la funcion search, la cual pide el resultado del label y el input del boton y el resultador lo transforma al nombre "query"
# luego "transforma" lo que ponemos en el label a "search_msg" y si search_msg no esta vacio entonces busca todas las imagenes que tengan como coincidencia 
#lo que pusimos en el label del home para asi crear la variable de imagenes_filtradas, luego pedimos al home.html que devuelva todas las imagenes con sus datos: nombre, estado, vivo,muerto, etc
#que coincidan con la variable imagenes filtradas. (que es lo que buscamos con el label y el boton) -->
def search(request):
    search_msg = request.POST.get('query', '')
    # si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py,
    # y luego renderiza el template (similar a home).
    if (search_msg != ''):
        
        imagenesfiltradas = getAllImages(search_msg)

        return render(request, 'home.html', {
            'images':  imagenesfiltradas,
            'search_msg': search_msg
        })
    else:
        return redirect('home')


# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    #agregamos logout para salir del modo admin 
    logout(request)
    return render(request, 'index.html')
