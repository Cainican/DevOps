##############################################
#   While を用いて、１から１０までを加算するプログラム   #
##############################################

# kaikeiyou hensuu
sum=0

#kasanyou hensuu
num=1


# num wo zutu fuyashinagara sum ni kasanshite iku
# 10 made kasansuru aida kurikaesu (while)

while num<=10:
	# kurikaeshite iru aida ni okonau shori
	sum=sum+num

	# num wo 1 fuyasu
	num=num+1

# kekka wo shutsuryokusuru
print("1 kara 10 made no kasan kekka ha {0} desu.".format(sum))