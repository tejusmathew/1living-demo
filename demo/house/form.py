from django.forms import ModelForm
from .models import House_refer, Refer


class House_refer_form(ModelForm):
    class Meta:
        model = House_refer
        fields = ["Address", "Bed", "Bath", "Storage", "Wifi", "Referal_code"]


class Refer_form(ModelForm):
    class Meta:
        model = Refer
        fields = ["name"]
