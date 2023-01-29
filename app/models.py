from django.db import models

# Create your models here.

#tworzenie modelu lekarze
class Lekarz(models.Model):

  lekarz_id = models.AutoField(primary_key=True)
  imie = models.CharField(max_length=100)
  nazwisko = models.CharField(max_length=100)
  
  #zwracanie imienia i nazwiska w wyświetlaniu
  def __str__(self):
        return str(self.imie+' '+self.nazwisko)

  #nazwanie modelu lekarz   
  class Meta:
        verbose_name = ("Lekarz")
        verbose_name_plural = ("Lekarz")

    
#tworzenie modelu pacjeci
class Pacjent(models.Model):
  Lekarz_id = models.ForeignKey(
          Lekarz, 
          on_delete=models.CASCADE
  )
  pacjent_id = models.AutoField(primary_key=True)
  imie = models.CharField(max_length=100)
  nazwisko = models.CharField(max_length=100)
  
  #zwracanie imienia i nazwiska w wyświetlaniu
  def __str__(self):
        return str(self.imie+' '+self.nazwisko)
  class Meta:
        verbose_name = ("Pacjent")
        verbose_name_plural = ("Pacjent")
 