from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import FormView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_tables2 import SingleTableView
import pandas as pd
from .models import Titanic
from .forms import UploadFileForm, TitanicForm
from .tables import TitanicTable


class UploadFileView(FormView):
    template_name = 'upload.html'
    form_class = UploadFileForm

    def form_valid(self, form):
        # Retrieve the uploaded Excel file
        excel_file = self.request.FILES['file']
        # Use pandas to read the Excel file
        df = pd.read_excel(excel_file, )

        # Iterate over the rows and save each record to the database

        for _, row in df.iterrows():
            try:
                Titanic.objects.create(
                    passengerID=row['PassengerId'],
                    survived=row['Survived'],
                    pclass=row['Pclass'],
                    name=row['Name'],
                    sex=row['Sex'],
                    age=row['Age'],
                    sibsp=row['SibSp'],
                    parch=row['Parch'],
                    ticket=row['Ticket'],
                    fare=row['Fare'],
                    cabin=row.get('Cabin', None),
                    embarked=row['Embarked']
                )
            except Exception as e:
                print(row)
                raise e

        return redirect('titanic_list')


class TitanicListView(ListView):
    model = Titanic
    template_name = 'titanic_list.html'
    context_object_name = 'titanic_data'


class TitanicCreateView(CreateView):
    model = Titanic
    form_class = TitanicForm
    template_name = 'titanic_form.html'
    success_url = reverse_lazy('titanic_list')


class TitanicUpdateView(UpdateView):
    model = Titanic
    form_class = TitanicForm
    template_name = 'titanic_form.html'
    success_url = reverse_lazy('titanic_list')


class TitanicDeleteView(DeleteView):
    model = Titanic
    template_name = 'titanic_confirm_delete.html'
    success_url = reverse_lazy('titanic_list')


class TitanicTableView(SingleTableView):
    model = Titanic
    table_class = TitanicTable
    template_name = 'titanic_table.html'
