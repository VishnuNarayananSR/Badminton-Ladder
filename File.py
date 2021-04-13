
class File:
    def __init__(self):
        self.data_filename = 'data.txt'
        self.ladder_filename = 'ladder.txt'

    def write_challege_data(self,name1:str,pos1:str,name2:str,pos2:str,_date:str)->None:
        open(file=self.data_filename,mode='a',encoding='utf-8').write(f'{name1}/{pos1}/{name2}/{pos2}/{date}\n')

    def read_data_file(self)->list:
        return open(file=self.data_filename,mode='r',encoding='utf-8').readlines()

    def get_ladder_player_list(self)->list:
        return open(file=self.ladder_filename,mode='r',encoding='utf-8').readlines()
    
    def rewrite_ladder_order(player_list):
        with open(file=self.ladder_filename,mode='w',encoding='utf-8') as file:
            for player in player_list:
                file.write(f'{player}\n')

    def add_player_file(self,player_name:str,_date:str)->None:
        open(file=self.ladder_filename,mode='a',encoding='utf-8').write(f'{player_name}\n')
        open(file=self.data_filename,mode='a',encoding='utf-8').write(f'+NEW/{player_name}/{_date}\n')

    def remove_player(self,player_name:str,_date:str)->None:
        open(file=self.data_filename,mode='a',encoding='utf-8').write(f'-EX/{player_name}/{_date}\n')


if __name__ == "__main__":
    pass