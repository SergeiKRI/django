# Generated by Django 5.0.4 on 2024-06-06 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_category_products_delete_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите заголовок",
                        max_length=100,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        blank=True,
                        help_text="Введите ссылку",
                        max_length=100,
                        null=True,
                        verbose_name="Ссылка",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        blank=True,
                        help_text="Напишите текст",
                        null=True,
                        verbose_name="Содержание",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите картинку",
                        null=True,
                        upload_to="blog/",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "date_created_at",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime.now,
                        help_text="ДД.ММ.ГГГГ",
                        null=True,
                        verbose_name="Дата добавления",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Есть")),
                (
                    "count_views",
                    models.PositiveIntegerField(
                        blank=True,
                        default=0,
                        help_text="Укажите количество просмотров",
                        null=True,
                        verbose_name="Количество просмотров",
                    ),
                ),
            ],
            options={
                "verbose_name": "запись",
                "verbose_name_plural": "записи",
                "ordering": (
                    "title",
                    "slug",
                    "text",
                    "image",
                    "date_created_at",
                    "is_active",
                    "count_views",
                ),
            },
        ),
        migrations.AlterField(
            model_name="products",
            name="date_created_at",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime.now,
                help_text="ДД.ММ.ГГГГ",
                null=True,
                verbose_name="Дата добавления",
            ),
        ),
        migrations.AlterField(
            model_name="products",
            name="date_updated_at",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime.now,
                help_text="ДД.ММ.ГГГГ",
                null=True,
                verbose_name="Дата изменения",
            ),
        ),
        migrations.AlterField(
            model_name="products",
            name="price",
            field=models.IntegerField(
                blank=True,
                help_text="Укажите цену товара",
                null=True,
                verbose_name="Цена за покупку",
            ),
        ),
    ]