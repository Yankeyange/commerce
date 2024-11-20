from django.contrib.auth.models import AbstractUser
from django.db import models


# création de touts mes modèles nécessaires

# modèles Utilisateurs déjà intégré de Django
class User(AbstractUser):
    pass

# modèles pour les enchères(Auctions)

class Auctions(models.Model):
    name = models.CharField(max_length=200)
    title = models.TextField(max_length=100)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    # la date à laquelle l'utilisateur va créer sa vente 
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
"""
    
# modèles pour les offres(bids)

class Bids(models.Model):
    # ici l'utilisateur peut donner un prix mais peut ne pas commenter
    price = models.IntegerField()


# modèles pour les commentaires

class Comment(models.Model):
    # ici l'utilisateur peut commenter mais peut ne pas lacher un prix
    text = models.ForeignKey(Auctions, on_delete=models.CASCADE)

    # je ne sais pas si je dois créer encore un modèle c'est un peu frustant tout cela
"""

class Details(models.Model):
    # le prix minimum qui doit être 
    min_price = models.PositiveIntegerField(default=1000)
    # pour gerer les commentaires de l'utilisateur
    comment = models.ForeignKey(Auctions, on_delete=models.CASCADE)
