# Generated by Django 4.1.7 on 2023-06-27 10:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appliance_Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('icon', models.ImageField(upload_to='ICONS')),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Appliance_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Appliance_Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Appliance_Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Appliance_Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Appliance_Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Appliance_Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.ManyToManyField(to='appliances.appliance_category')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Per',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Appliance_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('subcategory', models.ManyToManyField(to='appliances.appliance_sub_category')),
            ],
        ),
        migrations.CreateModel(
            name='Appliance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=False, quality=97, scale=None, size=[600, 600], upload_to=products.models.upload_location)),
                ('image2', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=False, null=True, quality=97, scale=None, size=[600, 600], upload_to=products.models.upload_location)),
                ('image3', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=False, null=True, quality=97, scale=None, size=[600, 600], upload_to=products.models.upload_location)),
                ('image4', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=False, null=True, quality=97, scale=None, size=[600, 600], upload_to=products.models.upload_location)),
                ('image5', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=False, null=True, quality=97, scale=None, size=[600, 600], upload_to=products.models.upload_location)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('currency', models.CharField(default='KES', max_length=5)),
                ('quantity', models.SmallIntegerField(default=1)),
                ('negotiable', models.BooleanField(default=False)),
                ('sponsored', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=False)),
                ('most_sold', models.BooleanField(default=False)),
                ('out_of_stock', models.BooleanField(default=False)),
                ('rating', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('product_serial', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('power_rating', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appliances.appliance_brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appliance_items', to='appliances.appliance_category')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appliances.appliance_color')),
                ('condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appliances.appliance_condition')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appliances.appliance_material')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business')),
                ('packaging', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appliances.package')),
                ('per', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appliances.per')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.region')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appliances.appliance_size')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appliance_subitems', to='appliances.appliance_sub_category')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appliance_subtypeitems', to='appliances.appliance_type')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
