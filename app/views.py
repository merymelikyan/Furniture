from django.shortcuts import render
from django.http import  HttpResponse
from .models import (
    HeaderText, 
    FooterText,
    MiniBlocks, 
    TreeBlocks,
    Testimonial,
    About,
    Furniture,
    Blog,
    Contact,
    InfoSection,
    Socials
)

def index(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "about": About.objects.all().first(),
        "mini_blocks": MiniBlocks.objects.all(),
        "tree_blocks": TreeBlocks.objects.all(),
        "testimonial": Testimonial.objects.all(),
        "info_section": InfoSection.objects.all(),
        "socials": Socials.objects.all()
    }

    return render(request, "home.html", context)

def single_blog(request, blog_id):
    #id = Blog.objects.get(pk=blog_id)
    blog = Blog.objects.get(id=blog_id)

    print(blog)
    print(id)
    return render(request, "single_blog.html", {
        "id": id,
        "blog": blog
    })
        


def about(request):
    context = {
        "about": About.objects.all().first(),
        "mini_blocks": MiniBlocks.objects.all(),
        "tree_blocks": TreeBlocks.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "socials": Socials.objects.all(),
        "info_section": InfoSection.objects.all().first(),
    }

    return render(request, "about.html", context)


def furniture(request):
    context = {
        "furniture": Furniture.objects.all().first(),
        "mini_blocks": MiniBlocks.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "socials": Socials.objects.all(),
    }

    return render(request, "furniture.html", context)


def blog(request):
    context = {
        "blog": Blog.objects.all(),
        "tree_blocks": TreeBlocks.objects.all(),
        "mini_blocks": MiniBlocks.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "socials": Socials.objects.all(),
        "info_section": InfoSection.objects.all().first(),
    }

    return render(request, "blog.html", context)


def contact(request):
    context = {
        "contact": Contact.objects.all().first(),
        "mini_blocks": MiniBlocks.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "socials": Socials.objects.all(),
        "info_section": InfoSection.objects.all().first(),
    }

    return render(request, "contact.html", context)



