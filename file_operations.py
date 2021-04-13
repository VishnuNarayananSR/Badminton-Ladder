data_filename = 'data.txt'
ladder_filename = 'ladder.txt'

def log_data_file(data_to_write):
    open(file=data_filename,mode='a',encoding='utf-8').write(f'{data_to_write}\n')

def read_data_file():
    return open(file=data_filename,mode='r',encoding='utf-8').readlines()

def get_ladder_player_list():
    return open(file=ladder_filename,mode='r',encoding='utf-8').readlines()

def add_player(player_name,_date=None):
    open(file=ladder_filename,mode='a',encoding='utf-8').write(f'{player_name}\n')
    open(file=data_filename,mode='a',encoding='utf-8').write(f'+NEW/{player_name}/{_date}/\n')


def remove_player(player_name):
    player_list = open(file=ladder_filename,mode='r',encoding='utf-8').readlines()
    player_list.remove(player_name)
    with open(file=data_filename,mode='w',encoding='utf-8') as file:
        for player in player_list:
            file.writ(f"{player}\n")