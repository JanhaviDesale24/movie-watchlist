# Generated by Django 5.1.6 on 2025-03-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('watched', 'Watched'), ('to_watch', 'To Watch')], default='to_watch', max_length=10)),
                ('rating', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
