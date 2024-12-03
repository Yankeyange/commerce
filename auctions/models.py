from django.contrib.auth.models import AbstractUser
from django.db import models


# création de touts mes modèles nécessaires

# modèles Utilisateurs déjà intégré de Django
class User(AbstractUser):
    pass

# modèles pour les enchères(Auctions)

class Comment(models.Model):
    # ici l'utilisateur peut commenter mais peut ne pas lacher un prix
    text = models.TextField(max_length=10000)
    # auction = models.ForeignKey(Auctions , on_delete=models.CASCADE)
    
# modèles pour les offres(bids)
class Bids(models.Model):
    # ici l'utilisateur peut donner un prix mais peut ne pas commenter
    price = models.IntegerField(default=1000)

# ajouter une catégories

class Category(models.Model):
    category = models.CharField(max_length=100)


# modèles pour les commentaires




class Auctions(models.Model):
    name = models.CharField(max_length=200)
    title = models.TextField(max_length=100)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    # la date à laquelle l'utilisateur va créer sa vente 
    date = models.DateTimeField(auto_now_add=True)
    # permettre à chaque utilisateur de laisser un commentaire
    
   
    def __str__(self):
        return self.name
    

    

