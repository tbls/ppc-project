# Generated by Django 3.2.7 on 2021-09-22 14:45

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('control_de_pendientes', '0008_auto_20210922_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_de_pendientes.area', verbose_name='Área'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='criticality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_de_pendientes.criticality', verbose_name='Criticidad'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='detection_date',
            field=models.DateField(verbose_name='Fecha de detección'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='intervention_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_de_pendientes.intervention_method', verbose_name='Método de Intervención'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='machine',
            field=models.CharField(max_length=50, verbose_name='Equipo / Instrumento'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='notice_number',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Sistema'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='observations',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Sistema'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='registration_date',
            field=models.DateField(default=django.utils.timezone.now, editable=False, verbose_name='Sistema'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_de_pendientes.specialty', verbose_name='Especialidad'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_de_pendientes.state', verbose_name='Sistema'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_de_pendientes.system', verbose_name='Sistema'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='user',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Reportado por'),
        ),
    ]