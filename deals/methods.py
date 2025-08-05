from integration_utils.bitrix24.models import BitrixUserToken, BitrixUser

user = BitrixUserToken.objects.filter(user__is_admin=True).first()


