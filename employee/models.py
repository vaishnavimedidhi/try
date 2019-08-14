from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length =200 , null =True)
    description =models.CharField(max_length=300 , null =True)
    
class emp(models.Model):
    name = models.CharField(max_length =200, null =True)
    designation = models.CharField(max_length =200, null =True)
    #emp_dept = models.ForeignKey(department , on_delete =models.CASCADE ,default="not specified")
    email= models.EmailField( null =True)
    join_date = models.DateField( null =True)
    dob = models.DateField( null =True)
    address = models.CharField(max_length= 200, null =True)
    user =models.OneToOneField(User, on_delete=models.CASCADE , null =True)
    

class phone_no(models.Model):
    emp_id= models.ForeignKey(emp , on_delete = models.CASCADE, null =True)
    phone_no =models.BigIntegerField( null =True)

    class Meta:
        unique_together=("emp_id" , "phone_no")

class field(models.Model):
    name=models.CharField(max_length= 200, null =True)
    dept_name=models.ForeignKey(department , on_delete=models.CASCADE , null =True)
    descrition=models.CharField(max_length= 200, null =True)

    class Meta:
        unique_together=("name","dept_name")

class project(models.Model):
    name = models.CharField(max_length=200, null =True)
    status_choice=(
        ('active' ,'active'),
        ('inactive' , 'inactive'),
        ('review' , 'review'),
        ('close' , 'close')
    )
    status=models.CharField(max_length= 200 ,choices= status_choice , null =True)
    deadline=models.DateField(null =True)
    field=models.ForeignKey(field ,on_delete= models.CASCADE , null =True )

class client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length =200, null =True)
    company = models.CharField(max_length = 200, null =True)
    proj_id = models.ForeignKey(project , on_delete=models.CASCADE, null =True)
    email = models.EmailField(null =True)

class client_phone(models.Model):
    client_id = models.ForeignKey(client , on_delete=models.CASCADE, null =True)
    phone_no = models.BigIntegerField(null =True)

    class Meta:
        unique_together=("client_id", "phone_no")

class promotions(models.Model):
    designation=models.CharField(max_length = 200, null =True)
    emp_id= models.ForeignKey(emp, on_delete=models.CASCADE, null =True)
    promoted_date = models.DateField( null =True)

    class Meta:
        unique_together=("designation" , "emp_id","promoted_date")


class accomplishment(models.Model):
    name = models.CharField(max_length = 200 , null =True)
    date = models.DateField(null =True)
    highlights = models.CharField(max_length =200, null =True)
    cashprice = models.FloatField(null =True)

    class Meta:
        unique_together= ("name" , "date" )

class accomplished_by(models.Model):
    name = models.CharField(max_length = 200, null =True) 
    date    = models.DateField(null =True)
    emp_id = models.ForeignKey(emp, on_delete=models.CASCADE, null =True)

    class Meta:
        unique_together =("name" , "emp_id")

class dashboard(models.Model):
    proj_id = models.ForeignKey(project, on_delete=models.CASCADE, null =True)
    emp_id = models.ForeignKey(emp, on_delete=models.CASCADE, null =True)
    function = models.CharField(max_length= 200, null =True)

    class Meta:
        unique_together=("proj_id","emp_id")

class leave(models.Model):
    emp_id = models.ForeignKey(emp, on_delete=models.CASCADE, null =True)
    date   = models.DateField( null =True)
    reason = models.CharField(max_length = 200, null =True)

    class Meta:
        unique_together =("emp_id" , "date")

class holiday(models.Model):
    date    = models.DateField(null =True)
    purpose = models.CharField(max_length = 200, null =True)

    class Meta:
        unique_together=("date","purpose")




