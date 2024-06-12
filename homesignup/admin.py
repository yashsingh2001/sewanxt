from django.contrib import admin

# Register your models here.


from homesignup.models import Homesignup

class HomesignupAdmin(admin.ModelAdmin):
    list_display = ('homesignup_username', 'homesignup_password','homesignup_email')  # Update field names here

admin.site.register(Homesignup, HomesignupAdmin)