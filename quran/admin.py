from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Sura)
admin.site.register(Aya)
admin.site.register(QuranTranslation)


admin.site.register(TranslatedAya)
admin.site.register(Root)
admin.site.register(Lemma)
admin.site.register(Word)