# tables.py
import django_tables2 as tables
from .models import Titanic


class TitanicTable(tables.Table):
    class Meta:
        model = Titanic
        template_name = "django_tables2/bootstrap.html"

        fields = (
            'passengerID', 'survived', 'pclass', 'name', 'sex', 'age', 'sibsp', 'parch', 'ticket', 'fare', 'cabin',
            'embarked')
