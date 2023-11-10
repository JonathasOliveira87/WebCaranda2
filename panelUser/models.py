from django.db import models
from django.contrib.auth.models import User
import re

class profileManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='avatar/')

    MORADOR_CHOICES = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    DONO_CHOICES = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    PET_CHOICES = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    telefone = models.CharField(max_length=50)
    morador = models.CharField(max_length=3, choices=MORADOR_CHOICES)
    dono = models.CharField(max_length=3, choices=DONO_CHOICES)
    casa = models.IntegerField()
    carro = models.CharField(max_length=50)
    moto = models.CharField(max_length=50)
    pet = models.CharField(max_length=3, choices=DONO_CHOICES)

    def save(self, *args, **kwargs):
        # Formatar o número de telefone
        self.telefone = self.format_phone_number(self.telefone)
        super(profileManager, self).save(*args, **kwargs)

    def format_phone_number(self, phone):
        # Remover caracteres não numéricos
        digits = re.sub(r'\D', '', phone)

        # Verificar o tamanho do número de telefone e aplicar a formatação
        if len(digits) == 11:
            # Formato com DDD (11 dígitos) - (00) 0.0000-0000
            formatted_phone = "({}) {}.{}-{}".format(digits[:2], digits[2:3], digits[3:7], digits[7:])
        elif len(digits) == 10:
            # Formato sem DDD (10 dígitos) - 0.0000-0000
            formatted_phone = "{}-{}".format(digits[:5], digits[5:])
        elif len(digits) == 9:
            # Formato com 9 dígitos, sem o primeiro 0 (9 dígitos) - 9.0000-0000
            formatted_phone = "9.{}-{}".format(digits[:4], digits[4:])
        else:
            # Caso o tamanho não corresponda aos formatos esperados, manter o original
            formatted_phone = phone

        return formatted_phone

    def __str__(self):
        return f'{self.user.username}, {self.telefone}, {self.morador}, {self.dono}, {self.casa}, {self.carro}, {self.moto}, {self.pet}, {self.profile_pic}'
