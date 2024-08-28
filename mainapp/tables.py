import django_tables2 as tables
from django.urls import reverse_lazy
from .models import Titanic

class TitanicTable(tables.Table):
    edit = tables.TemplateColumn(
        '<a href="{% url "passenger_edit" record.pk %}" class="btn btn-warning btn-sm">Edit</a>',
        orderable=False
    )
    delete = tables.TemplateColumn(
        '<a href="{% url "passenger_delete" record.pk %}" class="btn btn-danger btn-sm">Delete</a>',
        orderable=False
    )

    class Meta:
        model = Titanic
        template_name = "django_tables2/bootstrap.html"
        fields = ("passengerID", "name", "pclass", "sex", "age", "sibsp", "parch", "ticket", "fare", "cabin", "embarked", "edit", "delete")
