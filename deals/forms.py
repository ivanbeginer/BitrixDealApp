from django import forms


from deals.methods import user


stages = user.call_api_method('crm.status.entity.items',params={'entityId':'DEAL_STAGE'})['result']
res_stages = ((i['STATUS_ID'],i['NAME']) for i in stages)

currency = user.call_api_method('crm.currency.list',params={'order':{'field_1':'asc'}})['result']
res_currency = ((i['CURRENCY'],i['FULL_NAME']) for i in currency)

res_pay_methods = (('SBP','СБП'),('NAL','Наличные'),('CARD','Банковская карта'))


class DealCreateForm(forms.Form):

    title = forms.CharField(required=False,label='Название сделки')
    stage = forms.ChoiceField(choices=res_stages,required=False,label='Этап сделки')
    currency = forms.ChoiceField(choices=res_currency,required=False,label='Валюта')
    opportunity = forms.FloatField(min_value=0.00,required=False,label='Стоимость сделки')
    begin_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'},format='%d/%m/%Y'),required=False,label='Начало сделки')
    close_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'},format='%d/%m/%Y'),required=False,label='Конец сделки')
    payment_method = forms.ChoiceField(choices=res_pay_methods,required=False)

