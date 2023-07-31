from environs import Env

env = Env()
env.read_env()

club_id = env.int('CLUB_ID')  # ID группы

sleep_time = env.int('SLEEP_TIME')  # Интервал провки наличия заявок в секундах

vkapp_id = env('VKAPP_ID')  # Приложение для авторизации (не менять)

link_to_token = env('LINK_TO_TOKEN')

token = env('TOKEN')
