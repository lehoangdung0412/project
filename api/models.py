from django.db import models


class Customer(models.Model):
    fullname = models.CharField(max_length=50)
    DOB = models.DateField()
    address_id = models.ForeignKey('Address', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_lenght=20)
    image = models.ImageField()
    registered = models.BooleanField()
    facebook = models.CharField(max_length=50, null=True, blank=True)
    google = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class City(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class District(models.Model):
    city_id = models.ForeignKey('City', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class Ward(models.Model):
    district_id = models.ForeignKey('District', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class Address(models.Model):
    street = models.CharField(max_length=100)
    ward_id = models.ForeignKey('Ward', on_delete=models.CASCADE)
    district_id = models.ForeignKey('District', on_delete=models.CASCADE)
    city_id = models.ForeignKey('City', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class Supplier(models.Model):
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    supplier_id = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    favourite = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class COD(models.Model):
    customer_id = models.ForeignKey(on_delete=models.CASCADE)
    description = models.TextField()
    note = models.TextField()


class MasterCard(models.Model):
    cardID = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    date_expired = models.DateField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class ATMCard(models.Model):
    bank = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    cardID = models.CharField(max_length=50)
    date_expired = models.DateField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    description = models.TextField()
    COD_id = models.ForeignKey('COD', on_delete=models.CASCADE)
    mastercard_id = models.ForeignKey('MasterCard', on_delete=models.CASCADE)
    atmCard_id = models.ForeignKey('ATMCard', on_delete=models.CASCADE)


class Shipper(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class Delivery(models.Model):
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    payment_id = models.ForeignKey('Payment', on_delete=models.CASCADE)
    shipper_id = models.ForeignKey('Shipper', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    payment_id = models.ForeignKey('Payment', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    delivery_id = models.ForeignKey('Delivery', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=9, decimal_places=0)
    total = models.DecimalField(max_digits=9, decimal_places=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=9, decimal_places=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)


# class Branch(models.Model):
#     name = models.CharField(max_length=100)
#     time_work = models.DateTimeField()
#     address = models.CharField(max_length=255)
#     image = models.CharField(max_length=255)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now_add=True)


# class History(models.Model):
#     product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
#     branch_id = models.ForeignKey('Branch', on_delete=models.CASCADE)
#     payment_id = models.ForeignKey('Payment', on_delete=models.CASCADE)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now_add=True)


# class Comment(models.Model):
#     product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
#     branch_id = models.ForeignKey('Branch', on_delete=models.CASCADE)
#     comment = models.TextField()
#     updated_date = models.DateTimeField(auto_now_add=True)
#     created_date = models.DateTimeField(auto_now_add=True)
