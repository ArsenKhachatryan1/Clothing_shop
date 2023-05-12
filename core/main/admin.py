from django.contrib import admin
from .models import Header, Footer
from .models import AboutPage, Team, AboutContent, Partner
from .models import ProductTitle, ProductCategory, Product
from .models import Contact, ContactInfo, ContactPost, Customer
# Register your models here.

admin.site.register(Header)
admin.site.register(Footer)



admin.site.register(AboutPage)
admin.site.register(Team)
admin.site.register(AboutContent)
admin.site.register(Partner)
admin.site.register(ProductTitle)

admin.site.register(Contact)
admin.site.register(ContactInfo)
admin.site.register(ContactPost)
admin.site.register(Customer)
admin.site.register(ProductCategory)
admin.site.register(Product)