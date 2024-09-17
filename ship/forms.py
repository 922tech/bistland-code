from django import forms
from .models import Titanic


# 1. Upload File Form: Handles the Excel file upload
class UploadFileForm(forms.Form):
    file = forms.FileField(label="Select an Excel file")

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith('.xlsx'):
            raise forms.ValidationError('Please upload a valid Excel file (.xlsx).')
        return file


# 2. Titanic Form: Handles Create and Update operations for Titanic records
class TitanicForm(forms.ModelForm):
    class Meta:
        model = Titanic
        fields = [
            'passengerID', 'survived', 'pclass', 'name', 'sex', 'age',
            'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked'
        ]

    # Customizing the form fields for better user experience
    survived_choices = (
        (0, 'No (Died)'),
        (1, 'Yes (Survived)')
    )

    pclass_choices = (
        (1, '1st Class'),
        (2, '2nd Class'),
        (3, '3rd Class')
    )

    embarked_choices = (
        ('C', 'Cherbourg'),
        ('S', 'Southampton'),
        ('Q', 'Queenstown')
    )

    survived = forms.ChoiceField(choices=survived_choices, label="Survived")
    pclass = forms.ChoiceField(choices=pclass_choices, label="Class")
    embarked = forms.ChoiceField(choices=embarked_choices, label="Embarked")

    # Optional: Add custom validation logic for any field if needed
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and (age < 0 or age > 120):
            raise forms.ValidationError('Please enter a valid age between 0 and 120.')
        return age

    def clean_fare(self):
        fare = self.cleaned_data.get('fare')
        if fare < 0:
            raise forms.ValidationError('Fare cannot be negative.')
        return fare
