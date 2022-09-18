import copy
import itertools


class Player:
    win_num = 0
    game_num = 0
    win_rate = 0
    name = ""


def main():
    all_player_list = []
    Player_1 = Player()
    Player_1.name = "utsubo"
    all_player_list.append(Player_1)
    Player_2 = Player()
    Player_2.name = "haruto"
    all_player_list.append(Player_2)
    Player_3 = Player()
    Player_3.name = "hiyokome"
    all_player_list.append(Player_3)
    Player_4 = Player()
    Player_4.name = "musyamusya"
    all_player_list.append(Player_4)
    Player_5 = Player()
    Player_5.name = "kusomegane"
    all_player_list.append(Player_5)
    Player_6 = Player()
    Player_6.name = "mizu"
    all_player_list.append(Player_6)
    Player_7 = Player()
    Player_7.name = "kene"
    all_player_list.append(Player_7)
    Player_8 = Player()
    Player_8.name = "nusupi"
    all_player_list.append(Player_8)
    Player_9 = Player()
    Player_9.name = "sena"
    all_player_list.append(Player_9)
    #Player_10 = Player()
    #Player_10.name = "j"
    # all_player_list.append(Player_10)

    observer_1 = input("観戦者1の名前 : ")
    observer_2 = input("観戦者2の名前 : ")

    player_list = copy.deepcopy(all_player_list)

    # for p in Player_dict:

    # all_player_list_

    observer_list = []
    if (observer_1 != ""):
        for i in range(len(all_player_list)):
            if (player_list[i].name == observer_1):
                player_list.pop(i)
                break

    if (observer_2 != ""):
        for i in range(len(all_player_list)):
            if (player_list[i].name == observer_2):
                player_list.pop(i)
                break

    player_list_c = copy.deepcopy(player_list)
    for team_A in itertools.combinations(player_list, 4):
        #print("team A : ", team_A[0].name,
        #      team_A[1].name, team_A[2].name, team_A[3].name)
        team_B = []
        for player in player_list:
            if (player.name != team_A[0].name and
                player.name != team_A[1].name and
                player.name != team_A[2].name and
                player.name != team_A[3].name):
                team_B.append(player)
        #print("team B : ", team_B[0].name,
        #      team_B[1].name, team_B[2].name, team_B[3].name)


main()
