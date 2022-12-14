import Player
import itertools

def get_win_team():
    win_team = input("勝ったチーム : ")
    if (win_team == "A" or win_team == "B" or win_team == "a" or win_team == "b"):
        return win_team
    else:
        return get_win_team()


def decide_team():
    player_list = []
    Player_1 = Player("utsubo")
    player_list.append(Player_1)
    Player_2 = Player("haruto")
    player_list.append(Player_2)
    Player_3 = Player("hiyokome")
    player_list.append(Player_3)
    Player_4 = Player("musyamusya")
    player_list.append(Player_4)
    Player_5 = Player("kusomegane")
    player_list.append(Player_5)
    Player_6 = Player("mizu")
    player_list.append(Player_6)
    Player_7 = Player("kene")
    player_list.append(Player_7)
    Player_8 = Player("nusupi")
    player_list.append(Player_8)
    Player_9 = Player("sena")
    player_list.append(Player_9)
    #Player_10 = Player("")
    # player_list.append(Player_10)

    while (True):
        observer_1_name = ""
        observer_2_name = ""

        if (len(player_list) == 9):
            observer_1_name = input("観戦者1の名前 : ")
        elif (len(player_list) == 10):
            observer_1_name = input("観戦者1の名前 : ")
            observer_2_name = input("観戦者2の名前 : ")

        # 観戦者
        is_exist_observer_1 = False
        is_exist_observer_2 = False
        if (observer_1_name != ""):
            for i in range(len(player_list)):
                if (player_list[i].get_name() == observer_1_name):
                    observer_1 = player_list.pop(i)
                    is_exist_observer_1 = True
                    break
            # error
            if (not is_exist_observer_1):
                print("該当する名前がありません。もう一度入力してください。")
                continue

        if (observer_2_name != ""):
            for i in range(len(player_list)):
                if (player_list[i].get_name() == observer_2_name):
                    observer_2 = player_list.pop(i)
                    is_exist_observer_2 = True
                    break
            # error
            if (not is_exist_observer_2):
                print("該当する名前がありません。もう一度入力してください。")
                continue

        # チーム決定
        # error
        if (len(player_list) != 8):
            print("人数が8人ではない({}人)のでチーム分けできませんでした。".format(len(player_list)))
            continue

        previous_rate_diff = 100
        for team in itertools.combinations(player_list, 4):
            team_X = []
            team_Y = []

            for player in team:
                team_X.append(player)

            for player in player_list:
                if (player.get_name() != team_X[0].get_name() and
                    player.get_name() != team_X[1].get_name() and
                    player.get_name() != team_X[2].get_name() and
                        player.get_name() != team_X[3].get_name()):
                    team_Y.append(player)

            team_X_rate = team_X[0].get_win_rate() + team_X[1].get_win_rate() + \
                team_X[2].get_win_rate() + team_X[3].get_win_rate()
            team_Y_rate = team_Y[0].get_win_rate() + team_Y[1].get_win_rate() + \
                team_Y[2].get_win_rate() + team_Y[3].get_win_rate()
            rate_diff = abs(team_X_rate - team_Y_rate)

            if (rate_diff < previous_rate_diff):
                team_A = team_X
                team_B = team_Y
                previous_rate_diff = rate_diff

        print("team A : ", team_A[0].get_name(),
              team_A[1].get_name(), team_A[2].get_name(), team_A[3].get_name())
        print("team B : ", team_B[0].get_name(),
              team_B[1].get_name(), team_B[2].get_name(), team_B[3].get_name())

        # 勝率計算
        win_team = get_win_team()

        if (win_team == "A" or win_team == "a"):
            for player in team_A:
                player.win_game()
            for player in team_B:
                player.lose_game()

        elif (win_team == "B" or win_team == "b"):
            for player in team_B:
                player.win_game()
            for player in team_A:
                player.lose_game()

        # 観戦者を戻す
        if (is_exist_observer_1):
            player_list.append(observer_1)
        if (is_exist_observer_2):
            player_list.append(observer_2)


