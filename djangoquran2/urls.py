from django.urls import path
from . import views

app_name = "djangoquran2"
urlpatterns = [
    path("", views.surah, name="quran_surah"),
    path("words/<int:word_id>/", views.word, name="quran_word"),
    path("root_words/", views.root_list, name="quran_root_list"),
    path("root_words/<int:root_id>/", views.root, name="quran_root"),
]
