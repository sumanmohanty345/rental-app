from django.db import models

class CountryModel(models.Model):
    name=models.CharField(max_length=60)
    code=models.CharField(unique=True,max_length=6)

class StateModel(models.Model):
    name= models.CharField(max_length=60)
    code=models.CharField(unique=True,max_length=5)
    country=models.ForeignKey(CountryModel,on_delete=models.CASCADE)

class CustomerModel(models.Model):
    name=models.CharField(max_length=60)
    street=models.CharField(max_length=120)
    street2=models.CharField(max_length=120)
    zip=models.CharField(max_length=15)
    city=models.CharField(max_length=120)
    state=models.ForeignKey(StateModel,on_delete=models.CASCADE)
    country=models.ForeignKey(CountryModel,on_delete=models.CASCADE)
    phone=models.CharField(max_length=60)
    email=models.CharField(max_length=120)
class RentalAgreementModel(models.Model):
    reference=models.CharField(primary_key=True,max_length=25)
    rental_amount=models.FloatField()
    period=models.IntegerField()
    period_length=models.IntegerField()
    rental_type=models.CharField(max_length=50)
    agreement_date=models.DateField()
    custoemer=models.ForeignKey(CustomerModel,on_delete=models.CASCADE)
    item=models.CharField(max_length=60)
    stage=models.CharField(max_length=50)
class RentalAgreementLine(models.Model):
    date=models.DateField()
    payment_amount=models.FloatField()
    status=models.CharField(max_length=50)
    rental_agreement=models.ForeignKey(RentalAgreementModel,on_delete=models.CASCADE)
class RentalRegisterModel(models.Model):
    reference=models.CharField(max_length=25,unique=True)
    rental_agreement=models.ForeignKey(RentalAgreementModel,on_delete=models.CASCADE)
    payment_date=models.DateField()
    payment_amount=models.FloatField()
    customer=models.ForeignKey(CustomerModel,on_delete=models.CASCADE)
    rental_type=models.CharField(max_length=50)
    item=models.CharField(max_length=120)
    stage=models.CharField(max_length=50)