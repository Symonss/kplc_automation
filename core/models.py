from django.db import models


class Transaction(models.Model):
    meter_no = models.CharField(max_length=100)
    token = models.CharField(max_length =100)
    date = models.CharField(max_length=100)
    amount = models.CharField(max_length =100)
    units = models.CharField(max_length=100)
    token_amount = models.CharField(max_length=100)
    vat = models.CharField(max_length =100)
    fec = models.CharField(max_length=100)
    fc = models.CharField(max_length=100)
    epra = models.CharField(max_length =100)
    werma = models.CharField(max_length=100)
    rep = models.CharField(max_length=100)
    ia = models.CharField(max_length =100)

    def __str__(self):
        return self.meter_no
