name_ = input('Введите имя: ')
surname_ = input('Введите фамилию: ')
year_ = input('Введите год вашего рождения: ')
town_ = input('Введите название города, в котором вы проживаете: ')
email_ = input('Введите ваш email: ')
phone_ = input('Введите ваш номер телефона: ')

def dosie(**kwargs):
    result = f'Имя – {kwargs["name"]}\nФамилия – {kwargs.get("surname")}\nГод рождения – {kwargs.get("year")}\n' \
             f'Город – {kwargs.get("town")}\nEmail – {kwargs.get("email")}\nТелефон – {kwargs.get("phone")}\n'
    return result


print(dosie(
    name=name_,
    surname=surname_,
    year=year_,
    town=town_,
    email=email_,
    phone=phone_
))