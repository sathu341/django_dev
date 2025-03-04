from django import forms


class TipPredictionForm(forms.Form):
    total_bill = forms.FloatField(label="Total Bill (INR)", required=True)
    size = forms.IntegerField(label="Party Size", required=True)
    sex = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], label="Customer's Sex")
    smoker = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], label="Smoker?")
    day = forms.ChoiceField(choices=[('Thur', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], label="Day")
    time = forms.ChoiceField(choices=[('Lunch', 'Lunch'), ('Dinner', 'Dinner')], label="Time")

    total_bill = forms.FloatField(label="Total Bill ($)")
    sex = forms.ChoiceField(choices=[(0, 'Male'), (1, 'Female')], label="Sex")
    smoker = forms.ChoiceField(choices=[(0, 'Non-Smoker'), (1, 'Smoker')], label="Smoker")
    day = forms.ChoiceField(
        choices=[(0, 'Thur'), (1, 'Fri'), (2, 'Sat'), (3, 'Sun')],
        label="Day of the Week"
    )
    time = forms.ChoiceField(choices=[(0, 'Lunch'), (1, 'Dinner')], label="Time")
    size = forms.IntegerField(label="Party Size")


from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'role', 'email', 'phone_number', 'salary', 'shift', 'date_of_joining', 'address', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'shift': forms.Select(attrs={'class': 'form-control'}),
            'date_of_joining': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
           
        }
