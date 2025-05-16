from django.contrib import admin

from .models import Zakaznik, Ucet, TypUctu, UrokovaSazba, Poplatek

admin.site.register(Zakaznik)
admin.site.register(Ucet)
admin.site.register(TypUctu)
admin.site.register(UrokovaSazba)
admin.site.register(Poplatek)
# Register your models here.
