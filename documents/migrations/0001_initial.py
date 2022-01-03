# Generated by Django 4.0 on 2021-12-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedure_id', models.CharField(max_length=20, unique=True)),
                ('procedure_name', models.CharField(max_length=200)),
                ('procedure_department', models.CharField(max_length=50)),
                ('procedure_file', models.FileField(upload_to='procedures/%Y/%m/%d/')),
                ('procedure_date', models.CharField(max_length=20)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
