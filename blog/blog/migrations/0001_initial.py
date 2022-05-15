# Generated by Django 4.0.4 on 2022-05-15 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]