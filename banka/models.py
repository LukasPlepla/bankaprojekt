from django.db import models

# Create your models here.


class Zakaznik(models.Model):
    jmeno = models.CharField(max_length=50)
    prijmeni = models.CharField(max_length=50)
    datum_registrace = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class TypUctu(models.Model):
    nazev = models.CharField(max_length=50, unique=True)
    popis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nazev

class Ucet(models.Model):
    zakaznik = models.ForeignKey(Zakaznik, on_delete=models.CASCADE, related_name="ucty")
    typ = models.ForeignKey(TypUctu, on_delete=models.PROTECT, related_name="ucty")
    cislo_uctu = models.CharField(max_length=20, unique=True)
    datum_zalozeni = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Účet {self.cislo_uctu} ({self.typ}) – {self.zakaznik}"

class Poplatek(models.Model):
    ucet = models.ForeignKey(Ucet, on_delete=models.CASCADE, related_name="poplatky")
    castka = models.DecimalField(max_digits=10, decimal_places=2)
    popis = models.CharField(max_length=255, blank=True)
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Poplatek {self.castka} na účet {self.ucet}"

class UrokovaSazba(models.Model):
    typ_uctu = models.ForeignKey(TypUctu, on_delete=models.CASCADE, related_name="urokove_sazby")
    sazba = models.DecimalField(max_digits=5, decimal_places=2)
    platna_od = models.DateField()
    platna_do = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Úroková sazba {self.sazba}% pro {self.typ_uctu}, od {self.platna_od}"

