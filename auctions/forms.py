from django import forms
from .models import Listing, Category, Bid


class ListingForm(forms.ModelForm):
    class Meta():
        model = Listing
        fields = ["title", "description", "image_url", "category", "price"]
        labels = {"image_url": "Image URL"}

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            "image_url": forms.URLInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"})
        }
    
    # Define a custom widget for the category field
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={"class": "custom-select"})
    )

class BidForm(forms.ModelForm):
    class Meta():
        model = Bid
        fields = ["amount"]

        widgets = {
            "amount": forms.NumberInput(attrs={"class": "form-control"})
        }