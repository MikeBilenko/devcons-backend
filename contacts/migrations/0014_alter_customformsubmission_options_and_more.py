# Generated by Django 5.0.6 on 2024-06-11 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0013_alter_customformsubmission_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customformsubmission',
            options={'verbose_name': 'form submission', 'verbose_name_plural': 'form submissions'},
        ),
        migrations.AlterUniqueTogether(
            name='customformsubmission',
            unique_together=set(),
        ),
    ]
