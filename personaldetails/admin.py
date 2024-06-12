from django.contrib import admin

from personaldetails.models import personaldetails

class PersonaldetailsAdmin(admin.ModelAdmin):
    list_display = ( 
                    #    'personal_details_State1', 
                    #    'personal_details_Product1', 
                    #    'personal_details_Config',
                       'personal_details_aadhar',
                    #    'personal_details_FarmerName1',
                       'personal_details_guardian',
                       'personal_details_age',
                       'personal_details_number1',
                       'personal_details_gender',
                       'personal_details_caste',
                       'personal_details_resState1',
                       'personal_details_district',
                       'personal_details_block1',
                       'personal_details_grampanch',
                       'personal_details_village',
                       'personal_details_h_no',
                       'personal_details_pin',
                       'personal_details_category1',
                       'personal_details_nature1',
                       'personal_details_mandi',
                       'personal_details_invoice',
                       'personal_details_retailstore1',
                       'personal_details_bankname',
                       'personal_details_branchname',
                       'personal_details_ifsc1',
                       'personal_details_account_no',
                       'personal_details_nominee_name',
                       'personal_details_nominee_relation',
                       'personal_details_nominee_age',
                      
       )

admin.site.register(personaldetails, PersonaldetailsAdmin)    # list_display = ('farmerName1', 'state1', 'product1', 'aadhar', 'number1', 'bankname', 'account_no')
# search_fields = ('farmerName1', 'aadhar', 'number1')
# list_filter = ('state1', 'product1')