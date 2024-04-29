from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CardInDeckForm


# Add the following import
from django.http import HttpResponse

#Import Models from .models
from .models import Deck
from .models import Card
from .models import CardInDeck


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def card_index(request):
   cards = Card.objects.all()
   return render(request, 'cards/index.html', {'cards': cards})

def deck_index(request):
   decks = Deck.objects.all()
   return render(request, 'decks/index.html', {'decks': decks})

def deck_detail(request, deck_id):
   deck = Deck.objects.get(id=deck_id)
   cardsindeck = CardInDeck.objects.all()
   return render(request, 'decks/detail.html', {
      'deck': deck,
      'cardsindeck': cardsindeck
   })

#Login Required Functionality

#Deck Functionality
class DeckCreate(LoginRequiredMixin, CreateView):
    model = Deck
    fields = ['name', 'description', 'game']
    success_url = '/decks/'

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
   
class DeckUpdate(LoginRequiredMixin, UpdateView):
    model = Deck
    fields = ['name', 'description', 'game']
    success_url = '/decks/'

class DeckDelete(LoginRequiredMixin, DeleteView):
    model = Deck
    success_url = '/decks/'

#CardsInDeck Functionality
@login_required
def add_cardindeck(request, deck_id, card_id):
  cardindeck = CardInDeck.objects.filter(card_id = card_id, deck_id=deck_id).first()
  if cardindeck:
    return redirect('detail', deck_id=deck_id)
  form = CardInDeckForm(request.POST)
  if form.is_valid():
     new_cardindeck = form.save(commit=False)
     new_cardindeck.deck_id = deck_id
     new_cardindeck.card_id = card_id
     new_cardindeck.save()
  return redirect('detail', deck_id=deck_id)
