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
        ('appliances', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computing_Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='ICONS')),
                ('verified', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Computing_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Computing_Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Computing_Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Computing_Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Computing_Memory_Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Computing Memory Metric',
                'verbose_name_plural': 'Computing Memory Metrics',
            },
        ),
        migrations.CreateModel(
            name='Computing_Memory_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Computing Memory Type',
                'verbose_name_plural': 'Computing Memory Types',
            },
        ),
        migrations.CreateModel(
            name='Computing_Operating_System',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='ICONS')),
            ],
            options={
                'verbose_name': 'Computing operating system',
                'verbose_name_plural': 'Computing operating systems',
            },
        ),
        migrations.CreateModel(
            name='Computing_Ram_Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Computing Ram Metric',
                'verbose_name_plural': 'Computing Ram Metrics',
            },
        ),
        migrations.CreateModel(
            name='Computing_Screen_Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Computing Screen Size',
                'verbose_name_plural': 'Computing Screen Sizes',
            },
        ),
        migrations.CreateModel(
            name='Computing_Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Computing_Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.ManyToManyField(to='computersandaccessories.computing_category')),
            ],
        ),
        migrations.CreateModel(
            name='Computing_Weight_Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Computing Weight Metric',
                'verbose_name_plural': 'Computing Weight Metrics',
            },
        ),
        migrations.CreateModel(
            name='Computing_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('subcategory', models.ManyToManyField(to='computersandaccessories.computing_sub_category')),
            ],
        ),
        migrations.CreateModel(
            name='Computing',
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
                ('title', models.CharField(max_length=150)),
                ('model', models.CharField(blank=True, max_length=150, null=True)),
                ('processor', models.CharField(blank=True, max_length=150, null=True)),
                ('ram', models.CharField(blank=True, max_length=150, null=True)),
                ('storage', models.CharField(blank=True, max_length=4, null=True)),
                ('graphics_card', models.CharField(blank=True, max_length=150, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='computersandaccessories.computing_brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computing_items', to='computersandaccessories.computing_category')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='computersandaccessories.computing_color')),
                ('condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='computersandaccessories.computing_condition')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='computersandaccessories.computing_material')),
                ('operating_system', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='computersandaccessories.computing_operating_system')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business')),
                ('packaging', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appliances.package')),
                ('per', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appliances.per')),
                ('ram_metrics', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='computersandaccessories.computing_ram_metric')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.region')),
                ('screen_size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='computersandaccessories.computing_screen_size')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='computersandaccessories.computing_size')),
                ('storage_metrics', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='computersandaccessories.computing_memory_metric')),
                ('storage_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='computersandaccessories.computing_memory_type')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computing_subitems', to='computersandaccessories.computing_sub_category')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computing_subtypeitems', to='computersandaccessories.computing_type')),
                ('weight_metrics', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='computersandaccessories.computing_weight_metric')),
            ],
            options={
                'verbose_name': 'Computing Product',
                'verbose_name_plural': 'Computing  Products',
            },
        ),
    ]
