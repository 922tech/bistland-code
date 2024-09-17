# Generated by Django 4.2.11 on 2024-09-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Titanic",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("passengerID", models.IntegerField(primary_key=True, serialize=False)),
                ("survived", models.BooleanField()),
                (
                    "pclass",
                    models.IntegerField(
                        choices=[(1, "First"), (2, "Second"), (3, "Third")]
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("sex", models.CharField(max_length=10)),
                ("age", models.FloatField(blank=True, null=True)),
                ("sibsp", models.IntegerField()),
                ("parch", models.IntegerField()),
                ("ticket", models.CharField(max_length=20)),
                ("fare", models.FloatField()),
                ("cabin", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "embarked",
                    models.CharField(
                        choices=[
                            ("C", "Cherbourg"),
                            ("S", "Southampton"),
                            ("Q", "Queenstown"),
                            ("NaN", "Not Known"),
                        ],
                        max_length=3,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
