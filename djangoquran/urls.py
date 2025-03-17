from django.urls import path
from . import views

app_name = "djangoquran"
urlpatterns = [
    path("", views.index, name="quran_index"),
    path("<int:surah_number>/", views.surah, name="quran_surah"),
    # path("<int:sura_number>/<int:aya_number>/", views.aya, name="quran_aya"),
    path(
        "<int:surah_number>/<int:ayah_number>/<int:word_number>/",
        views.word,
        name="quran_word",
    ),
    # path("lemma/<int:lemma_id>/", views.lemma, name="quran_lemma"),
    # path("root/<int:root_id>/", views.root, name="quran_root"),
    # path("root/", views.root_index, name="quran_root_list"),
]
