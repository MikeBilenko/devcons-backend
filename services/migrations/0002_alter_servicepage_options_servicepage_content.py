# Generated by Django 5.0.6 on 2024-05-25 15:54

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicepage',
            options={'verbose_name': 'Service Page', 'verbose_name_plural': 'Service Pages'},
        ),
        migrations.AddField(
            model_name='servicepage',
            name='content',
            field=wagtail.fields.StreamField([('stages', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('stages', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=255, required=True)), ('description', wagtail.blocks.TextBlock(max_length=750, required=True))])))])), ('why', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', max_length=255, required=True)), ('why_sections', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=255, required=True)), ('description', wagtail.blocks.TextBlock(max_length=750, required=True)), ('icon', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('faq', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', max_length=250, required=True)), ('faqs', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(max_length=200, required=True)), ('answer', wagtail.blocks.TextBlock(max_length=400, required=True))])))]))], blank=True, null=True),
        ),
    ]
