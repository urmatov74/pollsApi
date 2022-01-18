# Generated by Django 3.1.4 on 2022-01-18 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20220118_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vote_variant', to='polls.variant'),
        ),
    ]