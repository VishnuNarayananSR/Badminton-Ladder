data_filename = 'data.txt'
ladder_filename = 'ladder.txt'

def log_data_file(data_to_write):
    open(file=data_filename,mode='a',encoding='utf-8').write(f'{data_to_write}\n')

def read_data_file():
    return open(file=data_filename,mode='r',encoding='utf-8').readlines()

def get_ladder_player_list():
    return open(file=ladder_filename,mode='r',encoding='utf-8').readlines()

