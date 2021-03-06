# Generated by Django 4.0.3 on 2022-03-10 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_id', models.CharField(max_length=100, unique=True)),
                ('document_name', models.CharField(max_length=200)),
                ('document_file', models.FileField(upload_to='documents/%Y/%m/%d/')),
                ('document_date', models.CharField(max_length=20)),
                ('access_for_all', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.department')),
                ('document_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.documentsection')),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.documentvariation')),
            ],
        ),
    ]
