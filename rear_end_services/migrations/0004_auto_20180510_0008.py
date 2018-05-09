# Generated by Django 2.0.4 on 2018-05-09 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rear_end_services', '0003_region_region_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='region_id',
            new_name='rid',
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_region', to='rear_end_services.Region', verbose_name='地区'),
        ),
    ]
