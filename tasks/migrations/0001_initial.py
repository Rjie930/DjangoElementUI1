# Generated by Django 4.2.2 on 2023-06-29 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
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
                    "name",
                    models.CharField(max_length=65, unique=True, verbose_name="活动名称"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("u", "未开始的活动"), ("o", "正在进行的活动"), ("f", "已经完成的活动")],
                        max_length=1,
                        verbose_name="活动类型",
                    ),
                ),
            ],
            options={
                "verbose_name": "任务",
                "verbose_name_plural": "任务",
            },
        ),
    ]