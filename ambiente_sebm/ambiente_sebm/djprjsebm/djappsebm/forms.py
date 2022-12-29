from django import forms
from djappsebm.models import *

class addClientesForm(forms.ModelForm):

    class Meta:
        
        model = TblClientes
        fields= '__all__'


class addCategoriaForm(forms.ModelForm):

    class Meta:
        model = TblCategorias
        fields= '__all__'
        
        
class addUsuariosForm(forms.ModelForm):

    class Meta:
        model = TblUsuarios
        fields= '__all__'


class addLibrosForm(forms.ModelForm):

    class Meta:
        model = TblLibros
        fields= '__all__'

        

class addAutorForm(forms.ModelForm):

    class Meta:

        model=TblAutores
        fields= '__all__'

    
    widgets={            
            
            'estado': forms.TextInput(attrs={'value': 'ACTIVO', 'readonly' : 'true'}),
        }

class FormPedidoCliente(forms.ModelForm):

    class Meta:
        model = TblPedidoCliente
        fields = '__all__'

    
        widgets={            
                
                'estado': forms.TextInput(attrs={'value': 'ACTIVO', 'readonly' : 'true'})

        }

class FormLibroPorAutor(forms.ModelForm):

    class Meta:
        
        model=TblLibroPorAutor
        fields= '__all__'

        

        widgets={
            
            'estado':forms.TextInput(attrs={'value':'ACTIVO', 'readonly':'true'}),
            
        }