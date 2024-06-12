from django.db import models

class personaldetails(models.Model):
    personal_details_state1 = models.CharField(max_length=100)
    personal_details_product1 = models.CharField(max_length=100)
    personal_details_config = models.CharField(max_length=100, blank=True, null=True)
    personal_details_aadhar = models.CharField(max_length=12)
    personal_details_farmerName1 = models.CharField(max_length=100)
    personal_details_guardian = models.CharField(max_length=100)
    personal_details_age = models.PositiveIntegerField()
    personal_details_number1 = models.CharField(max_length=10)
    personal_details_gender = models.CharField(max_length=10)
    personal_details_caste = models.CharField(max_length=100)
    personal_details_resState1 = models.CharField(max_length=100)
    personal_details_district = models.CharField(max_length=100)
    personal_details_block1 = models.CharField(max_length=100)
    personal_details_grampanch = models.CharField(max_length=100)
    personal_details_village = models.CharField(max_length=100)
    personal_details_h_no = models.CharField(max_length=100)
    personal_details_pin = models.CharField(max_length=6)
    personal_details_category1 = models.CharField(max_length=100)
    personal_details_nature1 = models.CharField(max_length=100)
    personal_details_mandi = models.CharField(max_length=100, blank=True, null=True)
    personal_details_invoice = models.CharField(max_length=100, blank=True, null=True)
    personal_details_retailstore1 = models.CharField(max_length=100, blank=True, null=True)
    personal_details_bankname = models.CharField(max_length=100)
    personal_details_branchname = models.CharField(max_length=100)
    personal_details_ifsc1 = models.CharField(max_length=11)
    personal_details_account_no = models.CharField(max_length=18)
    personal_details_nominee_name = models.CharField(max_length=100)
    personal_details_nominee_relation = models.CharField(max_length=100)
    personal_details_nominee_age = models.PositiveIntegerField()

    def __str__(self):
        return self.personal_details_state1
    
    def get_caste(self):
        return self.personal_details_caste

