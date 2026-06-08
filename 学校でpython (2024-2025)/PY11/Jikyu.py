# jikyukeisa

# jikyu no nyuuryoku ---(1)
user=input("jikyu ha ikuradesuka?")
jikyu=int(user)

#jikan no nyuuryoku
user=input("nanjikan hatarakimashitaka?")
jikan=int(user)

#keisan ---(2)
kyuryou=jikyu*jikan

#kekka wo hyouji ---(3)
fmt="""
jikyu{0}en deusu,{1} jikan hataraitanode...
kyuryou ha, {2}en desu.
"""

desc=fmt.format(jikyu, jikan, kyuryou)
print(desc)