# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Modern_Spanish_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    email = models.CharField(max_length=254, db_collation='Modern_Spanish_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class TblClientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=11, db_collation='Modern_Spanish_CI_AS')
    nombres = models.CharField(max_length=25, db_collation='Modern_Spanish_CI_AS')
    apellidos = models.CharField(max_length=25, db_collation='Modern_Spanish_CI_AS')
    telefono = models.CharField(max_length=12, db_collation='Modern_Spanish_CI_AS')
    direccion = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    correo_electronico = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    estado = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'tbl_clientes'

    def __str__(self):
        return '{}'.format(self.nombres)


class TblUsuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(TblClientes, models.DO_NOTHING, db_column='id_cliente')
    usuario = models.CharField(max_length=128, db_collation='Modern_Spanish_CI_AS')
    clave = models.CharField(max_length=128, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'tbl_usuarios'

    def __str__(self):
        return '{}'.format(self.usuario)


class TblCategorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=40, db_collation='Modern_Spanish_CI_AS')
    estado = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'tbl_categorias'

    def __str__(self):
        return '{}'.format(self.categoria)

class TblLibros(models.Model):
    isbn = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=125, db_collation='Modern_Spanish_CI_AS')
    fecha_pub = models.DateField()
    categoria = models.ForeignKey(TblCategorias, models.DO_NOTHING, db_column='categoria')
    precio = models.IntegerField()
    portada = models.FileField()
    cantidad_stock = models.IntegerField()
    estado = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'tbl_libros'

    def __str__(self):
        return '{}'.format(self.titulo)

class TblAutores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=25, db_collation='Modern_Spanish_CI_AS')
    apellidos = models.CharField(max_length=25, db_collation='Modern_Spanish_CI_AS')
    estado = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'tbl_autores'

    def __str__(self):
        return '{}'.format(self.nombres)

class TblLibroPorAutor(models.Model):
    id_autor = models.OneToOneField(TblAutores, models.DO_NOTHING, db_column='id_autor', primary_key=True)
    isbn = models.ForeignKey(TblLibros, models.DO_NOTHING, db_column='isbn')
    estado = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'tbl_libro_por_autor'
        unique_together = (('id_autor', 'isbn'),)


class TblPedidoCliente(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    nro_pedido = models.IntegerField()
    id_cliente = models.ForeignKey(TblClientes, models.DO_NOTHING, db_column='id_cliente')
    isbn = models.ForeignKey(TblLibros, models.DO_NOTHING, db_column='isbn')
    fecha_pedido = models.DateField()
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    estado = models.CharField(max_length=10, db_collation='Modern_Spanish_CI_AS')
    
    class Meta:
        managed = False
        db_table = 'tbl_pedido_cliente'
    
    def __str__(self):
        return '{}'.format(self.nro_pedido)
    
