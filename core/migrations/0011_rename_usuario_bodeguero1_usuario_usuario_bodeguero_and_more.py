# Generated by Django 4.0.4 on 2022-06-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_usuario_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario_bodeguero1',
            new_name='usuario_bodeguero',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario_vendedor1',
            new_name='usuario_contador',
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuario_vendedor',
            field=models.BooleanField(default=False),
        ),
    ]
