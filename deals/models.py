from django.db import models
from integration_utils.bitrix24.models import bitrix_user
# Create your models here.


class Deal(models.Model):
    title = models.CharField()
