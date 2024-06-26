from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

GAMES = (
    (1, "Unlisted"),
    (2, "Magic the Gathering"),
    (3, "Pokemon"),
    (4, "Yu-Gi-Oh"),
)

class Deck(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(
        default="No Description"
    )
    game = models.IntegerField(
        choices=GAMES,
        default=GAMES[0][0]
    )

    def __str__(self):
        return self.name
    
class Card(models.Model):
    name = models.CharField(max_length=75)
    game = models.IntegerField(
        choices=GAMES,
        default=GAMES[0][0]
    )
    rarity = models.CharField(max_length=15)
    cardType = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    frontImageURL = models.CharField(max_length=500)
    backImageURL = models.CharField(max_length=500)
    

    def __str__(self):
        return f"Game: {self.game}, Card: {self.name}"
    
class CardInDeck(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        default = 1,
    )

    def __str__(self):
        return f"Name: {self.card.name} , Quantity: {self.quantity}"