from django.contrib import admin
from .models import GPU

class GPUAdmin(admin.ModelAdmin):
    list_display = ["name", "generation", "Vram_amount", "release_date", "price"]

admin.site.register(GPU, GPUAdmin)