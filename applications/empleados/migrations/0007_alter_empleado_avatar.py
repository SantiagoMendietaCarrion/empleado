# Generated by Django 4.2.23 on 2025-07-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0006_empleado_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleados', verbose_name='Avatar'),
        ),
    ]
