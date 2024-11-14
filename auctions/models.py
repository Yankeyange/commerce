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
    image = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=100)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    # la date à laquelle l'utilisateur va créer sa vente 
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# modèles pour les offres(bids)

class Bids(models.Model):
    price = models.IntegerField()


# modèles pour les commentaires

class Comment(models.Model):
    text = models.ForeignKey(Auctions, on_delete=models.CASCADE)
