# karatto kara guramu ni henkansuru
# henkan no gen ni naru atai
per_ct=0.2

# yu-za- kara nyuuryoku wo eru
user=input("nani karatto desuka?")

# fudou shoutensuu ni henkansuru
ct=float(user)

#keisansuru
g=ct*per_ct

#kekka wo hyouji
desc="{0}karatto={1}guramu".format(ct,g)
print(desc)