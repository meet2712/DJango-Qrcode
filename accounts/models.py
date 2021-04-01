from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Fruits', 'Fruits'),
        ('Vegetables', 'Vegetables'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('reached to sorting enter', 'reached to sorting enter'),
        ('to quality check center', 'to quality check center'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return str(self.product)


class AccountsProduct(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_product'



class AccountsCustomer(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_customer'



class AccountsOrder(models.Model):
    date_created = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    customer = models.ForeignKey(AccountsCustomer, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('AccountsProduct', models.DO_NOTHING, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_order'


# class contactdetails(models.Model):
#     full_name = models.CharField(max_length=200, blank=True, null=True)
#     phone = models.CharField(max_length=200, blank=True, null=True)
#     email = models.CharField(max_length=200, blank=True, null=True)
#     message = models.CharField(max_length=1000, blank=True, null=True)
#
#     def __str__(self):
#         return self.full_name.name
#
#     class Meta:
#         managed = False
#         db_table = 'contact_details'
