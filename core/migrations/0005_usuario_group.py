# Generated by Django 4.0.4 on 2022-06-29 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0004_remove_usuario_group_remove_usuario_idtipousuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]
