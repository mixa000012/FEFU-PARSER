import requests

your_id = input('Снилс ')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

params = {
    'mode': 'class',
    'c': 'dvfu:admission.spd',
    'action': 'getStudents',
}

data = {
    'admissionCampaignType': 'Прием на обучение на бакалавриат/специалитет',
    'financingSource': 'Бюджетная основа',
    'studyForm': 'Очная',
    'implementationPlace': 'Владивосток',
    'trainingDirection': '09.03.03 Прикладная информатика',
    'consent': 'false',
}
data2 = {
    'admissionCampaignType': 'Прием на обучение на бакалавриат/специалитет',
    'financingSource': 'Бюджетная основа',
    'studyForm': 'Очная',
    'implementationPlace': 'Владивосток',
    'trainingDirection': '09.03.04 Программная инженерия',
    'consent': 'false',
}
data3 = {
    'admissionCampaignType': 'Прием на обучение на бакалавриат/специалитет',
    'financingSource': 'Бюджетная основа',
    'studyForm': 'Очная',
    'implementationPlace': 'Владивосток',
    'trainingDirection': '01.03.02 Прикладная математика и информатика',
    'consent': 'false',
}


def print_order(i):
    global data
    response = requests.post('https://www.dvfu.ru/bitrix/services/main/ajax.php', params=params, headers=headers,
                             data=i).json()
    dir = ''
    if i == data:
        dat = 'data'
        dir = 'Прикладная информатика'
    elif i == data2:
        dat = 'data2'
        dir = 'Программная инженерия'
    elif i == data3:
        dat = 'data3'
        dir = 'Информационная безопасность'
    order = ''
    data = response.get('data')
    try:
        for id in data:
            if your_id == id['name']:
                order = int(float((id.get('GENERALORDER'))))
                break
        print(f'{dir}: {order:.0f}')
    except ValueError:
        print(f'Скорее всего вы не участвуете в {dir}' '\n'
              f'Для смены направлений нужно залезть в исходный код, поменять для {dat} параметр trainingDirection')


spisok = [data, data2, data3]

# if __name__ == 'main':
for i in spisok:
    print_order(i)

s = input()
