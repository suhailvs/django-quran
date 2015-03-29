from django.shortcuts import render, get_object_or_404,get_list_or_404
from quran.models import Sura, Aya,TranslatedAya
# Create your views here.
def index(request):
    suras = get_list_or_404(Sura)
    return render(request,'index.html', {'suras': [suras[:38],suras[38:76],suras[76:]]})