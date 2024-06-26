from django.db import models

# Create your models here.
class states(models.Model):
    stateid = models.AutoField(primary_key=True)
    statename = models.CharField(max_length=50)
    
    def __str__(self):
        return self.statename

class district(models.Model):
    districtid = models.AutoField(primary_key=True)
    state = models.IntegerField(blank=True, null=True)  
    districtname = models.CharField(max_length=100)
    
    def __str__(self):
        return self.districtname 
    
class locations(models.Model):
    locationid = models.AutoField(primary_key=True)
    state = models.IntegerField(blank=True, null=True)  
    district = models.IntegerField(blank=True, null=True) 
    locationname = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.locationname 
    
class category(models.Model):
    categoryid = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    category_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.category_name

class sub_category(models.Model):
    sub_categoryid = models.AutoField(primary_key=True)
    category = models.ForeignKey(category, related_name='subcategories', on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=50)
    subcategory_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.subcategory_name

class product(models.Model):
    productid = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True, blank=True)
    sub_category = models.ForeignKey(sub_category, on_delete=models.CASCADE, null=True, blank=True)
    product_rate = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    productimage_1 = models.ImageField(upload_to='images/')
    productimage_2 = models.ImageField(upload_to='images/')
    productimage_3 = models.ImageField(upload_to='images/')
    description = models.TextField()
    product_status = models.CharField(max_length=100)
    registered_date = models.DateField()

    def __str__(self):
        return self.productname

class cusregform(models.Model):
    customerid = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)   
    email_id = models.CharField(max_length=50) 
    contact_no = models.CharField(max_length=50)    
    state= models.CharField(max_length=100) 
    district= models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    address= models.TextField()
    username = models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    
    def __str__(self):
        return self.customer_name
    
class cusdesign(models.Model):
    design_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField(blank=True, null=True) 
    category = models.CharField(max_length=100)   
    model_image = models.ImageField(upload_to='images/') 
    description = models.TextField()    
    name= models.CharField(max_length=100) 
    email_id= models.CharField(max_length=100)
    contact_number= models.CharField(max_length=100)
    address= models.TextField()
    
class admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_username = models.CharField(max_length=100)  
    admin_password = models.CharField(max_length=100)
    
    
# class contact(models.Model):
#     contact_id = models.AutoField(primary_key=True)  
#     name= models.CharField(max_length=100) 
#     email_id= models.CharField(max_length=100)
#     subject= models.CharField(max_length=100)
#     message= models.TextField()
    
class cart(models.Model):
    cart_id = models.AutoField(primary_key=True)  
    customer_id= models.IntegerField(blank=True, null=True) 
    product = models.IntegerField(blank=True, null=True) 
    quantity= models.IntegerField(blank=True, null=True) 
    price= models.BigIntegerField(blank=True, null=True) 
    cart_status= models.CharField(max_length=100)  
    cart_date= models.DateField() 
    
class billing_address(models.Model):  
    billing_address_id = models.AutoField(primary_key=True)   
    customer_id= models.IntegerField(blank=True, null=True)  
    full_name = models.CharField(max_length=100) 
    email_id= models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    street= models.CharField(max_length=100)
    landmark= models.CharField(max_length=100) 
    pincode= models.BigIntegerField(blank=True, null=True)  
    city= models.CharField(max_length=100) 
    state=  models.IntegerField(blank=True, null=True)  
    
class order_master(models.Model):
    order_master_id = models.AutoField(primary_key=True) 
    customer_id = models.IntegerField(blank=True, null=True)   
    order_date= models.DateField() 
    total_amount = models.BigIntegerField(blank=True, null=True)  
    order_status = models.CharField(max_length=100) 
    payment_method = models.CharField((""), max_length=50)
    
class order_detail(models.Model):
    order_detail_id = models.AutoField(primary_key=True)
    bill_no= models.BigIntegerField(blank=True, null=True) 
    customer_id = models.IntegerField(blank=True, null=True) 
    product_id = models.IntegerField(blank=True, null=True) 
    product_price = models.BigIntegerField(blank=True, null=True) 
    quantity= models.IntegerField(blank=True, null=True) 
    order_date= models.DateField()  
    order_status = models.CharField(max_length=100)    
    payment_method = models.CharField((""), max_length=50)    
  
class payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    bill_no= models.BigIntegerField(blank=True, null=True) 
    card_no= models.BigIntegerField(blank=True, null=True) 
    total_amount = models.BigIntegerField(blank=True, null=True) 
    paid_date= models.DateField() 
    paid_status = models.CharField(max_length=100)   
    



    