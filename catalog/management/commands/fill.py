from django.core.management import BaseCommand

from catalog.models import Category, Products


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        category = [
            {"name": "продукты", "description": ""},
            {"name": "морепродукты", "description": "достают из воды"},
            {"name": "напитки", "description": "пьют"},
        ]
        return category

    @staticmethod
    def json_read_products():
        products = [
            {"name": "cola", "description": "", "category": 6, "price": 70},
            {
                "name": "семга",
                "description": "",
                "category": 5,
                "price": 100,
            },
            {"name": "сода", "description": "", "category": 4, "price": 40},
        ]
        return products

    def handle(self, *args, **options):

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(Category(**category))
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(Products(**product))

        Products.objects.bulk_create(product_for_create)


# #
# #
# # class Command(BaseCommand):
# #     def handle(self, *args, **options):
# #         student_list = [
# #             {'last_name': 'Петров', 'first_name': 'Иван'},
# #             {'last_name': 'Семенов', 'first_name': 'Петр'},
# #             {'last_name': 'Артемов', 'first_name': 'Сема'},
# #             {'last_name': 'Иванов', 'first_name': 'Артем'},
# #             {'last_name': 'Романов', 'first_name': 'Роман'},
# #             {'last_name': 'Ларин', 'first_name': 'Андрей'},
# #             {'last_name': 'Карсунчов', 'first_name': 'Филипп'},
# #         ]
# #
# #         # for student_item in student_list:
# #         #     Student.objects.create(**student_item)
# #
# #         student_for_crete = []
# #         for student_item in student_list:
# #             student_for_crete.append(
# #                 Student(**student_item)
# #             )
# #         Student.objects.bulk_create(student_for_crete)
