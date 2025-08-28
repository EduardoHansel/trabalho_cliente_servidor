from django.db import models

class Credencial(models.Model):

    login = models.CharField(max_length=45, unique=True)
    senha = models.CharField(max_length=45)

    class Meta:
        verbose_name = "Credencial"
        verbose_name_plural = "Credenciais"
        db_table = "credenciais"
