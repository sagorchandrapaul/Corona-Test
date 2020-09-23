from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    SYMPTOMS_CHOICES = (
        ('BP', 'Breathing Problem'),
        ('DC', 'Dry Cough'),
        ('ST', 'Sore throat'),
        ('W', 'Weakness'),
        ('RN', 'Runny nose'),
    )
    AdditionalInformation_CHOICES = (
        ('AP', 'Abdominal Pain'),
        ('V', 'Vomiting'),
        ('D', 'Diarrhea'),
        ('CP', 'Chest Pain'),
        ('P', 'Chest Pressure'),
        ('MP', 'Muscle Pain'),
        ('LT', 'Loss Of Taste'),
        ('LS', 'Loss Of Smell'),
        ('RS', 'Rash On The Skin'),
        ('DF', 'Discoloration Of Fingers'),
        ('DT', 'Discoloration Of Toes'),
        ('LS', 'Loss Of Speech'),
        ('LM', 'Loss Of Movement'),
    )
    age = forms.IntegerField(required=True)
    temperature = forms.IntegerField(label="Temperature (°F)",required=True)
    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=GENDER_CHOICES, required=True
    )
    symptoms = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        choices=SYMPTOMS_CHOICES
    )
    additionalInformation = forms.MultipleChoiceField(label="Additional Information",
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        choices=AdditionalInformation_CHOICES
    )

    score = forms.IntegerField(
        widget=forms.HiddenInput(), required=False
    )

    class Meta:
        model = Patient
        fields = ('age', 'gender', 'temperature', 'symptoms', 'additionalInformation')
        exclude = ('score',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Submit'))
        



