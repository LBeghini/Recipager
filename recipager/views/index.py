from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse

from ..models import Ingredient


def index(request):
    return render(request, 'recipager/index.html')
