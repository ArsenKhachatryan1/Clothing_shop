from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Header, Footer
from .models import AboutPage, Team, AboutContent, Partner
from .models import ProductTitle, ProductCategory
from .models import Contact, ContactInfo, ContactPost, Customer
from .forms import ContactModelForm

# Create your views here.

def double_content():
    header_content = Header.objects.all()[0]
    footer_content = Footer.objects.all()[0]
    return [header_content, footer_content]

def index(request):
    return render(request, 'main/index.html', context={
        'link':'index',
        'header_content':double_content()[0],
        'footer_content':double_content()[1],
    })
    
def products(request):
    product_title = ProductTitle.objects.all()[0]
    product_category = ProductCategory.objects.all()
    
    return render(request, 'main/products.html', context={
        'link':'products',
        'header_content':double_content()[0],
        'footer_content':double_content()[1],
        'product_title':product_title,
        'product_category':product_category,
    })

def about(request):
    about_page = AboutPage.objects.all()[0]
    team_content = Team.objects.all()
    about_content = AboutContent.objects.all()
    partners = Partner.objects.all()
    return render(request, 'main/about.html', context={
        'link':'about',
        'header_content':double_content()[0],
        'footer_content':double_content()[1],
        'about_page':about_page,
        'team_content':team_content,
        'about_content':about_content,
        'partners':partners,
    })

def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            ContactPost.objects.create(**form.cleaned_data)
            return redirect('contact')
    else:
        form = ContactModelForm()

    contact_get = Contact.objects.all()[0]
    contact_info = ContactInfo.objects.all()
    customers = Customer.objects.all()
    return render(request, 'main/contact.html', context={
        'link':'contact',
        'header_content':double_content()[0],
        'footer_content':double_content()[1],
        'contact_get':contact_get,
        'contact_info':contact_info,
        'customers':customers,
    })


def index_detail(request, id):
    product_title = ProductTitle.objects.all()[0]
    product_category = ProductCategory.objects.all()
    prod_list = ProductCategory.objects.filter(pk=id)
    
    return render(request, 'main/index_detail.html', context={
        'link':'products',
        'header_content':double_content()[0],
        'footer_content':double_content()[1],
        'product_title':product_title,
        'product_category':product_category,
	    'prod_list':prod_list,
    })




