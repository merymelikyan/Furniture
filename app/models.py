from django.db import models
from django.utils import timezone

class HeaderText(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Header Text"
        verbose_name_plural = "Header Text"


class FooterText(models.Model):
    text = models.CharField(max_length=255)
        
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text"



class MiniBlocks(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.ImageField(upload_to="mini-blocks")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mini Block"
        verbose_name_plural = "Mini Blocks"


class TreeBlocks(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="tree-blocks")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tree Block"
        verbose_name_plural = "Tree Blocks"


class Testimonial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="testimonial")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = " Testimonial"
        verbose_name_plural = " Testimonial"



class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="about", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"   
        

class Blog(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"       



class Furniture(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Furniture"
        verbose_name_plural = "Furnitures"       



class Contact(models.Model):
    title = models.CharField(max_length=255)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"       

 

class InfoSection(models.Model):
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    phone_class = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    email_class = models.CharField(max_length=255)
    location_class = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Info Section"
        verbose_name_plural = "Info Sections"  
 

class Socials(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=255, blank=True)
    html_class = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"

               