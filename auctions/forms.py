from django import forms
from .models import Auctions

class AuctionsForm(forms.ModelForm):
  class Meta:
    model = Auctions
    fields = ['name', "title", "image","description", "price"]

# pour le formulaire du commentaire
"""
class EntryForm(forms.ModelForm):
  class Meta:
    model = Entry
    fields = ['text']

"""