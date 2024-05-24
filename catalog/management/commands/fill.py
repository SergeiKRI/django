from django.core.management import BaseCommand

# from catalog.models import Student
#
#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         student_list = [
#             {'last_name': 'Петров', 'first_name': 'Иван'},
#             {'last_name': 'Семенов', 'first_name': 'Петр'},
#             {'last_name': 'Артемов', 'first_name': 'Сема'},
#             {'last_name': 'Иванов', 'first_name': 'Артем'},
#             {'last_name': 'Романов', 'first_name': 'Роман'},
#             {'last_name': 'Ларин', 'first_name': 'Андрей'},
#             {'last_name': 'Карсунчов', 'first_name': 'Филипп'},
#         ]
#
#         # for student_item in student_list:
#         #     Student.objects.create(**student_item)
#
#         student_for_crete = []
#         for student_item in student_list:
#             student_for_crete.append(
#                 Student(**student_item)
#             )
#         Student.objects.bulk_create(student_for_crete)
