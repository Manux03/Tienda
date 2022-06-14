# Generated by Django 3.2.4 on 2022-05-26 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_compra_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra_detalle',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='compra_detalle',
            name='idEstado',
        ),
        migrations.AddField(
            model_name='compra_detalle',
            name='idProducto',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='core.producto'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Compra_Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, verbose_name='descripcion')),
                ('idEstado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estado')),
                ('idcompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.compra')),
            ],
        ),
    ]