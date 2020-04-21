from django.shortcuts import render
from Rental.models import StateModel,CountryModel,CustomerModel,RentalAgreementLine,RentalRegisterModel
import datetime
def ShowCoustemer(request):
    return render(request,'coustemer.html',{'state':StateModel.objects.all(),'country':CountryModel.objects.all()})


def SaveCoustemer(request):
    name=request.POST['c1']
    phone=request.POST['c2']
    lline1=request.POST['c3']
    emial=request.POST['c4']
    line2=request.POST['c5']
    city=request.POST['c6']
    state=request.POST['c7']
    country=request.POST['c8']
    zip=request.POST['c9']
    data={'meg':'saved'}
    CustomerModel(name=name,street=lline1,street2=line2,zip=zip,city=city,state_id=state,country_id=country,phone=phone,email=emial).save()
    return render(request,'coustemer.html',{'data':data})


def RentalAgree(request):
    return render(request,'renatalagreement.html',{'data':CustomerModel.objects.all()})

from Rental.models import RentalAgreementModel
def SaverentalAgreement(request):
    refrence5=''
    if request.POST['confirm'] == 'first':
        reference = request.POST['r1']
        period = request.POST['r2']
        customer = request.POST['r3']
        periodlength = request.POST['r4']
        rental_type = request.POST['r5']
        rental_amount = request.POST['r6']
        item = request.POST['r7']
        agreement_start = request.POST['r8']
        stage = request .POST['r9']
        RentalAgreementModel(reference=reference, rental_amount=rental_amount, period=period
                             , period_length=periodlength, rental_type=rental_type, item=item, custoemer_id=customer,
                             agreement_date=agreement_start, stage=stage).save()
        return render(request, 'renatalagreement.html', {'data2': reference,'data':CustomerModel.objects.all()})
    elif request.POST['confirm'] == 'second':
        reference=request.POST['ral1']
        payamount=request.POST['ral2']
        Date=request.POST['ral3']
        status=request.POST['ral4']
        value_rental=RentalAgreementModel.objects.filter(reference=reference).values('period','period_length','rental_amount')
        request.session['reference']=reference
        period_length=value_rental[0]['period_length']
        rental_amount=value_rental[0]['rental_amount']
        range_in=float(rental_amount)//float(payamount)
        range_in_2=round(range_in)
        date = datetime.datetime.strptime(Date, "%Y-%m-%d")
        month_in_31 = [1, 3, 5, 7, 8, 10, 12]
        month_in_30 = [4, 6, 9, 11]
        day_str = ''
        for x in range(range_in_2):
            if date.month in month_in_31:
                timedel = datetime.timedelta(days=31 * period_length)
            elif date.month in month_in_30:
                timedel = datetime.timedelta(days=30 * period_length)
            else:
                timedel = datetime.timedelta(days=28 * period_length)
            date = date + timedel
            day_str = str(date.date())
            RentalAgreementLine(rental_agreement_id=reference,payment_amount=payamount,date=day_str,status=status).save()

        return render(request, 'renatalagreement.html', {'data2': reference,'data':RentalAgreementModel.objects.all()})
    else:
        return render(request,'tableshow.html',{'data':RentalAgreementLine.objects.filter(rental_agreement_id=request.session['reference'])})


def openrentalreg(request):
    return render(request,'rentalopen.html',{'data2':RentalAgreementModel.objects.filter(reference=request.session['reference'])})


def saveregister(request):
    if request.POST['confirm'] == 'third':
        refer = request.POST['reg1']
        item = request.POST['reg2']
        rental_agree = request.POST['reg3']
        pay_date = request.POST['reg4']
        rental_type = request.POST['reg5']
        pay_amt = request.POST['reg6']
        customer = request.POST['reg7']
        stage = request.POST['reg8']
        request.session['date']=pay_date
        RentalRegisterModel(reference=refer,item=item,rental_agreement_id=rental_agree,
                            payment_date=pay_date,rental_type=rental_type,payment_amount=pay_amt,
                            customer_id=customer,stage=stage).save()
        return openrentalreg(request)
    if request.POST['confirm'] == 'first':
        RentalAgreementLine.objects.filter(rental_agreement_id=request.session['reference'],date=request.session['date']).update(status='confirm')
        #RentalRegisterModel.objects.filter(reference=request.session['reference']).update(status='confirm')
        return openrentalreg(request)
    if request.POST['confirm'] == 'second':
        RentalAgreementLine.objects.filter(rental_agreement_id=request.session['reference'],date=request.session['date']).update(status='cancel')
        return openrentalreg(request)

