from django.contrib import admin


from .models import (
    HeaderText, 
    FooterText, 
    MiniBlocks,
    TreeBlocks,
    Testimonial
)    


admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register( MiniBlocks)
admin.site.register( TreeBlocks)
admin.site.register( Testimonial)
