from django.db import models

class GPU(models.Model):
    name = models.IntegerField(max_length=100, default="")
    generation = models.CharField(max_length=4, default="")
    Vram_amount = models.IntegerField(blank=True, null=True, default="")
    release_date = models.DateField(max_length=20, default="")
    price = models.IntegerField(null=False, blank=False, default="")

def _str_(self):
    return f"{self.name} {self.generation} {self.Vram_amount} {self.release_date} {self.price} "