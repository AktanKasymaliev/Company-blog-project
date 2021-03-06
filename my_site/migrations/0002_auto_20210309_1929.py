# Generated by Django 3.1.7 on 2021-03-09 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='advertismentimages',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='my_site.advertisment'),
        ),
        migrations.AddField(
            model_name='advertisment',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_site.company'),
        ),
    ]
