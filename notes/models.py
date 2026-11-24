from django.db import models


class Ticket(models.Model):

    PRIORITY_CHOICES = [
        ('Низкий', 'Низкий'),
        ('Средний', 'Средний'),
        ('Высокий', 'Высокий'),
    ]

    STATUS_CHOICES = [
        ('Новая', 'Новая'),
        ('В работе', 'В работе'),
        ('Завершена', 'Завершена'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Новая'
    )

    def __str__(self):
        return self.title
