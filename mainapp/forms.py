from django import forms
from .models import Titanic


class TitanicUploadForm(forms.Form):
    file = forms.FileField()


class TitanicForm(forms.ModelForm):
    class Meta:
        model = Titanic
        fields = '__all__'
        widgets = {
            'survived': forms.Select(choices=[('0', 'No'), ('1', 'Yes')]),
            'pclass': forms.Select(choices=[('1', 'First Class'), ('2', 'Second Class'), ('3', 'Third Class')]),
            'sex': forms.Select(choices=[('male', 'Male'), ('female', 'Female')]),
            'embarked': forms.Select(choices=[('C', 'Cherbourg'), ('S', 'Southampton'), ('Q', 'Queenstown')]),
        }
