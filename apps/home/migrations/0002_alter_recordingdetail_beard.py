# Generated by Django 3.2.11 on 2024-02-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordingdetail',
            name='beard',
            field=models.CharField(choices=[('Full beard', 'Full beard'), ('Mustache', 'Mustache'), ('Goatbeard', 'Goatbeard'), ('Henriquatre', 'Henriquatre')], max_length=100, null=True),
        ),
    ]