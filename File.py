from datetime import date,datetime


date_format = "%d-%m-%Y"

class File:
    def __init__(self):
        self.data_filename = 'data.txt'
        self.ladder_filename = 'ladder.txt'

    def __remove_next_line(self, data_list) -> list:
        return [item.replace("\n", '') for item in data_list]

    def write_challenge_data(self, name1: str, pos1: str, name2: str, pos2: str, _date: str, score: str = None) -> None:
        open(file=self.data_filename, mode='a',
             encoding='utf-8').write(f'{name1} {pos1}/{name2} {pos2}/{_date}/{score}\n')

    def read_data_file(self) -> list:
        return self.__remove_next_line(self.__remove_next_line(open(file=self.data_filename, mode='r', encoding='utf-8').readlines()))

    def get_ladder_player_list(self) -> list:
        return self.__remove_next_line(open(file=self.ladder_filename, mode='r', encoding='utf-8').readlines())

    def get_yet_to_finish_challenges(self,_date:date) -> list:
        datas = self.read_data_file()
        _date = datetime.strptime(_date, date_format)
        challenges = []
        for item in datas:
            temp = item.split("/")
            event_date = datetime.strptime(temp[2], date_format)
            if event_date >= _date:
                if len(temp) == 4 and temp[-1].__contains__('None'):
                    challenges.append(item)
        return challenges

    def get_latest_n_challenges(self, cnt: int) -> list:
        datas = reversed(self.read_data_file())
        challenges = [item for item in datas if len(item.split("/")) == 4]
        challenge_cnt = len(challenges)
        if cnt > challenge_cnt:
            cnt = challenge_cnt
        return challenges[:cnt]

    def reorder_ladder_by_match(self, challenge_data: str, player_list: list) -> list:
        '''
        arguments sample:
        challenge_data:str  =   qwer 2/abcd 1/12-12-2021/14-10 18-15
        player_list:list    =   list of players

        return sample
        player_list with order modified
        '''
        temp = challenge_data.split("/")
        player1 = (temp[0].split()[0], int(temp[0].split()[1]))
        player2 = (temp[1].split()[0], int(temp[1].split()[1]))
        score = temp[3]
        if score != 'None':
            scores = [list(map(int, item.split("-"))) for item in score.split()]
            player1_set = 0
            player2_set = 0
            for a, b in scores:
                if a > b:
                    player1_set += 1
                else:
                    player2_set += 1
            if player1_set > player2_set:
                player_list.pop(player1[1]-1)
                player_list.insert(player1[1]-1, player2[0])
                player_list.pop(player2[1]-1)
                player_list.insert(player2[1]-1, player1[0])
        else:
                player_list.pop(player1[1]-1)
                player_list.insert(player1[1]-1, player2[0])
                player_list.pop(player2[1]-1)
                player_list.insert(player2[1]-1, player1[0])

        return player_list

    def __match_finished_ladder_update(self, challenge_data: str) -> None:
        player_list = self.getlad
        updated_player_list = self.reorder_ladder_by_match(
            challenge_data,  player_list)
        self.rewrite_ladder_order(updated_player_list)

    def update_score(self, challenge_data: str, score: str) -> None:
        '''
        arguments sample:
        challenge_data:str  =   name 1 1/name 2 2/2020-12-12/None
        score:str           =   12-24 15-18 
        '''
        datas = self.read_data_file()
        for ind, item in enumerate(datas):
            if item.__contains__(challenge_data):
                datas[ind] = item.replace('None', score)
                break
        with open(file=self.data_filename, mode='w', encoding='utf-8') as file:
            for item in datas:
                file.write(f"{item}\n")
        self.__match_finished_ladder_update(datas[ind])

    def rewrite_ladder_order(self, player_list: list) -> None:
        with open(file=self.ladder_filename, mode='w', encoding='utf-8') as file:
            for player in player_list:
                file.write(f'{player}\n')

    def add_player_file(self, player_name: str, _date: str) -> None:
        open(file=self.ladder_filename, mode='a',
             encoding='utf-8').write(f'{player_name}\n')
        open(file=self.data_filename, mode='a',
             encoding='utf-8').write(f'+NEW/{player_name}/{_date}\n')

    def remove_player(self, player_name: str, _date: str) -> bool:
        for item in self.read_data_file():
            if item.__contains__(f'-EX/{player_name}/'):
                return False
        open(file=self.data_filename, mode='a',
             encoding='utf-8').write(f'-EX/{player_name}/{_date}\n')
        return True


    def player_already_present(self, player_name: str) -> bool():
        player_list = self.get_ladder_player_list()
        if player_name in player_list:
            return True
        return False


    def last_active_date_of_player(self,player_name: str) -> date:
        datas = self.read_data_file()
        flag = True
        latest = None
        for item in datas:
            temp = item.split("/")
            if flag and len(temp) == 3:
                if temp[1] == player_name:
                    latest = datetime.strptime(temp[2], date_format)
                    # latest = latest.date().strftime(date_format)
                    flag = False
            elif len(temp) == 4:
                _player_1 = " ".join(temp[0].split()[:-1])
                _player_2 = " ".join(temp[1].split()[:-1])
                if player_name in [_player_1,_player_2]:
                    date_temp = datetime.strptime(temp[2], date_format)
                    # date_temp = date_temp.date().strftime(date_format)
                    if date_temp > latest:
                        latest = date_temp
        return latest.date().strftime(date_format)
        
    def get_challenges_by_player_name(self, name1: str) -> list:
        datas = self.read_data_file()
        ret_data = []
        for item in datas:
            temp = item.split("/")
            if len(temp) != 4:
                continue
            if item.__contains__(name1): 
                ret_data.append(item)
        return ret_data

    def get_challenges_by_date(self, date: str) -> list:
        datas = self.read_data_file()
        ret_data = []
        for item in datas:
            temp = item.split("/")
            if len(temp) != 4:
                continue
            if item.__contains__(date):
                ret_data.append(item)
        return ret_data

    def get_most_active_player(self) -> str:
        player_list = self.get_ladder_player_list()
        datas = self.read_data_file()
        match_data = {}
        for player in player_list:
            for item in datas:
                temp = item.split("/")
                if len(temp) != 4:
                    continue
                player_1_name = " ".join(temp[0].split()[:-1])
                player_2_name = " ".join(temp[1].split()[:-1])
                if player in [player_1_name, player_2_name]:
                    if player in match_data.keys():
                        match_data[player] += 1
                    else:
                        match_data[player] = 1
            else:
                if player not in match_data.keys():
                    match_data[player] = 0
        high_cnt = max(match_data.values())
        for key, value in match_data.items():
            if value == high_cnt:
                return key

    def get_least_active_player(self) -> str:
        player_list = self.get_ladder_player_list()
        datas = self.read_data_file()
        match_data = {}
        for player in player_list:
            for item in datas:
                temp = item.split("/")
                if len(temp) != 4:
                    continue
                player_1_name = " ".join(temp[0].split()[:-1])
                player_2_name = " ".join(temp[1].split()[:-1])
                if player in [player_1_name, player_2_name]:
                    if player in match_data.keys():
                        match_data[player] += 1
                    else:
                        match_data[player] = 1
                    break
            else:
                match_data[player] = 0
        high_cnt = min(match_data.values())
        for key, value in match_data.items():
            if value == high_cnt:
                return key

    def latest_date_in_the_data_file(self,)->date:
        datas = self.read_data_file()
        item = datas[-1]
        temp = item.split("/")
        return datetime.strptime(temp[2], date_format).date().strftime(date_format)
    
    def matches_between_two_dates(self,date_1:str,date_2:str)->list:
        datas = self.read_data_file()
        date_1 = datetime.strptime(date_1, date_format)
        date_2 = datetime.strptime(date_2, date_format)
        ret_data = []
        for item in datas:
            temp = item.split("/")
            if len(temp) == 4:
                match_date = datetime.strptime(temp[2], date_format)
                if date_1 <= match_date <= date_2:
                    ret_data.append(item)
        return ret_data
    
    def order_of_ladder_in_date(self,_date:str)->list:
        datas = self.read_data_file()
        player_list = []
        _date = datetime.strptime(_date, date_format)
        for item in datas:
            temp = item.split("/")
            event_date = datetime.strptime(temp[2], date_format)
            if event_date <= _date:
                if len(temp) == 3:
                    if temp[0] == '+NEW':
                        player_list.append(temp[1])
                    elif temp[0] == '-EX':
                        player_list.remove(temp[1])
                elif len(temp) == 4:
                    # player_list.append(temp[1])
                    player_list = self.reorder_ladder_by_match(item,player_list)
        return player_list
    
    def update_ladder_file(self,)->None:
        latest_date = self.latest_date_in_the_data_file()
        player_list = self.order_of_ladder_in_date(latest_date)
        self.rewrite_ladder_order(player_list)


if __name__ == "__main__":
    pass