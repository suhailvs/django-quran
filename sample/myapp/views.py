from django.shortcuts import render, get_object_or_404,get_list_or_404
from quran.models import *
import re
# Create your views here.
def index(request):
    if 'q' in request.GET:
        res = TranslatedAya.objects.filter(text__icontains=request.GET['q'])
        return render(request,'search.html',{'result':res}) 
    suras = get_list_or_404(Sura)
    return render(request,'index.html', {'suras': [suras[:38],suras[38:76],suras[76:]]})

def root_index(request):
    roots = Root.objects.all().order_by('letters')
    return render(request,'root_index.html', {'roots': roots})
    
def sura(request, sura_number,aya_range=None):        
    cur_trans = int(request.GET.get('trans',1))
    sura = get_object_or_404(Sura, number=sura_number)
    ayas = sura.ayas.all()
    trans = get_list_or_404(QuranTranslation)
    translations = sura.translations.filter(translation__id=cur_trans)
    if aya_range:
        m = re.match('(\d{1,3}).(\d{1,3})/',aya_range)
        if m: 
            l,u = m.group(1),m.group(2)
            u = u if u > l else l # cases like 12-1
            ayas = ayas.filter(number__range=[l,u])
            translations = translations.filter(aya__number__range=[l,u])
    ayas = zip(ayas, translations)
    return render(request,'sura.html',  {'sura': sura, 'ayas': ayas,'trans':trans,'cur_trans':cur_trans})


def aya(request, sura_number, aya_number, translation=1):
    sura = get_object_or_404(Sura, number=sura_number)
    aya = get_object_or_404(Aya, sura=sura, number=aya_number)
    translated_aya = get_object_or_404(TranslatedAya, aya=aya, translation=translation)
    words = aya.words.all()
    return render(request,'aya.html', {'sura': sura, 'aya': aya, 'translation': translated_aya, 'words': words})

##########################################
####         PARTS OF PAGE AYA       #####
##########################################
from django.shortcuts import HttpResponse
def word(request, sura_number, aya_number, word_number):
    aya = get_object_or_404(Aya, sura=sura_number, number=aya_number)
    word = get_object_or_404(Word, aya=aya, number=word_number)
    root = word.root

    if root:
        lemmas = root.lemmas.all()
        ayas = root.ayas.distinct()
        return render(request,'parts/root.html', {'root': root, 'lemmas': lemmas, 'ayas': ayas})
    return HttpResponse("UnKnown Root")#render(request,'parts/word.html', {'word': word, 'aya': aya, 'root': root})

def lemma(request, lemma_id):
    lemma = get_object_or_404(Lemma, pk=lemma_id)
    root = lemma.root
    words = lemma.word_set.all()
    ayas = lemma.ayas.distinct()
    return render(request,'parts/lemma.html', {'lemma': lemma, 'root': root, 'words': words, 'ayas': ayas})
############ / PARTS ####################

def root(request, root_id):
    root = get_object_or_404(Root, pk=root_id)
    lemmas = root.lemmas.all()
    ayas = root.ayas.distinct()
    return render(request,'parts/root.html', {'root': root, 'lemmas': lemmas, 'ayas': ayas})