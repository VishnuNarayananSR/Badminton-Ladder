
class File:
    def __init__(self):
        self.data_filename = 'data.txt'
        self.ladder_filename = 'ladder.txt'

    def __remove_next_line(self, data_list) -> list:
        return [item.replace("\n", '') for item in data_list]

    def write_challenge_data(self, name1: str, pos1: str, name2: str, pos2: str, date: str, score: str = None) -> None:
        open(file=self.data_filename, mode='a',
             encoding='utf-8').write(f'{name1} {pos1}/{name2} {pos2}/{date}/{score}\n')

    def read_data_file(self) -> list:
        return self.__remove_next_line(self.__remove_next_line(open(file=self.data_filename, mode='r', encoding='utf-8').readlines()))

    def get_ladder_player_list(self) -> list:
        return self.__remove_next_line(open(file=self.ladder_filename, mode='r', encoding='utf-8').readlines())

    def get_yet_to_finish_challenges(self) -> list:
        datas = self.read_data_file()
        challenges = []
        for item in datas:
            temp = item.split("/")
            if len(temp) == 4 and temp[-1].__contains__('None'):
                challenges.append(item)
        return challenges

    def get_latest_n_challenges(self, cnt:int) -> list:
        datas = reversed(self.read_data_file())
        challenges = [item for item in datas if len(item.split("/")) == 4]
        challenge_cnt = len(challenges)
        if cnt > challenge_cnt:
            cnt = challenge_cnt
        return challenges[:cnt]
    
    def update_score(self,challenge_data:str,score:str)->None:
        '''
        arguments sample:
        challenge_data:str  =   name 1 1/name 2 2/2020-12-12/None
        score:str           =   12-24 15-18 
        '''
        datas = self.read_data_file()
        for ind,item in enumerate(datas):
            if item.__contains__(challenge_data):
                datas[ind] = item.replace('None',score)
                break
        with open(file=self.data_filename,mode='w',encoding='utf-8') as file:
            for item in datas:
                file.write(f"{item}\n")

    def rewrite_ladder_order(self, player_list:list) -> None:
        with open(file=self.ladder_filename, mode='w', encoding='utf-8') as file:
            for player in player_list:
                file.write(f'{player}\n')

    def add_player_file(self, player_name: str, _date: str) -> None:
        open(file=self.ladder_filename, mode='a',
             encoding='utf-8').write(f'{player_name}\n')
        open(file=self.data_filename, mode='a',
             encoding='utf-8').write(f'+NEW/{player_name}/{_date}\n')

    def remove_player(self, player_name: str, _date: str) -> None:
        open(file=self.data_filename, mode='a',
             encoding='utf-8').write(f'-EX/{player_name}/{_date}\n')


if __name__ == "__main__":
    pass