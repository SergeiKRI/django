from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование товара",
    )
    description = models.TextField(
        max_length=100,
        verbose_name="Описание",
        help_text="Напишите описание",
        **NULLABLE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("name",)


class Products(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование товара",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Напишите описание", **NULLABLE
    )
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Превью",
        help_text="Загрузите картинку",
        **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Укажите категорию",
        **NULLABLE,
        related_name='products'
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Укажите цену товара"
    )
    date_created_at = models.DateTimeField(
        auto_created=True,
        verbose_name="Дата добавления",
        help_text="Дата добавления",
    )
    date_updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения",
        help_text="Дата изменения",
    )

    # is_active = models.BooleanField(default=True, verbose_name='Есть')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = (
            "name",
            "category",
            "price",
            "date_created_at",
            "date_updated_at",
        )

