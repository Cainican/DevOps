import random

count = 0

# To make use the are only 3 numbers in the list
# The numbers are in the []
def userInput(n):
    user = list(input("3桁数値を入力(999: 終了): "))
    if len(user) != 3:
        userInput(n)
    
    elif user == ["9","9","9"]:
        return "finish"
    
    else:
        eat = 0
        bite = 0
        before = -1

        # The random number is being reused
        for i in user:
            if i in n:
                if i == before:
                    continue
                
                # Indicates the placement of the number in the list
                # If there's two of the same number, it will call it out
                # Gets plus one, bc the number is correct
                elif user.index(i) == n.index(i):
                    eat += 1
                
                # Gets plus one, bc a number and placement are correct
                else:
                    bite +=1
                
                # Make sure the numbers are different,
                # and you can guess the numbers and placement better
                before = i
            
    if eat == 3:
        return "correct"
            
    # Eat and bite will come out a line further down, make it look cleaner
    # format and print shows the the results
    # If you have a number correct, or if you have the number and placement correct
    else:
        str = '''
    EAT = {0}
    BITE = {1}
'''.format(eat,bite)
        print(str)
        return False

# Make sure the numbers are in the []
randnum = []

# To make sure the numbers are different
while True:
    n = str(random.randint(0,9))
    if (n in randnum) == False:
        randnum.append(n)
    
    # To make sure there are only 3 numbers
    if len(randnum) == 3:
        break

# If the user inputs 999, the game is done/finished
while True:
    count += 1
    judged = userInput(randnum)
    if judged == "finish":
        print("終了")
        break

    elif judged == "correct":
        str = '''
    お見事!
    正解は{0}でした!
    試行回数: {1}
'''.format(''.join(randnum),count)
        print(str)
        break