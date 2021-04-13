
class File:
    def __init__(self):
        self.data_filename = 'data.txt'
        self.ladder_filename = 'ladder.txt'

    def log_data_file(self,data_to_write:str)->None:
        open(file=data_filename,mode='a',encoding='utf-8').write(f'{data_to_write}\n')

    def read_data_file(self)->list:
        return open(file=data_filename,mode='r',encoding='utf-8').readlines()

    def get_ladder_player_list(self)->list:
        return open(file=ladder_filename,mode='r',encoding='utf-8').readlines()

    def add_player(self,player_name:str,_date:str)->None:
        open(file=ladder_filename,mode='a',encoding='utf-8').write(f'{player_name}\n')
        open(file=data_filename,mode='a',encoding='utf-8').write(f'+NEW/{player_name}/{_date}/\n')

    def remove_player(self,player_name:str,_date:str)->None:
        open(file=data_filename,mode='a',encoding='utf-8').write(f'-EX/{player_name}/{_date}/\n')


if __name__ == "__main__":
    pass