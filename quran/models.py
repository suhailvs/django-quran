from django.db import models
from django.utils.safestring import mark_safe

from quran.buckwalter import *


class Sura(models.Model):
    """Sura (chapter) of the Quran"""

    REVELATION_CHOICES = (
        ('Meccan', 'Meccan'),
        ('Medinan', 'Medinan'),
    )

    number = models.IntegerField(primary_key=True, verbose_name='Sura Number')
    name = models.CharField(max_length=50, verbose_name='Sura Name')
    tname = models.CharField(max_length=50, verbose_name='English Transliterated Name')
    ename = models.CharField(max_length=50, verbose_name='English Name')
    order = models.IntegerField(verbose_name='Revelation Order')
    type = models.CharField(max_length=7, choices=REVELATION_CHOICES, verbose_name='')
    rukus = models.IntegerField(verbose_name='Number of Rukus')
    bismillah = models.CharField(max_length=50, blank=True, verbose_name='Bismillah')

    class Meta:
        ordering = ['number']

    @models.permalink
    def get_absolute_url(self):
        return ('quran_sura', [str(self.number)])

    def __str__(self):
        return self.tname

    def __unicode__(self):
        return self.name


class Aya(models.Model):
    """Aya (verse) of the Quran"""

    number = models.IntegerField(verbose_name='Aya Number')
    sura = models.ForeignKey(Sura, related_name='ayas')
    text = models.TextField(blank=False)

    class Meta:
        unique_together = (('number', 'sura'))
        ordering = ['sura', 'number']

    def end_marker(self):
        return mark_safe('&#64831;&#1633;&#64830;')

    @models.permalink
    def get_absolute_url(self):
        return ('quran_aya', [str(self.sura_id), str(self.number)])

    def __str__(self):
        return unicode_to_buckwalter(self.text)

    def __unicode__(self):
        return self.text


class QuranTranslation(models.Model):
    """Metadata relating to a translation of the Quran"""
    name = models.CharField(blank=False, max_length=50)
    translator = models.CharField(blank=False, max_length=50)
    source_name = models.CharField(blank=False, max_length=50)
    source_url = models.URLField(blank=False)

    def __unicode__(self):
        return self.name


class TranslatedAya(models.Model):
    """Translation of an aya"""
    sura = models.ForeignKey(Sura, related_name='translations')
    aya = models.ForeignKey(Aya, related_name='translations')
    translation = models.ForeignKey(QuranTranslation)
    text = models.TextField(blank=False)

    class Meta:
        unique_together = (('aya', 'translation'))
        ordering = ['aya']

    def __unicode__(self):
        return self.text


class Root(models.Model):
    """Root word"""

    letters = models.CharField(max_length=10, unique=True) # to my knowledge, there is no root with more than 7 letters
    ayas = models.ManyToManyField(Aya, through='Word')

    @models.permalink
    def get_absolute_url(self):
        return ('quran_root', [str(self.id)])

    def __str__(self):
        return unicode_to_buckwalter(self.letters)

    def __unicode__(self):
        return ' '.join(self.letters)


class Lemma(models.Model):
    """Distinct Arabic word (lemma) in the Quran"""
    token = models.CharField(max_length=50, unique=True)
    root = models.ForeignKey(Root, null=True, related_name='lemmas')
    ayas = models.ManyToManyField(Aya, through='Word')

    class Meta:
        ordering = ['token']

    @models.permalink
    def get_absolute_url(self):
        return ('quran_lemma', [str(self.id)])

    def __str__(self):
        return unicode_to_buckwalter(self.token)

    def __unicode__(self):
        return self.token

class Word(models.Model):
    """Arabic word in the Quran"""

    sura = models.ForeignKey(Sura, related_name='words')
    aya = models.ForeignKey(Aya, related_name='words')
    number = models.IntegerField()
    token = models.CharField(max_length=50)
    root = models.ForeignKey(Root, null=True, related_name='words')
    lemma = models.ForeignKey(Lemma)
    ename = models.CharField(max_length=50, blank=True)
    translation = models.CharField(max_length=200,blank=True)

    class Meta:
        unique_together = (('aya', 'number'))
        ordering = ['number']

    @models.permalink
    def get_absolute_url(self):
        return ('quran_word', [str(self.sura_id), str(self.aya.number), str(self.number)])

    def __str__(self):
        return unicode_to_buckwalter(self.token)

    def __unicode__(self):
        return self.token