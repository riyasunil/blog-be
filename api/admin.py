from django.contrib import admin

from .models import Blog
from .forms import BlogAdminForm
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
admin.site.register(Blog,BlogAdmin)
