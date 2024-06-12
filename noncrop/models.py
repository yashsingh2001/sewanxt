from django.db import models

class Noncrop(models.Model):
    noncrop_typeofrisk = models.CharField(max_length=100)
    noncrop_gender = models.CharField(max_length=10)
    noncrop_ageyears = models.IntegerField()
    noncrop_agemonths = models.IntegerField()
    noncrop_breed = models.CharField(max_length=100)
    noncrop_vaccination = models.BooleanField(null=True, blank=True)
    noncrop_hypothecated = models.BooleanField(null=True, blank=True, default=False)
    noncrop_taggingdate = models.DateField()
    noncrop_suminsured = models.DecimalField(max_digits=10, decimal_places=2)
    noncrop_marketvalue = models.DecimalField(max_digits=10, decimal_places=2)
    noncrop_pregnancystatus = models.CharField(max_length=100)
    noncrop_calvingcycle = models.CharField(max_length=100)
    noncrop_animalcolor = models.CharField(max_length=50) 
    noncrop_tailswitchcolour = models.CharField(max_length=50)
    noncrop_lefthornshape = models.CharField(max_length=50)
    noncrop_righthornshape = models.CharField(max_length=50)

    def __str__(self):
        return self.noncrop_typeofrisk