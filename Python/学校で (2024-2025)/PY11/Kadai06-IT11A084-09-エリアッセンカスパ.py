#############################################
#   課題06-PY11A084-09-エリアッセン カスパ   #
#############################################


points = [50,65,12,98,71,86,27,60]

name = input("リスト名を入力: ")

while name != "points":
    print("リスト名が違います")
    name = input("リスト名を入力: ")

for score in points:
    print(score,end = "\t")

sum_list = sum(points)
list_avg = sum_list/len(points)

print("\n\n平均点: {0}".format(list_avg))


# 平均以上
abv_avg = [p for p in points if p > list_avg]

print("\n平均以上")

# 平均以上のスコアを表示する
for score in abv_avg:
    print(score, end = "\t")
print()

print("\n最高点: ",max(points))
print("最低点: ",min(points))