from django import forms
from .models import Listing, Category


class ListingForm(forms.ModelForm):
    class Meta():
        model = Listing
        # fields = ["title", "description",
        #           "image_url", "category"]
        
        fields = "__all__"

        labels = {"image_url": "Image URL"}

    # Define a custom widget for the category field
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label=None
    )
