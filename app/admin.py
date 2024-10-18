from django.contrib import admin


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


admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register( MiniBlocks)
admin.site.register( TreeBlocks)
admin.site.register( Testimonial)
admin.site.register( About)
admin.site.register( Furniture)
admin.site.register( Blog)
admin.site.register( Contact)
admin.site.register( InfoSection)
admin.site.register( Socials)
