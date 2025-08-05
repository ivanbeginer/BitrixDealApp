from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from deals.forms import DealCreateForm, res_stages, stages
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


# Create your views here.


@main_auth(on_cookies=True)

def show_deals(request):
    user = request.bitrix_user_token
    deals = user.call_api_method('crm.deal.list', {
        'select': [
            'ID', 'TITLE', 'STAGE_ID', 'BEGINDATE', 'CLOSEDATE',
            'OPPORTUNITY', 'CURRENCY_ID', 'UF_CRM_USRFLD'
        ],
        'order': {'BEGINDATE': 'DESC'}
    })['result']
    print(stages)


    for deal in deals:
        deal['BEGINDATE']=deal['BEGINDATE'][:10]
        deal['CLOSEDATE']=deal['CLOSEDATE'][:10]
    #add_field = user.call_api_method('crm.deal.userfield.add',params={'fields':{'USER_TYPE_ID':'string','FIELD_NAME':'UF_CRM_USRFLD','LIST':[{'KEY':'SBP','VALUE':'СБП'},{'KEY':'NAL','VALUE':'Наличные'},{'KEY':'CARD','VALUE':'Банковская карта'}]}})['result']
    #change = user.call_api_method('crm.deal.userfield.delete',params={'id':241})

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
            print(data['payment_method'])
            print(res_stages)
            res = user.call_api_method('crm.deal.add',params={'fields':{
                'TITLE':data['title'],
                'STAGE_ID':data['stage'],
                'CURRENCY_ID':data['currency'],
                'OPPORTUNITY':data['opportunity'],
                'BEGINDATE':data['begin_date'],
                'CLOSEDATE':data['close_date'],
                'UF_CRM_USRFLD':data['payment_method']
            }})

            return redirect('show_deals')

    return render(request,'create_deal.html',locals())