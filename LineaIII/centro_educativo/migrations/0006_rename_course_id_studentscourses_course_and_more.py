# Generated by Django 4.1.1 on 2022-10-30 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centro_educativo', '0005_rename_students_courses_studentscourses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentscourses',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='studentscourses',
            old_name='student_id',
            new_name='student',
        ),
    ]