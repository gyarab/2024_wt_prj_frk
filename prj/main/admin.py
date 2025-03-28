from django.contrib import admin
from .models import GPU

class GPUAdmin(admin.ModelAdmin):
    list_display = ["name", "generation", "Vram_amount_GB", "release_year", "price_USD", "graphics_processor"]

admin.site.register(GPU, GPUAdmin)