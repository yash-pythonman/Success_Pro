# Generated by Django 2.2.2 on 2019-07-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('page', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('sub_page', models.CharField(max_length=200)),
                ('sup_page_image', models.CharField(max_length=200)),
            ],
        ),
    ]