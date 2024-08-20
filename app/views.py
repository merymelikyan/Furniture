from django.shortcuts import render
from django.http import  HttpResponse
from .models import (
    HeaderText, 
    FooterText, 
    MiniBlocks
)

def index(request):
    context = {
        "header_text": HeaderText.objects.all(),
        "footer_text": FooterText.objects.all().first(),
        "mini_blocks": MiniBlocks.objects.all()
    }

    return render(request, "base.html", context)

