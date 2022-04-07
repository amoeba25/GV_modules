from django.db import models
from django.core.validators import MaxValueValidator
import uuid

class Order(models.Model):
    cust_id = models.UUIDField(primary_key= True, default=uuid.uuid4, editable= False)
    cust_type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.IntegerField(validators=[MaxValueValidator(9999999999)]) # max cap for phone number length
    billing_add = models.CharField(max_length=200)
    shipping_add = models.CharField(max_length=200)
    reference_form = models.CharField(max_length=50)
    gst_no = models.CharField(max_length=15) #gst number is 15 digit
    payment_term = models.IntegerField(validators=[MaxValueValidator(100)])
    delivery_term = models.IntegerField(validators=[MaxValueValidator(100)])
    comments = models.CharField(max_length=500)
    
    class Meta:
        db_table = 'orders'
