from django import forms
from .models import *

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

class DateInput(forms.DateInput):
    input_type = 'date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {
            'due': (DateInput()),
        }
        fields = ['subject', 'title', 'description', 'due', 'is_finished']

class DashboardForm(forms.Form):
    text = forms.CharField(
        label='Enter your search term',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your search term'})
    )


# Search form
class YoutubeForm(forms.Form):
    query = forms.CharField(
        label='Search YouTube',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter search term'})
    )

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_finished']

class ConversionForm(forms.Form):
    input_value = forms.FloatField(
        label="Enter value",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter value"})
    )

    input_type = forms.ChoiceField(
        choices=[
            ('km_to_m', 'Kilometers to Meters'),
            ('m_to_km', 'Meters to Kilometers'),
            ('c_to_f', 'Celsius to Fahrenheit'),
            ('f_to_c', 'Fahrenheit to Celsius'),
        ],
        label="Conversion Type",
        widget=forms.Select(attrs={"class": "form-control"})
    )