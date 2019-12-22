import random
import time
def count_player():#플레이 할 사람수 입력
    while True:
        try:
            x = int(input("몇명?"))
            while x not in {2,3,4}:
                x = int(input("몇명?a"))
            break
        except ValueError:
            continue
    return x

def count_computer():
    if (count_player()) == 4:
        print("너무 많은 사람들이 참여하기 때문에 AI는 없습니다.")
    while (count_player() < 4):
        try:
            x = int(input("얼마나 많은 ai를 원합니까?"))
            while (x + count_player()) > 4:
                x = int(input("너무 많아요.",str(4-x)+"보다 적게 해 주세요."))
            break
        except ValueError:
            continue
    return x

def change_turn():#차례 넘기기
    while True:
        try:
            x = input("차례를 넘기시려면 y를 입력해주세요. ")
            while x != 'y':
                x = input("차례를 넘기시려면 y를 입력해주세요. ")
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
            x = input("땅을 사시겠습니까? (y or n) ")
            while x not in {'y','n'}:
                x = input("땅을 사시겠습니까? (y or n) ")
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
    time.sleep(0.5)
    place = ['s','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
    price = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    field = []
    for i in range(0,16):
        field.append({'place':place[i],'price':price[i]})
    print("+ - - - - - +")
    print("| "+str(field[4]['place'])+" "+str(field[5]['place'])+" "+str(field[6]['place'])+" "+str(field[7]['place'])+" "+str(field[8]['place'])+" |")
    print("| "+str(field[3]['place'])+"       "                                                                           +str(field[9]['place'])+" |")
    print("| "+str(field[2]['place'])+"       "                                                                          +str(field[10]['place'])+" |")
    print("| "+str(field[1]['place'])+"       "                                                                          +str(field[11]['place'])+" |")
    print("| "+str(field[0]['place'])+" "+str(field[15]['place'])+" "+str(field[14]['place'])+" "+str(field[13]['place'])+" "+str(field[12]['place'])+" |")
    print("+ - - - - - +")
    return field

def make_player(player):#플레이어 만들기
    player = {'before_where':0,'where':0,'money':50, 'alive':1, 'total':50}
    return player

def info_player(player):#플레이어 정보 출력
    if(player['where'] >= 16):
        player['where'] -= 16
        player['money'] += 30
        player['total'] += 30
    if(player['before_where'] == 0):
        player['before_where'] == 's'
    if(player['where'] != player['before_where']):
        if(player['where'] == 0):
            print("현재 위치 :",chr(player['before_where']+96),">>> s")
        else:
            if(player['before_where'] == 0):
                print("현재 위치 : s",">>>",chr(player['where']+96))
            else:
                print("현재 위치 :",chr(player['before_where']+96),">>>",chr(player['where']+96))
    else:
        if(player['where'] == 0):
            print("현재 위치 :"," s")
        else:
            print("현재 위치 :",chr(player['where']+96))
    player['before_where'] = player['where']
    print("보유 돈 : "+str(player['money']))
    print("총 액 : "+str(player['total']))

def the_end(player, cnt_p):
    if(player['money'] < 0):
        player['alive'] = 0
        cnt_p -= 1

def game():
    player_list = []
    buyland_list = []
    allland_list = []
    countp = count_player()
    cnt_p = countp
    count = countp
    for x in range(1, countp + 1):
        playerx = set()
        player_list.append(make_player(playerx))
    for i in range(countp):
        buyland_list.append([])
    start = press_start()
    while(start != True):
        start = press_start()
    game_round = 1
    while(game_round < 30):
        turn = 1
        while(turn < count+1):
            print("-----------------\n현재 라운드 : "+str(game_round))
            game_field = field()
            print("현재 차례 : player"+str(turn))
            time.sleep(1.5)
            go = dice()
            print("\n")
            player_list[turn-1]['where'] += go
            for i in range(1,count+1):
                print("player"+str(i))
                info_player(player_list[i-1])
                print("땅:",buyland_list[i-1],"\n")
            a = player_list[turn-1]['where']
            if game_field[a]['place'] not in allland_list:
                if(player_list[turn-1]['where'] != 0):
                    if(player_list[turn-1]['money'] < game_field[a]['price']):
                        print("돈이 부족해서 땅을 살 수 없습니다.")
                    else:
                        if(buy_land()):
                            buyland_list[turn-1].append(game_field[a]['place'])
                            player_list[turn-1]['money'] -= game_field[a]['price']
                            allland_list.append(game_field[a]['place'])
                else: print("출발점에 도착했습니다.")
            else:#누군가가 가지고 있다면
                for i in range(count):
                    if(game_field[a]['place'] in buyland_list[i]):
                        owner = i
                if(turn-1 == owner):
                    print("이미 소유한 땅입니다.")
                else:
                    print("player"+str(owner+1)+" 땅입니다.")
                    print("player"+str(owner+1)+"에게 "+str(game_field[a]['price']*2)+"원을 지불합니다.")
                    player_list[turn-1]['money'] -= game_field[a]['price'] * 2
                    player_list[turn-1]['total'] -= game_field[a]['price'] * 2
                    player_list[owner]['money'] += game_field[a]['price'] * 2
                    player_list[owner]['total'] += game_field[a]['price'] * 2
            next_turn = change_turn()
            while(next_turn != True):
                next_turn = change_turn()
            turn += 1
        game_round += 1
    print("게임이 종료되었습니다.")
    winner = 0
    for x in range(count-1):
        if(player_list[x]['total'] >= player_list[winner]['total']):
            winner = x+1
    if(winner %2 == 1):
        print("player"+str(winner+1)+"이 이 게임에서 이겼어요!")
    else:
        print("player"+str(winner+1)+"가 이 게임에서 이겼어요!")

game()
