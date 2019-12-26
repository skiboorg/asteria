from django.db import models

class Comment(models.Model):
    image = models.ImageField('Картинка отзыва большая 400 х 340 px', upload_to='comments', blank=False)
    writtenBy = models.CharField('От кого отзыв', max_length=75, blank=False, default='')
    description = models.TextField('Текст отзыва (примерно 380 слов)',  blank=False)


    def __str__(self):
        return 'Отзыв №{}'.format(self.id)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"