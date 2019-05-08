from django.shortcuts import render

# Create your views here.
from.models import Book
import xlrd


def get_data(request):
    data=Book.objects.all()
    return HttpResponse(data)