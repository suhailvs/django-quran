from django.shortcuts import render, get_object_or_404,get_list_or_404
from quran.models import *
import re
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def index(request):
    query= request.GET.get('q')
    if query and len(query)>2: # more that two letters are allowed to search
        cur_trans = int(request.GET.get('trans',1))
        res = TranslatedAya.objects.filter(text__icontains=query,translation=cur_trans)
        return render(request,'search_result.html',{'result':res,'q':query,'cur_trans':cur_trans}) 
    return HttpResponseRedirect('/1/')
    
def sura(request, sura_number,aya_range=None):        
    cur_trans = int(request.GET.get('trans',1))
    sura = get_object_or_404(Sura, number=sura_number)
    ayas = sura.ayas.all()    
    translations = sura.translations.filter(translation__id=cur_trans)
    if aya_range:
        m = re.match('(\d{1,3}).(\d{1,3})/',aya_range)
        if m: 
            l,u = m.group(1),m.group(2)
            u = u if u > l else l # cases like 12-1
            ayas = ayas.filter(number__range=[l,u])
            translations = translations.filter(aya__number__range=[l,u])
    ayas = zip(ayas, translations)
    return render(request,'sura.html',  {'sura': sura, 'ayas': ayas,'cur_trans':cur_trans})


def aya(request, sura_number, aya_number):
    cur_trans = int(request.GET.get('trans',1))
    sura = get_object_or_404(Sura, number=sura_number)
    aya = get_object_or_404(Aya, sura=sura, number=aya_number)
    translated_aya = get_object_or_404(TranslatedAya, aya=aya, translation=cur_trans)
    words = aya.words.all()
    return render(request,'aya.html', {'sura': sura, 'aya': aya,'cur_trans':cur_trans,'translation': translated_aya, 'words': words})

##########################################
####         WORD'S ROOT      #####
##########################################
def word(request, sura_number, aya_number, word_number):
    aya = get_object_or_404(Aya, sura=sura_number, number=aya_number)
    word = get_object_or_404(Word, aya=aya, number=word_number)
    root = word.root

    if root:
        lemmas = root.lemmas.all()
        ayas = root.ayas.distinct()
        return render(request,'parts/root.html', {'root': root, 'lemmas': lemmas, 'ayas': ayas})
    return HttpResponse("UnKnown Root")