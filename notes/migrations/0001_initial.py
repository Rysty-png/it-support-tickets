from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Note",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("course", models.CharField(help_text="Course code, like CS101", max_length=10)),
                ("title", models.CharField(max_length=120)),
                ("body", models.TextField(blank=True)),
                ("done", models.BooleanField(default=False, help_text="Revised already?")),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["done", "-created"],
            },
        ),
    ]
