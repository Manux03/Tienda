#TODOUSERSSSSS
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique='True', verbose_name='Nombre Usuario')),
                ('email', models.EmailField(max_length=254, unique='True', verbose_name='Correo Electronico')),
                ('nombres', models.CharField(max_length=200, null='False', verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=200, null='False', verbose_name='Apellido')),
                ('usuario_administrador', models.BooleanField(default=False)),
                ('usuario_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]