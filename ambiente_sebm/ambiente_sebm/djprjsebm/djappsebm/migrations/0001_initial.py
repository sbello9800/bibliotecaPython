# Generated by Django 4.0.8 on 2022-11-15 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblAutores',
            fields=[
                ('id_autor', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=25)),
                ('apellidos', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=25)),
                ('estado', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=10)),
            ],
            options={
                'db_table': 'tbl_autores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblCategorias',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=40)),
                ('estado', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=10)),
            ],
            options={
                'db_table': 'tbl_categorias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblClientes',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('identificacion', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=11)),
                ('nombres', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=25)),
                ('apellidos', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=25)),
                ('telefono', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=12)),
                ('direccion', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=100)),
                ('correo_electronico', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=100)),
                ('estado', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=10)),
            ],
            options={
                'db_table': 'tbl_clientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblLibros',
            fields=[
                ('isbn', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=125)),
                ('fecha_pub', models.DateField()),
                ('precio', models.IntegerField()),
                ('portada', models.CharField(blank=True, db_collation='Modern_Spanish_CI_AS', max_length=125, null=True)),
                ('cantidad_stock', models.IntegerField()),
                ('estado', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=10)),
            ],
            options={
                'db_table': 'tbl_libros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblPedidoCliente',
            fields=[
                ('id_pedido', models.IntegerField(primary_key=True, serialize=False)),
                ('nro_pedido', models.IntegerField()),
                ('fecha_pedido', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('estado', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=10)),
            ],
            options={
                'db_table': 'tbl_pedido_cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblLibroPorAutor',
            fields=[
                ('id_autor', models.OneToOneField(db_column='id_autor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='djappsebm.tblautores')),
                ('estado', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=10)),
            ],
            options={
                'db_table': 'tbl_libro_por_autor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblUsuarios',
            fields=[
                ('id_usuario', models.OneToOneField(db_column='id_usuario', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='djappsebm.tblclientes')),
                ('id_cliente', models.IntegerField()),
                ('usuario', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=128)),
                ('clave', models.CharField(db_collation='Modern_Spanish_CI_AS', max_length=128)),
            ],
            options={
                'db_table': 'tbl_usuarios',
                'managed': False,
            },
        ),
    ]