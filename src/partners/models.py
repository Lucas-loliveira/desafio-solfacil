from django.db import models


class Partner(models.Model):
    cnpj = models.CharField(max_length=14, unique=True)
    name = models.CharField(max_length=100)
    trade_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return self.name
