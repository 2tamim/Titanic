import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TitanicUploadForm
from .models import Titanic
from .tables import TitanicTable
from django_tables2 import RequestConfig
from .forms import TitanicForm
from django.contrib import messages


def upload_file(request):
    if request.method == 'POST':
        form = TitanicUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file, engine='openpyxl')

            created_count = 0
            duplicate_count = 0

            for _, row in df.iterrows():
                passenger_id = row['PassengerId']

                
                if not Titanic.objects.filter(passengerID=passenger_id).exists():
                    Titanic.objects.create(
                        passengerID=passenger_id,
                        survived=row['Survived'],
                        pclass=row['Pclass'],
                        name=row['Name'],
                        sex=row['Sex'],
                        age=row['Age'],
                        sibsp=row['SibSp'],
                        parch=row['Parch'],
                        ticket=row['Ticket'],
                        fare=row['Fare'],
                        cabin=row.get('Cabin', ''),
                        embarked=row['Embarked']
                    )
                    created_count += 1
                else:
                    duplicate_count += 1

            
            if created_count > 0:
                messages.success(request, f'{created_count} records have been added successfully.')
            if duplicate_count > 0:
                messages.warning(request, f'{duplicate_count} records were duplicates and not added.')

            return redirect('success')
    else:
        form = TitanicUploadForm()

    return render(request, 'upload.html', {'form': form})


def upload_success(request):
    return render(request, 'success.html')


def titanic_list(request):
    queryset = Titanic.objects.all()
    table = TitanicTable(queryset)
    RequestConfig(request).configure(table)
    return render(request, 'titanic_list.html', {'table': table})


def passenger_create_or_update(request, pk=None):
    if pk:
        passenger = get_object_or_404(Titanic, pk=pk)
    else:
        passenger = None

    if request.method == 'POST':
        form = TitanicForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            return redirect('titanic_list')
    else:
        form = TitanicForm(instance=passenger)

    return render(request, 'passenger_form.html', {'form': form})


def passenger_edit(request, pk):
    passenger = get_object_or_404(Titanic, pk=pk)
    if request.method == 'POST':
        form = TitanicForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            messages.success(request, 'Passenger updated successfully.')
            return redirect('titanic_list')
    else:
        form = TitanicForm(instance=passenger)
    return render(request, 'passenger_form.html', {'form': form})


def passenger_delete(request, pk):
    passenger = get_object_or_404(Titanic, pk=pk)
    if request.method == 'POST':
        passenger.delete()
        messages.success(request, 'Passenger deleted successfully.')
        return redirect('titanic_list')
    return render(request, 'passenger_confirm_delete.html', {'passenger': passenger})
