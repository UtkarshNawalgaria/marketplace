# Generated by Django 3.1.13 on 2022-05-19 16:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import marketplace.product.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220519_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='background_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to=marketplace.product.models.Category.upload_path),
        ),
        migrations.AddField(
            model_name='category',
            name='image_alt_text',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI'),
        ),
        migrations.CreateModel(
            name='ProductMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to=marketplace.product.models.ProductMedia.upload_path)),
                ('image_alt_text', models.CharField(blank=True, max_length=128)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='media', to='product.product')),
            ],
            options={
                'verbose_name': 'Product Media',
                'verbose_name_plural': 'Product Media',
            },
        ),
    ]
