from django.db import models

# Create your models here.
# name="name"
# name="mobile"
# name="email"
# name="dob"
# name="city"
# name="password"
# name="confirm_password"
# name="caccept"
class Student(models.Model):
    user_name=models.CharField(max_length=100,null=False)
    mobile=models.CharField(max_length=13)
    email=models.EmailField(null=False,unique=True)
    dateOfBirth=models.DateField()
    city=models.CharField(max_length=120)
    user_password=models.CharField(max_length=120)
    def __str__(self):
        return f'{self.user_name}     {self.email}      {self.user_password}'