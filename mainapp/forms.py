from django import forms


class TipPredictionForm(forms.Form):
    total_bill = forms.FloatField(label="Total Bill (INR)", required=True)
    size = forms.IntegerField(label="Party Size", required=True)
    sex = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], label="Customer's Sex")
    smoker = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], label="Smoker?")
    day = forms.ChoiceField(choices=[('Thru','Monday'),('Fri','Tuesday'),('Sat','Wednesday'),('Thur', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday'),], label="Day")
    time = forms.ChoiceField(choices=[('BreakFast','Dinner'),('Lunch', 'Lunch'), ('Dinner', 'Dinner')], label="Time")

    total_bill = forms.FloatField(label="Total Bill ($)")
    sex = forms.ChoiceField(choices=[(0, 'Male'), (1, 'Female'),(0,'Others')], label="Sex")
    smoker = forms.ChoiceField(choices=[(0, 'Non-Smoker'), (1, 'Smoker')], label="Smoker")
    day = forms.ChoiceField(
        choices=[(0, 'Thur'), (1, 'Fri'), (2, 'Sat'), (3, 'Sun'),(4,'Mon'),(5,'Tues'),(6,'Wedn')],
        label="Day of the Week"
    )
    time = forms.ChoiceField(choices=[(0, 'Lunch'), (1, 'Dinner'),(0,'Break Fast')], label="Time")
    size = forms.IntegerField(label="Party Size")


from .models import Employee

from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'role', 'email', 'phone_number', 'address', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'role': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]{10}', 'required': 'required'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'required': 'required'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
    
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Enter a valid 10-digit phone number.")
        return phone

