from django.shortcuts import render
from django.http import  HttpResponse
from .models import (
    HeaderText, 
    FooterText,
    MiniBlocks, 
    TreeBlocks,
    TestimonialMain,
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
        "furniture": Furniture.objects.all().first(),
        "mini_blocks": MiniBlocks.objects.all(),
        "blog": Blog.objects.all().first(),
        "tree_blocks": TreeBlocks.objects.all(),
        "testimonial_main": TestimonialMain.objects.all().first(),
        "testimonial": Testimonial.objects.all(),
        "contact": Contact.objects.all().first(),
        "info_section": InfoSection.objects.all().first(),
        "socials": Socials.objects.all()
    }

    return render(request, "home.html", context)


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
        "blog": Blog.objects.all().first(),
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



