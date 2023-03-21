from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Specjalizacja(models.Model): #popraic nazwy  na jakies normalne kurtwa ten
    SPECJALIZACJA=(
            ('Rodzinny','Rodzinny'),
            ('Dermatolog','Dermatolog'),
            ('Pediatra','Pediatra'),
            ('Ortopeda','Ortopeda'),
            ('Neurolog','Neurolog'),
        )
    specjalizacja = models.CharField(max_length=30,choices=SPECJALIZACJA)
    def __str__(self):    
        return self.specjalizacja


class Lekarz(models.Model):
    name = models.CharField(max_length=40)
    specjalizacja = models.ForeignKey(Specjalizacja,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Pacjent(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=9)
    pesel = models.CharField(max_length=11)
    email = models.CharField(max_length=30)
    def __str__(self):
        return self.name  
 
class Oddział(models.Model):
    name = models.CharField(max_length=40)
    adres = models.CharField(max_length=30)
    def __str__(self):
        return self.name

# class Notatka(models.Model):
#     content = models.CharField(max_length=100)

class Wizyta(models.Model):
    # content = models.ForeignKey(Notatka, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()   #input type="data"
    pacjent = models.ForeignKey(Pacjent, on_delete=models.CASCADE)
    lekarz = models.ForeignKey(Lekarz,on_delete=models.SET_NULL,null=True)
    oddział = models.ForeignKey(Oddział,on_delete=models.CASCADE)
    content = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return f'{self.lekarz} {self.date.date()}' 