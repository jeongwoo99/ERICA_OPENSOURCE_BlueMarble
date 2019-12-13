import random
def count_player():#플레이 할 사람수 입력
    while True:
        try:
            x = int(input("몇명?"))
            while x not in {2,3,4}:
                x = int(input("몇명?"))
            break
        except ValueError:
            continue
    return x

def change_turn():#차례 넘기기
    while True:
        try:
            x = input("차례를 넘기시려면 y를 입력해주세요.")
            while x != 'y':
                x = input("차례를 넘기시려면 y를 입력해주세요.")
            break
        except ValueError:
            continue
    if x == 'y':
        return True
    else:
        return False

def press_start():#누르면 시작
    while True:
        try:
            x = input("press start(s를 입력해주세요.)")
            while x != 's':
                x = input("press start(s를 입력해주세요.)")
            break
        except ValueError:
            continue
    if(x == 's'):
        return True
    else:
        return False

 def buy_land():#땅 사기
    while True:
        try:
            x = input("땅을 사시겠습니까? y or n")
            while x not in {'y','n'}:
                x = input("땅을 사시겠습니까? y or n")
            break
        except ValueError:
            continue
    if(x == 'y'):
        return True
    else:
        return False

def dice():#주사위 굴리기
    dice = [1,2,3,4,5,6]
    random.shuffle(dice)
    print("이번 주사위 : "+str(dice[0]))
    return dice[0]

def field():#게임 판 보여주기
    place = ['s','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
    price = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    field = []
    for i in range(0,16):
        field.append({'place':place[i],'price':price[i]})
    print("+ - - - - - +")
    print("l "+str(field[4]['place'])+" "+str(field[5]['place'])+" "+str(field[6]['place'])+" "+str(field[7]['place'])+" "+str(field[8]['place'])+" l")
    print("l "+str(field[3]['place'])+"       "+str(field[9]['place'])+" l")
    print("l "+str(field[2]['place'])+"       "+str(field[10]['place'])+" l")
    print("l "+str(field[1]['place'])+"       "+str(field[11]['place'])+" l")
    print("l "+str(field[0]['place'])+" "+str(field[15]['place'])+" "+str(field[14]['place'])+" "+str(field[13]['place'])+" "+str(field[12]['place'])+" l")
    print("+ - - - - - +")
    return field

def make_player(player):#플레이어 만들기
    player = {'where':0,'money':50}
    return player
