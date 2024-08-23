from django.db import models

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
    price = models.FloatField() 
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
