# Generated by Django 3.2.6 on 2023-10-25 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0013_alter_detalleusuario_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleusuario',
            name='tipo',
            field=models.CharField(default='No verificado', max_length=20, null=True),
        ),
    ]
