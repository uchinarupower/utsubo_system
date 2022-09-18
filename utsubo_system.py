import copy
import itertools


class Player:
    def __init__(self, name):
        self.win_num = 0
        self.game_num = 0
        self.win_rate = 0
        self.name = name

    def win_game(self):
        self.win_num += 1
        self.game_num += 1
        if (self.win_num != 0):
            self.win_rate = self.game_num / self.win_num

    def lose_game(self):
        self.game_num += 1
        if (self.win_num != 0):
            self.win_rate = self.game_num / self.win_num

    def get_win_rate(self):
        return self.win_rate


def main():
    all_player_list = []
    Player_1 = Player("utsubo")
    all_player_list.append(Player_1)
    Player_2 = Player("haruto")
    all_player_list.append(Player_2)
    Player_3 = Player("hiyokome")
    all_player_list.append(Player_3)
    Player_4 = Player("musyamusya")
    all_player_list.append(Player_4)
    Player_5 = Player("kusomegane")
    all_player_list.append(Player_5)
    Player_6 = Player("mizu")
    all_player_list.append(Player_6)
    Player_7 = Player("kene")
    all_player_list.append(Player_7)
    Player_8 = Player("nusupi")
    all_player_list.append(Player_8)
    Player_9 = Player()
    Player_9.name = "sena"
    player_list.append(Player_9)
    Player_10 = Player()
    Player_10.name = ""
    player_list.append(Player_10)

    while (True):

        observer_1_name = input("観戦者1の名前 : ")
        observer_2_name = input("観戦者2の名前 : ")

        player_list = all_player_list

        # 観戦者
        is_exist_observer_1 = False
        is_exist_observer_2 = False
        if (observer_1_name != ""):
            for i in range(len(player_list)):
                if (player_list[i].name == observer_1_name):
                    observer_1 = player_list.pop(i)
                    is_exist_observer_1 = True
                    break

        if (observer_2_name != ""):
            for i in range(len(player_list)):
                if (player_list[i].name == observer_2_name):
                    observer_2 = player_list.pop(i)
                    is_exist_observer_2 = True
                    break

        # チーム決定
        previous_rate_diff = 100
        for team in itertools.combinations(player_list, 4):
            team_X = []
            team_Y = []
            # print("team A : ", team_X[0].name,
            #      team_X[1].name, team_X[2].name, team_X[3].name)
            for player in team:
                team_X.append(player)

            for player in player_list:
                if (player.name != team_X[0].name and
                    player.name != team_X[1].name and
                    player.name != team_X[2].name and
                        player.name != team_X[3].name):
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

        print("team A : ", team_A[0].name,
              team_A[1].name, team_A[2].name, team_A[3].name)
        print("team B : ", team_B[0].name,
              team_B[1].name, team_B[2].name, team_B[3].name)

        # 勝率計算
        win_team = input("勝ったチーム : ")

        if (win_team == "A"):
            for player in team_A:
                player.win_game()
            for player in team_B:
                player.lose_game()

        elif (win_team == "B"):
            for player in team_B:
                player.win_game()
            for player in team_A:
                player.lose_game()

        # 観戦者を戻す
        if (is_exist_observer_1):
            player_list.append(observer_1)
        if (is_exist_observer_2):
            player_list.append(observer_2)


main()
