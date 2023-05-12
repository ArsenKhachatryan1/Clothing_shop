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

class AboutPage(models.Model):

    img1 = models.ImageField('Background Image', upload_to='images')
    general_title = models.CharField('General Title 1', max_length=50)
    general_subtitle = models.CharField('Subtitle', max_length=60)
    title1 = models.CharField('Title 1', max_length=50)
    img2 = models.ImageField('Image 1', upload_to='images')
    subtitle = models.CharField('Subtitle', max_length=60)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    social1 = models.CharField('Social 1', max_length=50)
    social2 = models.CharField('Social 2', max_length=50)
    social3 = models.CharField('Social 3', max_length=50)
    social4 = models.CharField('Social 4', max_length=50)
    social_url1 = models.URLField('Social Url 1')
    social_url2 = models.URLField('Social Url 2')
    social_url3 = models.URLField('Social Url 3')
    social_url4 = models.URLField('Social Url 4')
    title2 = models.CharField('Title 2', max_length=50)
    img3 = models.ImageField('Image 2', upload_to='images')
    title3 = models.CharField('Title 3', max_length=50)


    class Meta:

        verbose_name = 'About Page'
        verbose_name_plural = 'About Page'

class Team(models.Model):

    img = models.ImageField('Image', upload_to='images')
    social1 = models.CharField('Social 1', max_length=50)
    social2 = models.CharField('Social 2', max_length=50)
    social3 = models.CharField('Social 3', max_length=50)
    social4 = models.CharField('Social 4', max_length=50)
    social_url1 = models.URLField('Social Url 1')
    social_url2 = models.URLField('Social Url 2')
    social_url3 = models.URLField('Social Url 3')
    social_url4 = models.URLField('Social Url 4')
    title = models.CharField('Name', max_length=50)
    subtitle = models.CharField('Profession', max_length=50)
    text = models.TextField('Info')

class AboutContent(models.Model):

    title = models.CharField('Title', max_length=50)
    text = models.TextField('Text')
    btn_name = models.CharField('Button Name', max_length=40)

class Partner(models.Model):
    
    img = models.ImageField('Logo Image', upload_to='images')

class Contact(models.Model):

    img = models.ImageField('Background Image', upload_to='images')
    general_title = models.CharField('General Title', max_length=50)
    general_subtitle = models.CharField('Subtitle', max_length=60)
    title1 = models.CharField('Title 1', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=60)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    social1 = models.CharField('Social 1', max_length=50)
    social2 = models.CharField('Social 2', max_length=50)
    social3 = models.CharField('Social 3', max_length=50)
    social4 = models.CharField('Social 4', max_length=50)
    social_url1 = models.URLField('Social Url 1')
    social_url2 = models.URLField('Social Url 2')
    social_url3 = models.URLField('Social Url 3')
    social_url4 = models.URLField('Social Url 4')
    title2 = models.CharField('Title 2', max_length=50)
    btn_name = models.CharField('Button Name', max_length=40)
    title3 = models.CharField('Title 3', max_length=50)
    inp1 = models.CharField('Placeholder 1', max_length=50)
    inp2 = models.CharField('Placeholder 2', max_length=50)
    inp3 = models.CharField('Placeholder 3', max_length=50)
    inp4 = models.CharField('Placeholder 4', max_length=50)

    class Meta:

        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

class ContactInfo(models.Model):

    title = models.CharField('Title', max_length=60)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')

    def __str__(self) -> str:
        return self.title

class ContactPost(models.Model):

    user_name = models.CharField('Username', max_length=60)
    user_email = models.EmailField('Email')
    subject = models.CharField('Subject', max_length=100)
    message = models.TextField('Message')

    class Meta:

        verbose_name = 'Contact POST'
        verbose_name_plural = 'Contact POST'

    def __str__(self) -> str:
        return self.user_name
    
class Customer(models.Model):

    img = models.ImageField('Image', upload_to='images')


class ProductTitle(models.Model):

    title = models.CharField('Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=50)
    img = models.ImageField('Image', upload_to='images')

class ProductCategory(models.Model):

    name = models.CharField('Category Name', max_length=50)

    class Meta:

        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def __str__(self) -> str:
        return self.name

class Product(models.Model):

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='cat_prod')
    img = models.ImageField('Name', upload_to='images')
    name = models.CharField('Name', max_length=50)
    text = models.TextField('Text')
    price = models.CharField('Price', max_length=50)


