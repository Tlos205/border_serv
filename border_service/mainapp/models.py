# mainapp/models.py
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField   # для красивого редактирования текста


class News(models.Model):
    """Новости и пресс-релизы"""
    title = models.CharField("Заголовок", max_length=200)
    slug = models.SlugField("URL (авто)", max_length=200, unique_for_date='pub_date')
    content = RichTextField("Текст новости")
    pub_date = models.DateField("Дата публикации", default=timezone.now)
    is_published = models.BooleanField("Опубликовано", default=True)
    is_important = models.BooleanField("Важное объявление (на главную)", default=False)
    image = models.ImageField("Фото (необязательно)", upload_to='news/', blank=True, null=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости и пресс-релизы"
        ordering = ['-pub_date']

    def __str__(self):
        return self.title


class Leader(models.Model):
    """Руководство"""
    POSITION_CHOICES = [
        ('chief', 'Начальник Пограничного управления'),
        ('deputy_chief', 'Первый заместитель'),
        ('deputy_personnel', 'Заместитель по работе с личным составом'),
        ('deputy_coast', 'Заместитель — начальник отдела пограничной охраны'),
        ('deputy_logistics', 'Заместитель - начальник отдела материально-технического обеспечения'),
        ('other', 'Иное руководство'),
    ]

    rank = models.CharField("Звание", max_length=50)
    full_name = models.CharField("ФИО", max_length=100)
    position = models.CharField("Должность", max_length=50, choices=POSITION_CHOICES)
    photo = models.ImageField("Фотография", upload_to='leaders/')
    years_service = models.CharField("Годы службы", max_length=100, blank=True)
    awards = RichTextField("Награды и заслуги", blank=True)
    sort_order = models.PositiveIntegerField("Порядок сортировки", default=0)

    class Meta:
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководство"
        ordering = ['sort_order', 'id']

    def __str__(self):
        return f"{self.rank} {self.full_name}"
    
class Vacancy(models.Model):
    military_unit = models.CharField("Районное подразделение", max_length=200, blank=True)
    title = models.CharField("Должность", max_length=200)
    rank = models.CharField("Звание", max_length=100, blank=True)
    salary_from = models.PositiveIntegerField("Денежное довольствие от, руб.")
    salary_to = models.PositiveIntegerField("Денежное довольствие до, руб.", blank=True, null=True)
    requirements = models.TextField("Требования")
    duties = models.TextField("Обязанности", blank=True)
    benefits = models.TextField("Льготы и гарантии", blank=True)
    contact_phone = models.CharField("Телефон для связи по вакансии", max_length=30, blank=True)
    is_published = models.BooleanField("Опубликовано", default=True)
    sort_order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Вакансия (контракт)"
        verbose_name_plural = "Вакансии на контракт"
        ordering = ['sort_order']

    def __str__(self):
        return self.title