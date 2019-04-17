# Generated by Django 2.2 on 2019-04-17 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beer_app', '0004_auto_20190417_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='beer_app.User'),
        ),
        migrations.AlterField(
            model_name='review',
            name='beer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers', to='beer_app.Beer'),
        ),
    ]
