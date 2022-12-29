from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import *
from djappsebm.utils import render_to_pdf
from django.core.files.storage import FileSystemStorage
from urllib import request

from djappsebm.forms import addClientesForm, addCategoriaForm, addUsuariosForm, addLibrosForm, addAutorForm, FormPedidoCliente, FormLibroPorAutor
from djappsebm.models import TblClientes, TblCategorias, TblLibros, TblAutores,TblUsuarios,TblPedidoCliente, TblLibroPorAutor, AuthUser
from django.contrib import auth
from django.urls import reverse_lazy

from djappsebm.views import *

# Create your views here.

def index(request):
    
        return render(request, 'djappsebm/index.html')

def error(request):
    return render(request, "djappsebm/error.html")

def inicio_sesion_sebm(request):
    if request.POST:
        usuario = request.POST['usuario']
        clave = request.POST['password']

        try:
            #authUser = AuthUser.objects.get(username=usuario, password=clave)
            user = auth.authenticate(username = usuario, password = clave)
            auth.login(request, user)
            #return HttpResponse("Ingreso al inicio de sesion con el usuario: " + usuario )

        except (AuthUser.DoesNotExist, AttributeError):
            return HttpResponse("Error al intentar ingresar a la pagina")

        return redirect('inicio_sebm')

    else:
        return HttpResponse("Usted esta intentando ingresar incorrectamente")


def cerrar_sesion_sebm(request):
    auth.logout(request)
    return redirect('index')

def inicio_sebm(request):
    return render(request,'djappsebm/inicio.html')

def inicio_sebm2(request):
    return render(request,'djappsebm/ini.html')

def addLibro_sbm(request):
    return render(request, 'djappsebm/addLibro.html')

##CLIENTES##

    #agregar clientes

class Cliente_Create_sebm(CreateView):

    model = TblClientes
    form_class = addClientesForm
    template_name = 'djappsebm/clientes/addCliente.html'
    success_url = reverse_lazy('listar_clientes_sebm')
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Cliente_Create_sebm,self).dispatch(request,*args, **kwargs)

# def addCliente_sbm(request):
#     if  request.user.is_authenticated:
#         if request.method == 'POST':
#             form = addClientesForm(request.POST)
#             if form.is_valid():
#                 form.save()
#             return redirect('listar_clientes_sebm')
#         else:
#             form = addClientesForm()
#         return render(request,'djappsebm/clientes/addCliente.html', {'form': form})
#     else:
#         return render(request, 'djappsebm/error.html')

    #Listar clientes

class Cliente_list_sebm(ListView):

    model = TblClientes
    template_name = 'djappsebm/clientes/listar_cliente.html'

    def get_queryset(self):
        return TblClientes.objects.filter(estado='ACTIVO')
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Cliente_list_sebm,self).dispatch(request,*args, **kwargs)

# def listar_clientes_sebm(request):
#     if  request.user.is_authenticated:
#         clientes=TblClientes.objects.filter(estado='ACTIVO')
#         contexto ={'clientes':clientes}
#         return render(request, 'djappsebm/clientes/listar_cliente.html', contexto)
#     else:
#         return render(request, 'djappsebm/error.html')


    #eliminar cliente

class Eliminar_cliente_sebm(View):
    def get(self, request, id_cli):
        autor = TblClientes.objects.get(id_cliente=id_cli)
        autor.estado= 'INACTIVO'
        autor.save()
        return redirect('listar_clientes_sebm')
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Eliminar_cliente_sebm,self).dispatch(request,*args, **kwargs)

        #editar cliente

class Cliente_update_sebm(UpdateView):
    model = TblClientes
    form_class = addClientesForm
    template_name = 'djappsebm/clientes/addCliente.html'
    success_url=reverse_lazy('listar_clientes_sebm')
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Cliente_update_sebm,self).dispatch(request,*args, **kwargs)

# def editClient_sebm(request, id_cli):
#     if  request.user.is_authenticated:
#         clientes= TblClientes.objects.get(pk=id_cli)
#         if request.method=='GET':
#             form =addClientesForm(instance=clientes)
#         else:
#             form=addClientesForm(request.POST, instance=clientes)
#             if form.is_valid():
#                 form.save()
#             return redirect('listar_clientes_sebm')
#         return render(request, 'djappsebm/clientes/addCliente.html', {'form': form})
#     else:
#         return render(request, 'djappsebm/error.html')
    
##CATEGORIAS##
    
        #agregar categoria
class Categoria_Create_sebm(CreateView):

    model = TblCategorias
    form_class = addCategoriaForm
    template_name = 'djappsebm/categoria/add_categoria.html'
    success_url = reverse_lazy('listar_categoria_sebm')
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Categoria_Create_sebm,self).dispatch(request,*args, **kwargs)

    #Listar categoria

class Listar_categoria_sebm(ListView):
    model = TblCategorias
    template_name = 'djappsebm/categoria/listar_categoria.html'
    def get_queryset(self):
        return TblCategorias.objects.filter(estado='ACTIVO')
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Listar_categoria_sebm,self).dispatch(request,*args, **kwargs)


    #eliminar categoria

class Categoria_eliminar_sebm(View):
    def get(self, request, id_cat):
        categoria = TblCategorias.objects.get(id_categoria=id_cat)
        categoria.estado= 'INACTIVO'
        categoria.save()
        return redirect('listar_categoria_sebm')
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Categoria_eliminar_sebm,self).dispatch(request,*args, **kwargs)
    
    #editar categoria
class Categoria_update_sebm(UpdateView):
    model = TblCategorias
    form_class = addCategoriaForm
    template_name = 'djappsebm/categoria/add_categoria.html'
    success_url=reverse_lazy('listar_categoria_sebm')
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Categoria_update_sebm,self).dispatch(request,*args, **kwargs)
    ##LIBROS##
    
        #agregar ibro
class Libro_Create_sebm(CreateView):

    model = TblLibros
    form_class = addLibrosForm
    template_name ='djappsebm/libros/addLibro.html'
    try: 
        portada=request.FILES['foto_perfil']  # type: ignore
        ruta_foto = f"media/{portada.name}"
        fs=FileSystemStorage()
        file_name = fs.save(portada.name, portada)
    except:
            ruta_foto ="media/sin_portada.png"

    success_url=reverse_lazy('listar_libros_sebm')
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Libro_Create_sebm,self).dispatch(request,*args, **kwargs)

# def addLibro_sbm(request):
#     if  request.user.is_authenticated:
#         if request.method == 'POST':
#             form = addLibrosForm(request.POST)
#             if form.is_valid():
#                 form.save()
#             return redirect('listar_libros_sebm')
#         else:
#             form = addLibrosForm()
#         return render(request,'djappsebm/libros/addLibro.html', {'form': form})
#     else:
#         return render(request, 'djappsebm/error.html')

    #Listar libros

class Listar_libro_sebm(ListView):
    model = TblLibros
    template_name = 'djappsebm/libros/listar_libros.html'
    def get_queryset(self):
        return TblLibros.objects.filter(estado='ACTIVO')
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Listar_libro_sebm,self).dispatch(request,*args, **kwargs)
# def listar_libros_sebm(request):
#     if  request.user.is_authenticated:
#         libros=TblLibros.objects.filter(estado='ACTIVO')
#         contexto ={'libros':libros}
#         return render(request, 'djappsebm/libros/listar_libros.html', contexto)
#     else:
#         return render(request, 'djappsebm/error.html')


    #eliminar libro

class Eliminar_libro_sebm(View):
    def get(self, request, id_lib):
        autor = TblLibros.objects.get(isbn=id_lib)
        autor.estado= 'INACTIVO'
        autor.save()
        return redirect('listar_libros_sebm')
    
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')
        #editar libro

class Libro_update_sebm(UpdateView):
    model = TblLibros
    form_class = addLibrosForm
    template_name = 'djappsebm/libros/addLibro.html'
    success_url=reverse_lazy('listar_libros_sebm')
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Libro_update_sebm,self).dispatch(request,*args, **kwargs)
# def editLibro_sebm(request, id_cli):
#     if  request.user.is_authenticated:
#         clientes= TblClientes.objects.get(pk=id_cli)
#         if request.method=='GET':
#             form =addClientesForm(instance=clientes)
#         else:
#             form=addClientesForm(request.POST, instance=clientes)
#             if form.is_valid():
#                 form.save()
#             return redirect('listar_clientes_sebm')
#         return render(request, 'djappsebm/clientes/addCliente.html', {'form': form})
#     else:
#         return render(request, 'djappsebm/error.html')
    
    ##USUARIOS##

    #agregar usuarios

class Usuario_Create_sebm(CreateView):

    model = TblUsuarios
    form_class = addUsuariosForm
    template_name = 'djappsebm/usuarios/add_usuarios.html'
    success_url = reverse_lazy('listar_usuarios_sebm')
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Usuario_Create_sebm,self).dispatch(request,*args, **kwargs)
# def addUsuario_sbm(request):
#     if  request.user.is_authenticated:
#         if request.method == 'POST':
#             form = addUsuariosForm(request.POST)
#             if form.is_valid():
#                 form.save()
#             return redirect('addUsuario_sbm')
#         else:
#             form = addUsuariosForm()
#         return render(request,'djappsebm/usuarios/add_usuarios.html', {'form': form})
#     else:
#             return render(request, 'djappsebm/error.html')

    #Listar usuarios

class Listar_usuario_sebm(ListView):
    model = TblUsuarios
    template_name = 'djappsebm/usuarios/listar_usuarios.html'
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Listar_usuario_sebm,self).dispatch(request,*args, **kwargs)
# def listar_usuarios_sebm(request):
#     if  request.user.is_authenticated:
#         clientes=TblClientes.objects.filter(estado='ACTIVO')
#         contexto ={'clientes':clientes}
#         return render(request, 'djappsebm/clientes/listar_cliente.html', contexto)
#     else:
#         return render(request, 'djappsebm/error.html')


    #eliminar usuarios

class Usuario_delete_sebm(View):
    def get(self, request, id_u):
        usuario = TblUsuarios.objects.get(pk=id_u)
        usuario.delete()
        return redirect('listar_usuarios_sebm')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Usuario_delete_sebm,self).dispatch(request,*args, **kwargs)
        #editar usuarios

class Usuario_update_sebm(UpdateView):
    model = TblUsuarios
    form_class = addUsuariosForm
    template_name = 'djappsebm/usuarios/add_usuarios.html'
    success_url=reverse_lazy('listar_usuarios_sebm')
def dispatch(self, request, *args, **kwargs) :
    if self.request.user.is_anonymous:
        return redirect('error')

    return super(Usuario_update_sebm,self).dispatch(request,*args, **kwargs)
# def editUsuario_sebm(request, id_cli):
#     if  request.user.is_authenticated:
#         clientes= TblClientes.objects.get(pk=id_cli)
#         if request.method=='GET':
#             form =addClientesForm(instance=clientes)
#         else:
#             form=addClientesForm(request.POST, instance=clientes)
#             if form.is_valid():
#                 form.save()
#             return redirect('listar_clientes_sebm')
#         return render(request, 'djappsebm/clientes/addCliente.html', {'form': form})
#     else:
#         return render(request, 'djappsebm/error.html')


#AUTOR

#Insertar Autor

class Insertar_autor_sebm(CreateView):
    model = TblAutores
    form_class = addAutorForm
    template_name = 'djappsebm/autores/add_autor.html'
    success_url = reverse_lazy('Listar_autor_sebm')
    
    
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Insertar_autor_sebm,self).dispatch(request,*args, **kwargs)


#Listar autor


class Listar_autor_sebm(ListView):
    model = TblAutores
    template_name = 'djappsebm/autores/listar_autor.html'
    def get_queryset(self):
        return TblAutores.objects.filter(estado = 'ACTIVO')
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Listar_autor_sebm,self).dispatch(request,*args, **kwargs)
    


#Editar Autor

class Editar_autor_sebm(UpdateView):
    model= TblAutores
    form_class=addAutorForm
    template_name ='djappaacc/Autores/autores.html'
    success_url=reverse_lazy('listar_autor')
    
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Editar_autor_sebm,self).dispatch(request,*args, **kwargs)


#eliminar

class Eliminar_autor_sebm(View):
    def get(self, request, id_aut):
        autor = TblAutores.objects.get(id_autor=id_aut)
        autor.estado= 'INACTIVO'
        autor.save()
        return redirect('Listar_autor_sebm')
    
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Eliminar_autor_sebm,self).dispatch(request,*args, **kwargs)

class Reporte_autor_sebm(View):
    def get(self, request, *args, **kwargs):
        object_list = TblAutores.objects.all()
        data = {
            'object_list': object_list
        }
        pdf = render_to_pdf('djappsebm/autores/listar_autor.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Reporte_autor_sebm,self).dispatch(request,*args, **kwargs)


#Insertar Pedido cliente

class insertar_Pedido_cliente_sebm(CreateView):
    model = TblPedidoCliente
    form_class = FormPedidoCliente
    template_name = 'djappsebm/pedido_cliente/addPedidoCliente.html'
    success_url = reverse_lazy('listar_PedidoCliente')
    
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(insertar_Pedido_cliente_sebm,self).dispatch(request,*args, **kwargs)




#Listar Pedidos clientes


class listar_Pedido_cliente_sebm(ListView):
    model = TblPedidoCliente
    template_name = 'djappsebm/pedido_cliente/listar_pedidoClientes.html'
    def get_queryset(self):
        return TblPedidoCliente.objects.filter(estado = 'ACTIVO')
    
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(listar_Pedido_cliente_sebm,self).dispatch(request,*args, **kwargs)




#Editar Pedidos clientes

class editar_Pedido_cliente_sebm(UpdateView):
    model= TblPedidoCliente
    form_class=FormPedidoCliente
    template_name ='djappsebm/pedido_cliente/pedidoCliente.html'
    success_url=reverse_lazy('listar_PedidoCliente')
    
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(editar_Pedido_cliente_sebm,self).dispatch(request,*args, **kwargs)



#eliminar Pedidos clientes

class eliminar_Pedido_cliente_sebm(View):
    def get(self, request, id_ped_sebm):
        pedido = TblPedidoCliente.objects.get(id_pedido=id_ped_sebm)
        pedido.estado= 'INACTIVO'
        pedido.save()
        return redirect('listar_PedidoCliente')
    
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(eliminar_Pedido_cliente_sebm,self).dispatch(request,*args, **kwargs)
    
    
class reporte_pedido_cliente_sebm(View):
    def get(self, request, *args, **kwargs):
        object_list = TblPedidoCliente.objects.all()
        data = {
            'object_list': object_list
        }
        pdf = render_to_pdf('djappsebm/pedido_cliente/listar_pedidoClientes.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(reporte_pedido_cliente_sebm,self).dispatch(request,*args, **kwargs)

#insertar Libros por autor

class Libros_Autor_Create_sebm(CreateView): 
    model = TblLibroPorAutor
    form_class=FormLibroPorAutor
    template_name ='djappsebm/libro_autor/insertar_libro_autor.html'
    success_url=reverse_lazy('libroAutor_listar')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Libros_Autor_Create_sebm,self).dispatch(request,*args, **kwargs)



#Listar Libros por autor

class Libros_Autor_list_sebm(ListView):
    
    model = TblLibroPorAutor
    template_name = 'djappsebm/libro_autor/listar_pedido_cliente.html'

    def get_queryset(self):
        return TblLibroPorAutor.objects.filter(estado='ACTIVO')
    
    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
            return redirect('error')

        return super(Libros_Autor_list_sebm,self).dispatch(request,*args, **kwargs)
    


#Editar Libros por autor


class Libros_Autor_update_sebm(UpdateView):
    model= TblLibroPorAutor
    form_class=FormLibroPorAutor
    template_name ='djapphapp/libros_autor/libroAutor.html'
    success_url=reverse_lazy('libroAutor_listar')

    def dispatch(self, request, *args, **kwargs) :
        if self.request.user.is_anonymous:
             return redirect('error')

        return super(Libros_Autor_update_sebm,self).dispatch(request,*args, **kwargs)

#Eliminar Libros por autor
    
class Libros_Autor_delate_sebm(View):
    def get(self, request, id_lib_aut_sebm):
        libros_por_autor = TblLibroPorAutor.objects.get(id_autor=id_lib_aut_sebm)
        libros_por_autor= 'INACTIVO'
        libros_por_autor.save()  # type: ignore
        return redirect('libroAutor_listar')
#Reporte Libros por autor

class Libros_Autor_report_sebm(View):
    def get(self, request, *args, **kwargs):
        object_list = TblLibroPorAutor.objects.all()
        data = {
            'object_list': object_list
        }
        pdf = render_to_pdf('djappsebm/libro_autor/listar_libro_autor.html', data)
        return HttpResponse(pdf, content_type='application/pdf')