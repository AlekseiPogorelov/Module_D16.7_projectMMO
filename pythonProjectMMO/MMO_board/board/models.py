from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.conf import settings


class Post(models.Model):
    TYPE = (
        ('tanks', 'Танки'),
        ('heals', 'Хилы'),
        ('dd', 'ДД'),
        ('traders', 'Торговцы'),
        ('gm', 'Гилдматеры'),
        ('qg', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('tanners', 'Кожевники'),
        ('potionmakers', 'Зельевары'),
        ('spell masters', 'Мастера заклинаний'),
    )

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    category = models.CharField(
        max_length=20,
        verbose_name="Категория",
        choices=TYPE,
        default='tanks',
    )

    subject = models.CharField("Тема", max_length=200)
    description = models.TextField("Объявление", max_length=20000)

    # images = models.ForeignKey(
    #     'gallery.Gallery',
    #     verbose_name="Изображения",
    #     blank=True,
    #     null=True,
    #     on_delete=models.SET_NULL
    # )
    # file = models.FileField("Файл", upload_to="board_file/", blank=True, null=True)
    # created = models.DateTimeField("Дата создания", auto_now_add=True)
    # slug = models.SlugField("url", max_length=200, blank=True, null=True)
    #
    # def save(self, *args, **kwargs):
    #     self.slug = transliteration_rus_eng(self.subject) + "_" + str(self.id)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"category": self.category, "slug": self.slug})

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class UserResponse(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="Объявление", on_delete=models.CASCADE)
    subject = models.CharField("Тема", max_length=300)
    text = models.TextField("Текст объявления", max_length=20000)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        super(UserResponse, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = 'Отклики'
