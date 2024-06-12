from django.contrib import admin
from homepage.models import Homepage

class HomepageAdmin(admin.ModelAdmin):
    list_display = ('homepage_username', 'homepage_password')

admin.site.register(Homepage, HomepageAdmin)