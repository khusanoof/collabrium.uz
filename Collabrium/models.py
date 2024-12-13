from django.db import models
from ckeditor.fields import RichTextField

#1
from django.utils.translation import gettext_lazy as _

class Space(models.Model):
    space = models.CharField(max_length=300)
    page_slug = models.SlugField(unique=True) 
    image = models.ImageField(upload_to='Images/space')
    class Meta:
        verbose_name = _("Space")
        verbose_name_plural = _("Spaces")

    def __str__(self):
        return f"{self.space}"
    

#2
class Faq(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    page_slug = models.SlugField()

    class Meta:
        verbose_name = _("Faq")
        verbose_name_plural = _("Faqs")
    
    def __str__(self):
        return f"{self.title}"
    

#3
class Blog(models.Model):
    image_cover = models.ImageField(upload_to='blog_images', verbose_name="Обложка изображения")
    date = models.DateField(auto_now_add=True, verbose_name="Дата публикации")
    title = models.CharField(max_length=255, verbose_name="Заголовок статьи")
    page_slug = models.SlugField(unique=True, verbose_name="Слаг страницы")
    main_title = models.CharField(max_length=200, verbose_name="Основной заголовок")
    text_first = RichTextField(verbose_name="Текст 1")
    text_second = RichTextField(verbose_name="Текст 2")
    image_first = models.ImageField(upload_to='blog_images', blank=True, null=True, verbose_name="Первое изображение")
    image_second = models.ImageField(upload_to='blog_images', blank=True, null=True, verbose_name="Второе изображение")

    def __str__(self):
        return self.title

#4
class OurTeam(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='OurTeam_images')
    job = models.CharField(max_length=200)
    description = models.TextField()
    class Meta:
        verbose_name = _("OurTeam")
        verbose_name_plural = _("OurTeams")

    def __str__(self):
        return f"{self.name}"


#5
class Rezident(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='rezident_images')
    job = models.CharField(max_length=200)
    description = models.TextField()
    class Meta:
        verbose_name = _("Rezident")
        verbose_name_plural = _("Rezidents")

    def __str__(self):
        return f"{self.name}"



