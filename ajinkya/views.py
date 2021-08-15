from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Quotes
# Create your views here.
def index(request):
    quotes = Quotes.objects.all()
    return render(request, 'ajinkya/index.html', {'quotes':quotes})
