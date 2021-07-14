
x = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def isOcuppied(a):
    if x[int(a)]== ' ':
        return False
    else:
        return True
def gameisdone():

    res=False
    if x[0]==x[1] and x[0]!=' ':
        if x[1]==x[2]:
            res=True
    if x[0]==x[3] and x[0]!=' ':
        if x[3]==x[6]:
            res=True

    if x[1] == x[4] and x[1]!=' ':
        if x[4] == x[7]:
            res = True
    if x[2]==x[5] and x[2]!=' ':
        if x[5]==x[8]:
            res=True
    if x[3]==x[4] and x[3]!=' ':
        if x[4]==x[5]:
            res=True
    if x[6]==x[7] and x[6]!=' ':
        if x[7]==x[8]:
            res=True
    if x[0]==x[4] and x[0]!=' ':
        if x[4]==x[8]:
            res=True
    if x[6]==x[4] and x[6]!=' ':
        if x[4]==x[2]:
            res=True
    return res


i=1
while gameisdone()==False and i<10:
    print("|_" + str(x[0]) + "_|" + "|_" + str(x[1]) + "_|" + "|_" + str(x[2]) + "_|")
    print("|_" + str(x[3]) + "_|" + "|_" + str(x[4]) + "_|" + "|_" + str(x[5]) + "_|")
    print("|_" + str(x[6]) + "_|" + "|_" + str(x[7]) + "_|" + "|_" + str(x[8]) + "_|")
    if i%2==1:
        place =input("Player 1 please choose your placement...1-9 : ")
        x[int(place)-1] = 'X'

    else:
        place = input("Player 2 please choose your placement...1-9 : ")
        x[int(place)-1] = 'O'


    i=i+1
if i<10:
    if i%2==1:
        print('\x1b[6;30;42m'+"Game is over , Player 2 WON"+'\x1b[0m')
        print("|_" + str(x[0]) + "_|" + "|_" + str(x[1]) + "_|" + "|_" + str(x[2]) + "_|")
        print("|_" + str(x[3]) + "_|" + "|_" + str(x[4]) + "_|" + "|_" + str(x[5]) + "_|")
        print("|_" + str(x[6]) + "_|" + "|_" + str(x[7]) + "_|" + "|_" + str(x[8]) + "_|")
    else:
        print('\x1b[6;30;42m'+"Game is over , Player 1 WON"+'\x1b[0m')
        print("|_" + str(x[0]) + "_|" + "|_" + str(x[1]) + "_|" + "|_" + str(x[2]) + "_|")
        print("|_" + str(x[3]) + "_|" + "|_" + str(x[4]) + "_|" + "|_" + str(x[5]) + "_|")
        print("|_" + str(x[6]) + "_|" + "|_" + str(x[7]) + "_|" + "|_" + str(x[8]) + "_|")
else:
    print("Game is over , DRAW")

