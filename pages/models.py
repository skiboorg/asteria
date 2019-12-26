from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from random import choices
import string

class Master(models.Model):
    name = models.CharField('Имя и Фамилия мастера', max_length=255, blank=False, null=True)
    job = models.CharField('Специализация', max_length=255, blank=False, null=True)
    info = models.TextField('Информация', max_length=255, blank=False, null=True)

    def __str__(self):
        return 'Специалист : {}'.format(self.name)

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

class ServiceName(models.Model):
    name = models.CharField('Вид работы', max_length=255, blank=False, null=True)
    image = models.ImageField('Изображение превью (360 x 250)', upload_to='services_img/', blank=False, null=True)
    imageHeader = models.ImageField('Изображение для бекграунда страницы с услугой (1920х560)')
    topText = RichTextUploadingField('Текст на страницу с услугой', blank=True, null=True)
    acc1Text = RichTextUploadingField('Показания', blank=True, null=True)
    acc2Text = RichTextUploadingField('Противопоказания', blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, unique=True, db_index=True)
    page_h1 = models.CharField('Тег H1', max_length=255, blank=False, null=True)
    page_title = models.CharField('Название страницы SEO', max_length=255, blank=False, null=True)
    page_description = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True)
    page_keywords = models.TextField('Keywords SEO', blank=True, null=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if not self.name_slug:
            testSlug = ServiceName.objects.filter(name_slug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.name_slug = slug + slugRandom
        self.name_lower = self.name.lower()
        super(ServiceName, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return f'/service/{self.name_slug}/'

    def get_header(self):
        if self.imageHeader:
            return self.imageHeader.url
        else:
            return '/static/img/about-us-bg.jpg'

    def __str__(self):
        return 'Вид работы : {}'.format(self.name)

    class Meta:
        verbose_name = "Вид работы"
        verbose_name_plural = "Виды работ"


class SeoTag(models.Model):
    indexTitle = models.CharField('Тег Title для главной', max_length=255, blank=True, null=True)
    indexDescription = models.CharField('Тег Description для главной', max_length=255, blank=True, null=True)
    indexKeywords = models.TextField('Тег Keywords для главной',  blank=True, null=True)
    servicesTitle = models.CharField('Тег Title для страницы со всеми услугами', max_length=255, blank=True, null=True)
    servicesDescription = models.CharField('Тег Description для страницы со всеми услугам', max_length=255, blank=True,
                                           null=True)
    servicesKeywords = models.TextField('Тег Keywords для страницы со всеми услугам', blank=True, null=True)
    postsTitle = models.CharField('Тег Title для страницы со всеми статьями', max_length=255, blank=True, null=True)
    postsDescription = models.CharField('Тег Description для страницы со всеми статьями', max_length=255, blank=True,
                                           null=True)
    postsKeywords = models.TextField('Тег Keywords для страницы со всеми статьями', blank=True, null=True)
    aboutTitle = models.CharField('Тег Title для страницы о компании', max_length=255, blank=True, null=True)
    aboutDescription = models.CharField('Тег Description для страницы о компании', max_length=255, blank=True,
                                        null=True)
    aboutKeywords = models.TextField('Тег Keywords для страницы о компании', blank=True, null=True)

    yandexMetrika = models.TextField('Код Яндекс метрики',  blank=True, null=True)
    fbPixel = models.TextField('Код пикселя', blank=True, null=True)
    yandexTAG = models.CharField('Код подтверждения Яндекс', max_length=255, blank=True, null=True)
    googleTAG = models.CharField('Код подтверждения google', max_length=255, blank=True, null=True)

    def __str__(self):
        return 'Теги для статических страниц'

    class Meta:
        verbose_name = "Теги для статических страниц"
        verbose_name_plural = "Теги для статических страниц"

