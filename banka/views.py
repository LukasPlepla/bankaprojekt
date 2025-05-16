from django.shortcuts import render
from .models import Zakaznik, TypUctu, Ucet, Poplatek, UrokovaSazba


def index(request):
    zakaznici = Zakaznik.objects.all()
    typy_uctu = TypUctu.objects.all()
    ucty = Ucet.objects.all()
    poplatky = Poplatek.objects.all()
    urokove_sazby = UrokovaSazba.objects.all()
    
    context = {
        'zakaznici': zakaznici,
        'typy_uctu': typy_uctu,
        'ucty': ucty,
        'poplatky': poplatky,
        'urokove_sazby': urokove_sazby,
    }
    
    return render(request, 'banka/index.html', context)


