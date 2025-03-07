from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('one', TemplateView.as_view(template_name='main/one.html')),
    path('two', TemplateView.as_view(template_name='main/two.html')),
]
