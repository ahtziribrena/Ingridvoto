from django.db import models
class Ciudadanos(models.Model):
    clave_Electoral=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    edad=models.CharField(max_length=3)
    curp=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    def __str__(self):
        return self.clave_Electoral
    class Meta:
        db_table="ciudadanos"

class Candidaturas(models.Model):
    id_candidato=models.CharField(max_length=50)
    clave_Electoral=models.ForeignKey('Ciudadanos',on_delete=models.CASCADE)
    cargo=models.CharField(max_length=50)
    partido=models.CharField(max_length=50)
    def __str__(self):
        return self.partido
    class Meta:
        db_table="candidaturas"

class Votos(models.Model):
    voto=models.ForeignKey('Candidaturas',on_delete=models.CASCADE)
    class Meta:
        db_table="votos"
# Create your models here.