from django.db import models

class Root(models.Model):
    token = models.CharField(max_length=10, unique=True)

class Lemma(models.Model):
    """Distinct Arabic word (lemma) in the Quran"""
    token = models.CharField(max_length=50, unique=True)
    root = models.ForeignKey(Root, on_delete=models.CASCADE, null=True)


class Word(models.Model):
    """Arabic word in the Quran"""
    surah = models.IntegerField()
    ayah = models.IntegerField()
    position = models.IntegerField()
    token = models.CharField(max_length=50)
    meaning = models.CharField(max_length=50)
    lemma = models.ForeignKey('Lemma', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.surah}:{self.ayah} {self.token}({self.meaning})'

