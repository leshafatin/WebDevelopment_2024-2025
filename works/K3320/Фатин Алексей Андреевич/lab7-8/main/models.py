from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]  # Оценка от 1 до 5

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name="Оценка")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

    def __str__(self):
        return f"Отзыв от {self.name} ({self.rating}/5)"