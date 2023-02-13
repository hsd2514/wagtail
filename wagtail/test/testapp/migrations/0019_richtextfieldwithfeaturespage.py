# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 22:20
from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0040_page_draft_title"),
        ("tests", "0018_multiselect_form_field"),
    ]

    operations = [
        migrations.CreateModel(
            name="RichTextFieldWithFeaturesPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                ("body", wagtail.fields.RichTextField()),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]