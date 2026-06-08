#######################
#   List-kakugen.py   #
#######################

import random

# kakugen wo risuto ni tainyuu ---(1)
kakugen = ["nou aru takagatsume wo kakusu", "buta ni shiju", "nito wo oumono ha itto wo mo ezu", "tataki tsudzuke nasai. sousureba akaremasu."]

# randamu ni suuchi wo 1 tsu erabu --- (2)
i = random.randint(0,len(kakugen)-1)

# eranda kakugen wo hyoujisuru --- (3)
print(kakugen[i])