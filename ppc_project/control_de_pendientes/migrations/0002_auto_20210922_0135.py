# Generated by Django 3.2.7 on 2021-09-22 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('control_de_pendientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_de_pendientes.area'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='criticality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_de_pendientes.criticality'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='intervention_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_de_pendientes.intervention_method'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_de_pendientes.specialty'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_de_pendientes.state'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_de_pendientes.system'),
        ),
        migrations.AlterField(
            model_name='pending',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
