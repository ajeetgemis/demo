# Generated by Django 3.2.16 on 2023-01-16 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_categ', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=20)),
                ('p_description', models.CharField(max_length=30)),
                ('p_image', models.ImageField(upload_to='uploads\\products')),
                ('p_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.categories')),
            ],
        ),
    ]
