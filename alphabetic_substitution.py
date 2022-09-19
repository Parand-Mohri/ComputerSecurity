from collections import OrderedDict
from operator import itemgetter

text = "LYMBXJXKBBKBJPJJBBKBJPZPHYXNJKGOLOGPIEYHKBIXJSOEPVJBPMBXJEPONKBIEJGJOEATPYOXUOBAJPTJLKJDXGYLOEPKLKAKODKBPJDDKIJBAJXOPOGAKJBAJAYVSMPJEGAKJBAJOSSDKJXVOPTJVOPKAGOBXEYFYPKAGLMEPTJEVYEJXNJVOKBPOKBGODOEIJBJPHYENYLKBXMGPEZSOEPBJEGPTEYMITPTJOHOEXHKBBKBINJHYENSEYIEOVVJOBXPTEYMITYMEEJGJOEATAYDDOFYEOPKYBGPTJXJSOEPVJBPSEYUKXJGJXMAOPKYBPTEYMITYBJFOATJDYEGSEYIEOVVJOBXPHYVOGPJEGSEYIEOVVJGEJGJOEATOPPTJXJSOEPVJBPYLXOPOGAKJBAJOBXNBYHDJXIJJBIKBJJEKBIGSOBGPTJXKGAKSDKBJGOBXKBPJELOAJGYLOEPKLKAKODKBPJDDKIJBAJXOPOGAKJBAJAYVSMPJEGAKJBAJOBXOSSDKJXVOPTJVOPKAGHJXJUJDYSBJHPYYDGOBXVJPTYXYDYIKJGPYOXUOBAJPTJGJLKJDXGOPPTJGOVJPKVJHJAYDDOFYEOPJHKPTOHKXJEOBIJYLKBGPKPMPJGFYPTHKPTKBOBXYMPGKXJYLVOOGPEKATPMBKUJEGKPZOBXHYENYBXKUJEGJOSSDKAOPKYBGKBADMXKBIKBPTJLKJDXGYLTJODPTOBXVJXKAKBJDYIKGPKAGFKYDYIZOEPSTZGKAGAZFJEGJAMEKPZBJMEYGAKJBAJOBXJXMAOPKYB"
letterFrequency = ['E', 'T', 'A','O','I','N','S','R','H','D','L','U','C','M','F','Y','W','G','P','B','V','K','X','Q','J','Z' ]
# letterFrequency = ['E', 'T', 'A','O','I','N','S','R','H','D','L','U','C','M','F','Y','W','G','P','B','V','K','X','Q','J','Z' ]
all_freq = {}

for i in text:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

all_freq = sorted(all_freq.items(), key=itemgetter(1))
res = OrderedDict(reversed(all_freq))
print(res)
n_text = " "
for x in text:
    n_text += letterFrequency[list(res.keys()).index(x)]

print(n_text)
