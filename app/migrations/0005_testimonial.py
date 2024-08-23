# Generated by Django 4.2.13 on 2024-08-23 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_miniblocks_treeblocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='testimonial')),
            ],
            options={
                'verbose_name': ' Testimonial',
                'verbose_name_plural': ' Testimonial',
            },
        ),
    ]