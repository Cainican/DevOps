####################################################
#   While を用いて、1から10までの偶数だけ加算するプログラム	   #
#   		Whilepractice2.py		   #
####################################################

sum=0
num=1

# num wo 1 zutu fuyashinagara sum ni kasanshite iku
# 10 made kasansuru aida kurikaesu (while)

while num<=10:
	# kurikaeshite iru aida ni okonau whori
	# 偶数か?
	if num % 2==0:
		# 偶数なので sum に加算
		sum=sum+num

	# tsugi no atai no jyunbi
	num=num+1

# kekka wo shutsuryokusuru
print(" 1 kara 10 made no guuzuu no kasan kekka ha {0} desu.".format(sum))