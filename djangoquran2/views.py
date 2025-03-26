from django.shortcuts import render
from .models import Root, Word
from django.db.models import Max, Case, When, Value, CharField
from djangoquran2.buckwalter import LETTERS_ONLY


def surah(request):
    if request.method == "POST":
        qs = Word.objects.filter(surah=request.POST.get("surah_number"))
        total_ayahs = qs.aggregate(m=Max("ayah"))["m"]
        ayahs = [
            qs.filter(ayah=i).order_by("position") for i in range(1, total_ayahs + 1)
        ]
        return render(request, "djangoquran2/surah.html", {"ayahs": ayahs})
    return render(request, "djangoquran2/index.html", {"surahs": list(range(1, 115))})


def word(request, word_id):
    word = Word.objects.get(id=word_id)
    return render(request, "djangoquran2/word.html", {"word": word})


def root_list(request):
    conditions = [When(token__startswith=l, then=Value(l)) for l in LETTERS_ONLY]
    letter_group = Case(*conditions, default=Value("Other"), output_field=CharField())
    roots = Root.objects.values("token", "id").annotate(group=letter_group)
    root_group = {l: roots.filter(group=l) for l in LETTERS_ONLY}
    return render(request, "djangoquran2/root_list.html", {"roots": root_group})


def root(request, root_id):
    words = Word.objects.filter(lemma__root_id=root_id)
    return render(request, "djangoquran2/root.html", {"words": words})
