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
