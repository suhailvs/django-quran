from os import path
def path_to(fn):
    return path.join(path.dirname(__file__), fn)
    
def import_word_translations():
    f = open(path_to('quran/data/corpus/word_by_word_meaning.txt'))
    words = []

    for line in f:
        parts = line.strip().split('|')
        sura_number = 0
        try:
            sura_number = int(parts[0])
        except ValueError:
            continue
        aya_number = int(parts[1])
        word_number = int(parts[2])
        ename = parts[3]
        translation = parts[4]
        words.append([sura_number,aya_number,word_number,ename,translation])
    return words
        
data = { 
    "language": "eg", 
    "title": "Word by word translation", 
    "text": import_word_translations()
}
import json
with open('word_by_word.json', 'w') as outfile:
    json.dump(data, outfile)