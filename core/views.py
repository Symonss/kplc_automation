from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from core.models import Transaction
@csrf_exempt 
def home(request):
    data = request.body.decode('utf-8').split('\n')
    nedded_data = data[1:]


    #Meter number
    meter = nedded_data[0]
    splited_meter_list = meter.split(':',1)
    meter_only = splited_meter_list[1]
  

    # Date
    date = nedded_data[2]
    splited_date_list = date.split(':',1)
    date_only = splited_date_list[1]
   

    #Token
    token = nedded_data[1]
    splited_token_list = token.split(':',1)
    token_only = splited_token_list[1]
  

       # Units
    unit = nedded_data[3]
    splited_unit_list = unit.split(':',1)
    unit_only = splited_unit_list[1]
 

       # Amount
    amount = nedded_data[4]
    splited_amount_list = amount.split(':',1)
    amount_only = splited_amount_list[1]

           # token_mount
    token_amount = nedded_data[5]
    splited_token_amount_list = token_amount.split(':',1)
    token_amount_only = splited_token_amount_list[1]

               # VAT
    vat = nedded_data[6]
    splited_vat_amount_list = vat.split(':',1)
    vat_only = splited_vat_amount_list[1]

               # FEC
    fec_amount = nedded_data[7]
    splited_fec_amount_list = fec_amount.split(':',1)
    fec_only = splited_fec_amount_list[1]

           # FC
    fc_amount = nedded_data[8]
    splited_fc_amount_list = fc_amount.split(':',1)
    fc_only = splited_fc_amount_list[1]

         # EPRA
    epra_amount = nedded_data[9]
    splited_epra_amount_list = epra_amount.split(':',1)
    epra_only = splited_epra_amount_list[1]

         # WERMA
    werma_amount = nedded_data[10]
    splited_werma_amount_list = werma_amount.split(':',1)
    werma_only = splited_werma_amount_list[1]

         # REP
    rep_amount = nedded_data[11]
    splited_rep_amount_list = rep_amount.split(':',1)
    rep_only = splited_rep_amount_list[1]

         # IA
    ia_amount = nedded_data[12]
    splited_ia_amount_list = ia_amount.split(':',1)
    ia_only = splited_ia_amount_list[1]
    print(ia_only)


    t = Transaction(ia = ia_only,rep = rep_only,werma = werma_only,epra = epra_only,fc = fc_only,fec = fec_only,vat=vat_only,token_amount = token_amount_only,meter_no  = meter_only, token = token_only, date = date_only, amount = amount_only, units = unit_only )
    t.save()


    return render(request, 'home.html', {})
