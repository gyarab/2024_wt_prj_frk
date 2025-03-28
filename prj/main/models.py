from django.db import models

class GPU(models.Model):
    name = models.CharField(max_length=30, default="")
    generation = models.CharField(max_length=4, default="")
    Vram_amount_GB = models.CharField(max_length=20, default="")
    release_year = models.IntegerField(null=False, blank=False, default="")
    price_USD = models.IntegerField(null=False, blank=False, default="")
    graphics_processor = models.CharField(max_length=10, default="")


def __str__(self):
    return f"{self.name} {self.generation} {self.Vram_amount_GB} {self.release_year} {self.price_USD} {self. graphics_processor} "