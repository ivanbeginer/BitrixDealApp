from django.shortcuts import render, redirect

from deals.forms import DealCreateForm
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


# Create your views here.

@main_auth(on_cookies=True)
def show_deals(request):
    user = request.bitrix_user_token
    res = user.call_api_method('crm.deal.list')['result'][:10]
    new_res = {}
    for deal in res:
        deal['BEGINDATE']=deal['BEGINDATE'][:10]
        deal['CLOSEDATE']=deal['CLOSEDATE'][:10]
    # for deal in res:
    #     user.call_api_method('crm.deal.delete',params={'id':deal['ID']})

    return render(request,'deals.html',locals())

@main_auth(on_cookies=True)
def create_deal(request):
    user = request.bitrix_user_token
    form = DealCreateForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            data = form.cleaned_data
            print(data['begin_date'])
            res = user.call_api_method('crm.deal.add',params={'fields':{
                'TITLE':data['title'],
                'STAGE':data['stage'],
                'CURRENCY_ID':data['currency'],
                'OPPORTUNITY':data['opportunity'],
                'BEGINDATE':data['begin_date'],
                'CLOSEDATE':data['close_date'].strftime('%d/%m/%y')
            }})
            return redirect('show_deals')

    return render(request,'create_deal.html',locals())