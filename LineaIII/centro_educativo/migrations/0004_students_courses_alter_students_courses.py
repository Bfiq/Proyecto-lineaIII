# Generated by Django 4.1.1 on 2022-10-30 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centro_educativo', '0003_remove_courses_students_students_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students_Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centro_educativo.courses')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centro_educativo.students')),
            ],
        ),
        migrations.AlterField(
            model_name='students',
            name='courses',
            field=models.ManyToManyField(through='centro_educativo.Students_Courses', to='centro_educativo.courses'),
        ),
    ]