from django.shortcuts import render

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


# Create your views here.

@main_auth(on_cookies=True)
def show_deals(request):
    user = request.bitrix_user_token
    res = user.call_api_method('crm.deal.list')['result'][:10]
    value = len(res)
    return render(request,'deals.html',locals())

@main_auth(on_cookies=True)
def create_deal(request):
    user = request.bitrix_user_token
    res_create = user.call_api_method('crm.deal.add')
    print(res_create)
    return render(request,'deals.html',locals())