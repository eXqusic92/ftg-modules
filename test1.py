import requests
from time import sleep
from colorama import init, Fore

init(autoreset=True)

api_key = 'B30BeBB15955fB24463B8c904f72c5cd'


def get_balance():  # Получение баланса
    balance = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key={}&action=getBalance'.format(api_key))
    return str(balance.text.split(':')[1].split("'")).strip("[']")


def get_numbers_status():  # Получение свободных номеров
    nums = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key={}&action=getNumbersStatus&country=1'.format(api_key)).json()
    return str(nums['tg_0'])


def get_number():  # Покупка номера ACCESS_NUMBER:394315244:380916127183
    num = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key={}&action=getNumber&service=tg&country=1'.format(api_key)).text.split(":")
    if num[0] == "ACCESS_NUMBER":
        return [str(num[1]), str(num[2])]
    elif num[0] == "NO_NUMBERS":
        return num[0]
    elif num[0] == "NO_BALANCE":
        return num[0]
    else:
        print("Ошибка", num[0])
        exit()


def set_status(status_id):
    status_id = str(status_id)
    status = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key={}&action=setStatus&status=1&id={}'.format(api_key, status_id)).text
    if status == "ACCESS_READY":
        return status
    else:
        return


def get_status(status_id):  # STATUS_OK:59170
    status_id = str(status_id)
    status = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key={}&action=getStatus&id=${}'.format(api_key, status_id)).text
    status = status.split(":")
    if status[0] == "STATUS_OK":
        return status[1]
    elif status[0] == "STATUS_WAIT_CODE":
        return status[0]


def set_status_done(status_id):
    status_id = str(status_id)
    done = requests.get('https://sms-activate.ru/stubs/handler_api.php?api_key={}&action=setStatus&status=6&id={}'.format(api_key, status_id)).text
    return done


print(Fore.BLUE + "Ждем номер...")
while True:
    response = get_number()
    if response == "NO_NUMBERS":
        sleep(3)
        pass
    elif response == "NO_BALANCE":
        print(Fore.RED + "Недостаточно средств")
        exit()
    else:
        operation_id = response[0]
        number = response[1]
        print("Номер получен. ID операции: " + Fore.GREEN + f"{operation_id}." + Fore.RESET + " Номер телефона: " + Fore.GREEN + f"{number}")
        break
input("Подтвердите отправку смс (нажмите Enter)")
print("Ждем код...")
set_status(operation_id)

while True:
    if get_status(operation_id) == "STATUS_WAIT_CODE":
        sleep(3)
        pass
    else:
        code = get_status(operation_id)
        print(f"Код получен - " + Fore.GREEN + f"{code}")
        answer = input("Код верный? да/нет - ")
        if answer == "да":
            set_status_done(operation_id)
        exit()
