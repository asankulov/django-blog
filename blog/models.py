from django.db import models
from django.utils import timezone
from django.urls import reverse

from blog.helper import PathAndRename


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now, editable=False)
    image = models.ImageField(verbose_name='Картинка', upload_to=PathAndRename('post_images/'))

    class Meta:
        ordering = ('-date_posted',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class CustomBaseModel(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    image = models.ImageField(verbose_name='Фото', upload_to=PathAndRename('avatars/'))

    class Meta:
        abstract = True

    def __str__(self):
        return self.full_name


class CustomStaffBaseModel(CustomBaseModel):
    title = models.CharField(verbose_name='Должность', max_length=255)

    def __str__(self):
        return f'{self.title} - {self.full_name}'

    class Meta:
        abstract = True


class Administration(CustomStaffBaseModel):
    class Meta:
        verbose_name = 'Администрация'
        verbose_name_plural = 'Администрация'

    def get_absolute_url(self):
        return reverse('administration_detail', kwargs={'pk': self.pk})


class Teacher(CustomStaffBaseModel):
    class Meta:
        verbose_name = 'Педагогический состав'
        verbose_name_plural = 'Педагогический состав'

    def get_absolute_url(self):
        return reverse('teacher_detail', kwargs={'pk': self.pk})


class OurPride(CustomBaseModel):
    class Meta:
        verbose_name = 'Ими гордится школа'
        verbose_name_plural = 'Ими гордится школа'

    def get_absolute_url(self):
        return reverse('our_pride_detail', kwargs={'pk': self.pk})


class Honour(CustomBaseModel):
    class Meta:
        verbose_name = 'Отличники образования'
        verbose_name_plural = 'Отличники образования'

    def get_absolute_url(self):
        return reverse('honour_detail', kwargs={'pk': self.pk})
