# Generated by Django 4.2.2 on 2023-07-05 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_outlet", "0004_author_alter_book_slug_alter_book_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books",
                to="book_outlet.author",
            ),
        ),
    ]
