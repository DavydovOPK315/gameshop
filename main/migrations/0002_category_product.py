# Generated by Django 2.2.6 on 2020-05-30 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30)),
                ('slug', models.SlugField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30)),
                ('slug', models.SlugField(max_length=10)),
                ('year', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, upload_to='photo_products')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('count', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(related_name='products', to='main.Category')),
                ('os', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Os')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Studio')),
            ],
            options={
                'ordering': ['name'],
                'index_together': {('id', 'slug')},
            },
        ),
    ]
