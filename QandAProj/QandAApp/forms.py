from django import forms
from QandAApp.models import QandAModel


class NewQnadAForm(forms.ModelForm):
    class Meta():
        model = QandAModel
        fields = '__all__'
