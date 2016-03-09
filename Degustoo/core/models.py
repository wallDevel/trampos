from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.utils import timezone

from cliente.models import Cliente
from restaurante.models import Restaurante

# CUSTOM MANAGERS
class MyManager(BaseUserManager):
    def _create_user(self, email, password, nivel,
                     is_admin, is_superuser, is_active, **kwargs):
        if not email:
            raise ValueError("Please enter you email account")
        email = self.normalize_email(email)
        usuario = self.model(
                             email=email, password=password, nivel=nivel,
                             is_admin=is_admin, is_superuser=is_superuser, is_active=is_active, **kwargs)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    
    def create_user(self, email=None, password=None, nivel=1, **kwargs):
        return self._create_user(email, password, nivel, False, False, True, **kwargs)
    
    def create_superuser(self, email, password, nivel=0, **kwargs):
        return self._create_user(email, password, nivel, True, True, True, **kwargs)
        

# MODULES 
class Usuario(AbstractBaseUser, PermissionsMixin):
    NIVEL_CHOICES = (
        (0, 'ADMIN'),
        (1, 'CLIENTE'),
        (2, 'RESTAURANTE'),
        (3, 'RESTAURANTE DIAMANTE'),
    )
    
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=50, blank=True)
    nivel = models.IntegerField(choices=NIVEL_CHOICES)
    avatar = models.OneToOneField("Imagem", blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['nivel']
    
    objects = MyManager()
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    
    @property 
    def is_staff(self):
        return self.is_admin

class Imagem(models.Model):
    image = models.ImageField()

class Endereco(models.Model):
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50) 
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=50) 
    complemento = models.CharField(max_length=50) 
    cep = models.CharField(max_length=50)

    def __unicode__(self):
        return self.cep
    
class Voto(models.Model):
    KIND = (
            (0, "-"),
            (1, "+")
    )
    
    QUANTITY = (
            (1),
            (2),
            (3),
            (4),
            (5)
    )
    from_cliente = models.ForeignKey(Cliente)
    to_restaurante = models.ForeignKey(Restaurante)
    tipo = models.IntegerField(choices=KIND)
    quantidade = models.IntegerField()

    def __unicode__(self):
        return self.quantidade
    
class Comentario(models.Model):
    cliente = models.ForeignKey(Cliente)
    restaurante = models.ForeignKey(Restaurante)
    texto = models.TextField()
    send_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.texto

class Resposta(models.Model):
    cliente = models.ForeignKey(Cliente)
    restaurante = models.ForeignKey(Restaurante)
    comentario = models.ForeignKey(Comentario)
    texto = models.TextField()
    send_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.texto

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente)
    restaurante = models.ForeignKey(Restaurante)