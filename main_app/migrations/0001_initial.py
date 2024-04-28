# Generated by Django 5.0.4 on 2024-04-28 06:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardID', models.IntegerField(max_length=20)),
                ('name', models.CharField(max_length=75)),
                ('game', models.CharField(choices=[(1, 'Unlisted'), (2, 'Magic the Gathering'), (3, 'Pokemon'), (4, 'Yu-Gi-Oh')], default=2, max_length=1)),
                ('rarity', models.CharField(max_length=15)),
                ('cardType', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('frontImageURL', models.CharField(max_length=500)),
                ('backImageURL', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deckID', models.IntegerField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(default='No Description', max_length=500)),
                ('game', models.CharField(choices=[(1, 'Unlisted'), (2, 'Magic the Gathering'), (3, 'Pokemon'), (4, 'Yu-Gi-Oh')], default=1, max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
