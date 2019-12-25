from django import forms
from .models import Item

ATTRS = {
    'class': 'border border-gray-500 focus:border-blue-500 text-gray-800 py-1 px-2 w-full',
    'placeholder': 'Write your name here'}
widget = forms.TextInput(
    ATTRS
)


class ItemForm(forms.ModelForm):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            ATTRS
        )
    )
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            ATTRS
        )
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'border border-gray-500 focus:border-blue-500 text-gray-800 py-1 px-2 w-full',
                'placeholder': 'Enter Text here'}
        )
    )
    price = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'class': 'border border-gray-500 focus:border-blue-500 text-gray-800 py-1 px-2 w-full',
            }
        )
    )
    photo = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'relative border border-gray-500 focus:border-blue-500 text-gray-800  w-full',
            }
        )
    )

    class Meta:
        model = Item
        fields = ['name', 'title', 'text', 'price', 'photo']
