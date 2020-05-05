from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse


from pages.mixins import SeoMixin


class Page(SeoMixin):
    title = models.CharField('Заголовок странциы', max_length=128)
    body = models.TextField('Текст страницы')
    created = models.DateTimeField('Добавлено', auto_now_add=True)
    modified = models.DateTimeField('Изменено', auto_now=True)
    slug = models.SlugField('url-страницы')

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pages', kwargs={'slug': self.slug})

    def render_body(self):
        return mark_safe(self.body)
