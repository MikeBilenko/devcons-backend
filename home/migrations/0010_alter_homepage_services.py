# Generated by Django 5.0.6 on 2024-05-25 16:37

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_homepage_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='services',
            field=wagtail.fields.StreamField([('services', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Services', max_length=250, required=True)), ('services', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Service Title', max_length=100, required=True)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False))])))]))], blank=True, null=True),
        ),
    ]
