from django.db import models

# Create your models here.

class Header(models.Model):

    title = models.CharField('Title', max_length=50)
    colored_title = models.CharField('Colored Title', max_length=50)
    path1 = models.CharField('Path 1', max_length=50)
    path2 = models.CharField('Path 2', max_length=50)
    path3 = models.CharField('Path 3', max_length=50)
    path4 = models.CharField('Path 4', max_length=50)
    path5 = models.CharField('Path 5', max_length=50)

    class Meta:

        verbose_name = 'Header'
        verbose_name_plural = 'Header'

class Footer(models.Model):

    text = models.TextField('Copyright')
    name = models.CharField('Name', max_length=50)
    name_link = models.CharField('Name Link', max_length=50)

    class Meta:

        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'