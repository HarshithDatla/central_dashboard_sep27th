# Generated by Django 4.2.5 on 2023-09-28 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trust',
            name='user',
            field=models.ManyToManyField(related_name='trusts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='school',
            name='trust',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='dashboard.trust'),
        ),
    ]
