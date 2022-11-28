from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,  UserCreationForm
from django.contrib.auth.forms import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserEditForm
from django.contrib.auth.decorators import login_required
from federations.models import Federation

def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    )

def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(name__contains=search_param)
        query.add(Q(official_website__contains=search_param), Q.OR)
        federations = Federation.objects.filter(query)
        context_dict.update(
            {
                "federations": federations,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )
    
def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('contraseña')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "final_project/home.html", {"mensaje":f"Bienvenido {usuario}"} )
            else:

                return render(request, "final_project/home.html", {"mensaje":"Datos incorrectos, vuelva a ingresa su usuario."} )
    
    else:

                return render(request, "final_project/home.html", {"mensaje":"Error, formulario incorrecto"} )

    form = AuthenticationForm()

    return render(request, "final_project/login.html", {'form', form})
 
def register(request):
    
    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data*['username']
            form.save()
            return render(request, "final_project/home.html", {"mensaje":"Usuario creado correctamente"} )    

    else: 

        form = UserCreationForm()

    return render(request, "final_project/login.html", {'form', form})    



def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "final_project/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "final_project/edit_profile.html", {"miFormulario": miFormulario, "usuario": usuario})
