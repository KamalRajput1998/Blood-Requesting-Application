from django.db import models
from django.contrib.auth.models import User

#Dimension tables:

#User table.
Occupations = [
    ('Consultant', "Consultant"),
    ('GP', "GP"),
    ('Doctor', "Doctor"),
    ('Other', 'Other')
]

class User(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Occupation = models.CharField(max_length=10, choices=Occupations, default="Consultant")
    Extension = models.CharField(max_length=10)
    Fullname = models.CharField(max_length=100)

    def __str__(self):
        return self.Fullname
    
    class Meta:
        verbose_name_plural = "Users"


#Patient table.
'''
class Patient(models.Model):
    System_Number = models.CharField(max_length=10)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    DOB = models.DateField()

    def __str__(self):
        return(f'{self.System_Number}')
'''

#CMV table.
'''
class CMV(models.Model):
    CMV = models.CharField(max_length=100)

    def __str__(self):
        return(f"{self.CMV}")
'''

#Irradiated products table.
'''
class Irradiated_Products(models.Model):
    IR = models.CharField(max_length=100)

    def __str__(self):
        return(f"{self.IR}")
    
    class Meta:
        verbose_name_plural = "Irradiated_Products"
'''

#Fact table:

#Transaction table / can be further normalized if needed.
class Transaction(models.Model):
    #System_Number = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    System_Number = models.CharField(max_length=10, null=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CMV = models.CharField(max_length=100, null=True)
    IR = models.CharField(max_length=100, null=True)
    Recent_Transfusion = models.BooleanField(default=False)
    Pregnant = models.BooleanField(default=False)
    High_Risk = models.BooleanField(default=False)
    Date_Submitted = models.DateTimeField(auto_now_add=True, null=True)
    Diagnosis = models.CharField(max_length=100)
    Urgent = models.BooleanField(default=False) 
    GS = models.BooleanField(default=False)
    DAT = models.BooleanField(default=False)
    Other_Test = models.TextField(null=True)
    #Choices for blood component fields
    '''
    Metric = [
        ('Units', "Units"),
        ('Ml', "Ml"),
    ]
    '''
    #Fields for blood components
    RC = models.BooleanField(default=False)
    RC_Measurement = models.CharField(max_length=100,null=True)
    RC_Quantity = models.CharField(max_length=100,null=True)
    RC_Reason = models.CharField(max_length=100,null=True)
    RC_OtherReason = models.TextField(null=True)
    
    Platelets = models.BooleanField(default=False)
    Platelets_Measurement = models.CharField(max_length=100,null=True)
    Platelets_Quantity = models.CharField(max_length=100, null=True)
    Platelets_Reason = models.CharField(max_length=100, null=True)
    Platelets_OtherReason = models.TextField(null=True)
    
    FFP = models.BooleanField(default=False)
    FFP_Measurement = models.CharField(max_length=100, null=True)
    FFP_Quantity = models.CharField(max_length=100, null=True)
    FFP_Reason = models.CharField(max_length=100,null=True)
    FFP_OtherReason = models.TextField(null=True)

    Cryo = models.BooleanField(default=False)
    Cryo_Measurement = models.CharField(max_length=100, null=True)
    Cryo_Quantity = models.CharField(max_length=100, null= True)
    Cryo_Reason = models.CharField(max_length=100, null=True)
    Cryo_OtherReason = models.TextField(null=True)

    DateTimeRequired = models.DateTimeField(auto_now=False, null=True)

    def __str__(self):
        return (f'Request for {self.System_Number}, form submitted on {self.Date_Submitted}')
    
    