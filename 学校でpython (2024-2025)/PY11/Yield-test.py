############################
#   P. 144 自作イテレータ   #
#      yield-test.py       #
############################

def gen1to3():
    yield 1;    # リストを生成する
    yield 2;
    yield 3;

it = gen1to3()
for i in it:    # リスト (1, 2 ,3)を出力する
    print(i)