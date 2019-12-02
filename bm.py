import random
def count_player():
	while True:
		try:
			x = int(input("몇명?"))
			while x not in {2,3,4}:
				x = int(input("몇명?"))
			break
		except ValueError:
			continue
	return x

def dice():
	dice = [1,2,3,4,5,6]
	random.shuffle(dice)
	print("이번 주사위 : "+str(dice[0]))
	return dice[0]

def field():
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

def make_player(player):
	player = {'where':0,'money':50}
	return player

def info_player(player):
	if(player['where'] >= 16):
		player['where'] -= 16
		player['money'] += 30
	print("현재 위치 : "+chr(player['where'] + 96))
	print("보유 돈 : "+str(player['money']))

def game():
	player_list = []
	count = count_player()
	if(count == 2):
		player1 = set()
		player2 = set()
		player_list.append(make_player(player1))
		player_list.append(make_player(player2))
	elif(count == 3):
		player1 = set()
		player2 = set()
		player3 = set()
		player_list.append(make_player(player1))
		player_list.append(make_player(player2))
		player_list.append(make_player(player3))
	else:
		player1 = set()
		player2 = set()
		player3 = set()
		player4 = set()
		player_list.append(make_player(player1))
		player_list.append(make_player(player2))
		player_list.append(make_player(player3))
		player_list.append(make_player(player4))

	rchk = 0
	while(rchk < count):
		field()
		print("\n")
		for i in range(1,count+1):
			print("player"+str(i))
			info_player(player_list[i-1])
		print("\n")
		a = dice()
		print("\n")
		player_list[0]['where'] += a
		for i in range(1,count+1):
			print("player"+str(i))
			info_player(player_list[i-1])
		rchk += 1

game()
