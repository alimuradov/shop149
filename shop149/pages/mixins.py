from django.db import models


class SeoMixin(models.Model):
    # SEO BLOCK
    page_title = models.CharField('Заголовок страницы в браузере', max_length=60, blank=True)
    meta_description = models.CharField('Описание страницы в браузере', max_length=180, blank=True)
    meta_keywords = models.CharField('ключевые слова', max_length=512, blank=True)

    class Meta:
        abstract = True
