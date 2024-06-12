from django.contrib import admin

# Register your models here.


from noncrop.models import Noncrop

class noncropAdmin(admin.ModelAdmin):
    list_display = ('noncrop_typeofrisk', 'noncrop_gender','noncrop_ageyears','noncrop_agemonths','noncrop_breed','noncrop_vaccination','noncrop_hypothecated','noncrop_taggingdate','noncrop_suminsured','noncrop_marketvalue','noncrop_pregnancystatus','noncrop_calvingcycle','noncrop_animalcolor','noncrop_tailswitchcolour','noncrop_lefthornshape','noncrop_righthornshape')

admin.site.register(Noncrop, noncropAdmin)