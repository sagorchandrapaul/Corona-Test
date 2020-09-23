from django.db import models
from multiselectfield import MultiSelectField


class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    SYMPTOMS_CHOICES = (
        ('BP', 'Breathing Problem'),
        ('DC', 'Dry Cough'),
        ('ST', 'Sore Throat'),
        ('W', 'Weakness'),
        ('RN', 'Runny Nose'),
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
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    pub_date = models.DateField(auto_now_add=True)
    temperature = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    symptoms = MultiSelectField(max_length=255, choices=SYMPTOMS_CHOICES)
    additionalInformation = MultiSelectField(
        max_length=255,
        choices=AdditionalInformation_CHOICES
    )
    score = models.IntegerField(blank=True, null=True)

