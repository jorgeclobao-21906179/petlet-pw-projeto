from django.forms import ModelForm
from .models import Customer,AdoptAnimal

class ContactForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class AdoptionForm(ModelForm):
    class Meta:
        model = AdoptAnimal
        fields = '__all__'