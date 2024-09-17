from django.db import models
from common.models import BaseModel


class Titanic(BaseModel):
    class SexChoices(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
        OTHER = 'other', 'Other'

    class EmbarkedChoices(models.TextChoices):
        CHERBOURG = 'C', 'Cherbourg'
        SOUTHAMPTON = 'S', 'Southampton'
        QUEENSTOWN = 'Q', 'Queenstown'
        NOT_KNOWN = 'NaN', 'Not Known'

    passengerID = models.IntegerField(primary_key=True)
    survived = models.BooleanField()  # 0 = not survived, 1 = survived
    pclass = models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third')])
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=SexChoices.choices)
    age = models.FloatField(null=True, blank=True)
    sibsp = models.IntegerField()  # Siblings/Spouses aboard
    parch = models.IntegerField()  # Parents/Children aboard
    ticket = models.CharField(max_length=20)
    fare = models.FloatField()
    cabin = models.CharField(max_length=20, null=True, blank=True)
    embarked = models.CharField(max_length=3, choices=EmbarkedChoices.choices)

    def __str__(self):
        return self.name
