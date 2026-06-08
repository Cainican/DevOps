##########################
#   課題01-IT11A084-09   #
##########################

import datetime

# 年
def year():
    try:
        userYear = int(input("生年月日の西暦(1900～2024): "))
        if userYear >= 1900 and userYear <= 2024:
            return userYear
        
        else:
            print("有効な数値を入力してください\n")
            return year()
    
    except ValueError:
        print("数値を入力してください\n")
        return year()

# 月
def month():
    try:
        userMonth = int(input("生年月日の月(1～12): "))
        if userMonth >=1 and userMonth <= 12:
            return userMonth
        
        else:
            print("有効な数値を入力してください\n")
            return month()
    
    except ValueError:
        print("数値を入力してください\n")
        return month()

# 日
def day():
    try:
        userDay = int(input("生年月日の日(1～31): "))
        if userDay >= 1 and userDay <= 31:
            return userDay
        
        else:
            print("有効な数値を入力してください\n")
            return day()
    
    except ValueError:
        print("数値を入力してください\n")
        return day()


y = year()

m = month()

d = day()



# 生年月日を入力 (生年月日を datetime.date で作成)
t1 = datetime.date(y, m, d)

# 本日を入力
t2 = datetime.date.today()

# 生まれたから今日まで計算
past = t2 - t1

print("\n生年月日: ", t1.strftime("%Y/%m/%d"))
print("今日: ", t2.strftime("%Y/%m/%d"))
print("生まれてから", past.days, "日経ちました!")