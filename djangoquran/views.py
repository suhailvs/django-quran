from django.shortcuts import render, get_object_or_404,get_list_or_404
from .models import Root,Lemma,Word
from django.db.models import Max

def index(request):
    surahs = [i for i in range(1,115)]
    return render(request,'djangoquran/index.html', {'surahs': surahs})

def surah(request, surah_number):
    qs = Word.objects.filter(surah=surah_number)
    total_ayahs = qs.aggregate(m=Max('ayah'))['m']
    ayahs = []
    for i in range(1,total_ayahs+1):
        ayahs.append(qs.filter(ayah=i).order_by('position'))
    
    return render(request,'djangoquran/surah.html',  {'ayahs': ayahs, 'surah':surah_number})


def word(request, surah_number, ayah_number, word_number):
    # aya = get_object_or_404(Aya, sura=sura_number, number=aya_number)
    word = get_object_or_404(Word, surah=surah_number,ayah=ayah_number, position=word_number)
    # root = word.root
    return render(request,'djangoquran/word.html', {'word': word}) #, 'root': root})
"""
def lemma(request, lemma_id):
    lemma = get_object_or_404(Lemma, pk=lemma_id)
    root = lemma.root
    words = lemma.word_set.all()
    ayas = lemma.ayas.distinct()
    return render(request,'parts/lemma.html', {'lemma': lemma, 'root': root, 'words': words, 'ayas': ayas})

def root(request, root_id):
    root = get_object_or_404(Root, pk=root_id)
    lemmas = root.lemmas.all()
    ayas = root.ayas.distinct()
    return render(request,'parts/root.html', {'root': root, 'lemmas': lemmas, 'ayas': ayas})

def root_index(request):
    roots = Root.objects.all().order_by('id')
    return render(request,'parts/root_index.html', {'roots': roots})
"""