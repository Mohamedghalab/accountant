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
    importer_number = models.PositiveIntegerField(verbose_name='رقم المورد', default=0)
    company = models.ForeignKey(Company, verbose_name='الشركه', on_delete=models.CASCADE, related_name='importers')
    name = models.CharField(verbose_name='اسم المورد', max_length=200)
    phone = PhoneNumberField(verbose_name='موبايل')
    countBuyMony = models.DecimalField(verbose_name='مجموع المبالع المشترى من المورد', max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    category_number = models.PositiveIntegerField(verbose_name='رقم الصنف', default=0)
    importer = models.ForeignKey(Importer, on_delete=models.CASCADE, related_name='categories')
    nameAr = models.CharField(verbose_name='اسم الصنف بالعربيه', max_length=100)
    nameEn = models.CharField(verbose_name='اسم الصنف بالانجليزيه', max_length=100)
    price = models.DecimalField(verbose_name="السعر", max_digits=7, decimal_places=2)
    date = models.DateTimeField(verbose_name='تاريخ الانتاج')

    def __str__(self):
        return self.Ar


class Price(models.Model):
    cstName = models.CharField(verbose_name='اسم العميل', max_length=200)
    taxNumber = models.PositiveIntegerField(verbose_name="الرقم الضريبى")
    priceDate = models.DateTimeField(verbose_name="تاريخ التسعيره")
    category = models.ForeignKey(Category, verbose_name="اسم الصنف", on_delete=models.CASCADE, related_name='prices')
    countty = models.DecimalField(verbose_name='الكميه', max_digits=10, decimal_places=2)
    unitPrice = models.DecimalField(verbose_name='سعر الوحده', max_digits=7, decimal_places=2)
    totalPrice = models.DecimalField(verbose_name='السعر الاجمالى', max_digits=10, decimal_places=2)
    price = models.CharField(max_length=50, verbose_name='مبلغ التسعيره')
    discount = models.FloatField(verbose_name='الخصم')
    afterDiscount = models.DecimalField(verbose_name='بعد الخصم', decimal_places=2, max_digits=10)
    finalPrice = models.DecimalField(verbose_name='المجموع النهائى', decimal_places=2, max_digits=10)
    
    def __str__(self):
        return self.cstName


class Customer(models.Model):
    customer_number = models.PositiveIntegerField(verbose_name='رقم العميل', default=0)
    name = models.CharField(verbose_name='اسم العميل', max_length=100)
    phone = PhoneNumberField(verbose_name='رقم الهاتف')
    total_paid = models.DecimalField(verbose_name='مجموع المبالغ المدفوعه', max_digits=10, decimal_places=2)
    remaining_amounts = models.DecimalField(verbose_name='مجموع المبالغ المتبقيه', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    
class Invoice(models.Model):
    invoice_number = models.PositiveIntegerField(verbose_name='رقم الفاتورة', default=0)
    name = models.CharField(verbose_name="اسم العميل", max_length=50)    
    taxNumber = models.PositiveIntegerField(verbose_name="الرقم الضريبى")
    priceDate = models.DateTimeField(verbose_name="تاريخ الفاتورة")
    price = models.ForeignKey(Price, verbose_name='التسعيره', on_delete=models.CASCADE, related_name='invoices')
    category = models.ForeignKey(Category, verbose_name="اسم الصنف", on_delete=models.CASCADE, related_name='invoices')
    countty = models.DecimalField(verbose_name='الكميه', max_digits=10, decimal_places=2)
    unitPrice = models.DecimalField(verbose_name='سعر الوحده', max_digits=7, decimal_places=2)
    totalPrice = models.DecimalField(verbose_name='السعر الاجمالى', max_digits=10, decimal_places=2)
    price = models.CharField(max_length=50, verbose_name='مبلغ الفاتورة')
    discount = models.FloatField(verbose_name='الخصم')
    afterDiscount = models.DecimalField(verbose_name='المبلغ بعد الخصم', decimal_places=2, max_digits=10)
    finalPrice = models.DecimalField(verbose_name='المجموع النهائى', decimal_places=2, max_digits=10)
    
    def __str__(self):
        return self.name
    