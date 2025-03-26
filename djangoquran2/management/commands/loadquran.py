from django.core.management.base import BaseCommand
from djangoquran2.models import Word, Root, Lemma
import csv
import importlib.resources
AYAHS_PER_SURAH = [
    7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110, 98, 135,
    112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88, 75, 85, 54, 53, 89, 59,
    37, 35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24, 13, 14, 11, 11, 18, 12, 12, 30, 52, 52,
    44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42, 29, 19, 36, 25, 22, 17, 19, 26, 30, 20, 15, 21, 11, 8,
    8, 19, 5, 8, 8, 11, 11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6
]

def calculate_line_number(surah, ayah):
    if 0 < surah < 115 or 0 < ayah <= AYAHS_PER_SURAH[surah - 1]:
        return sum(AYAHS_PER_SURAH[: surah - 1]) + ayah
    return None

def read_csv(fname):
    with importlib.resources.files("djangoquran2.datas").joinpath(fname).open("r") as f:
        return list(csv.reader(f))

class Command(BaseCommand):
    help = "Quran commands"

    def handle(self, *args, **options):
        # Word.objects.all().delete()
        
        self.stdout.write('Loading lemmas and roots...')
        if Lemma.objects.exists() or Root.objects.exists():
            self.stdout.write('lemmas or roots table is not empty')
        else:
            objs = []
            lemmas = read_csv("lemmas.csv")            
            for lemma in lemmas:
                root,_= Root.objects.get_or_create(token=lemma[1])
                objs.append(Lemma(token=lemma[0],root=root))
            self.stdout.write('Running bulk create...')
            Lemma.objects.bulk_create(objs)
            self.stdout.write('Lemmas and roots completed')


        # Words
        self.stdout.write('Loading words...')
        if Word.objects.exists():
            self.stdout.write('Word table is not empty')
        else:            
            objs = []
            words_list = read_csv("words.csv")  
            for surah in range(1,115):
                self.stdout.write(f'Loading surah {surah} of 114...')
                for ayah in range(1,AYAHS_PER_SURAH[surah - 1]+1):
                    lineno = calculate_line_number(surah, ayah)-1 # since index starts with zero
                    for position,word in enumerate(words_list[lineno]):
                        token,meaning,lemma = word.split('|')
                        lobj = Lemma.objects.get(token=lemma)
                        objs.append(Word(surah=surah,ayah=ayah,
                            position=position+1, token=token,meaning=meaning, lemma=lobj))
            self.stdout.write('Running bulk create...')
            Word.objects.bulk_create(objs)
            self.stdout.write('Words completed')