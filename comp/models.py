from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    name  = models.CharField(verbose_name="اسم الشركه", max_length=100)
    phone = PhoneNumberField(verbose_name=' الهاتف الارضى')
    mobile = PhoneNumberField(verbose_name='موبايل')
    document1 = models.IntegerField(verbose_name='رقم السجل التجارى')
    document2 = models.IntegerField(verbose_name='الرقم الضريبى')
    address1 = models.CharField(verbose_name='العنوان1', max_length=200)
    address2 = models.CharField(verbose_name='العنوان2', max_length=200)

    def __str__(self):
        return self.name


class Importer(models.Model):
    company = models.ForeignKey(Company, verbose_name='الشركه', on_delete=models.CASCADE, related_name='importers')
    name = models.CharField(verbose_name='اسم المورد', max_length=200)
    phone = PhoneNumberField(verbose_name='موبايل')
    countBuyMony = models.DecimalField(verbose_name='مجموع المبالع المشترى من المورد', max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    

