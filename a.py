import  datetime
from datetime import timedelta
import json
from re import sub

def get_age (birthdate):
    timedelta(days=5511).days / 365

    now = datetime.date.today()
    date = now - birthdate
    age=date.days/365

    return round(age,1)

def how_long_working(seniority):
    timedelta(days=5511).days / 365

    now = datetime.date.today()
    date = now - seniority
    years = date.days / 365
    return round(years, 1)


def add_employee(employee):
    try:
        print ('Dodaj pracownika z działu sprzedaż')
        name=input('Imię').capitalize()
        last_name=input('Nazwisko').capitalize()
        birthday = input('Podaj datę urodzenia pracownika. '
                         'Pamiętaj o wpisaniu "/" po roku i dniu urodzin (DD/MM/YYYY)')
        birthdate = datetime.datetime.strptime(birthday, "%d/%m/%Y").date()
        age=get_age(birthdate)
        if age>65:
            print ('Błędnie wprowadzona data. Wiek pracownika nie może przekroczyć 65 lat!')
        elif age<18:
            print('Błędnie wprowadzona data. Pracownik musi ukończyć 18 lat')
        else:
            start_date= input(('Podaj datę zatrudnienia pracownika. '
                             'Pamiętaj o wpisaniu "/" po roku i dniu zatrudnienia (DD/MM/YYYY)'))
            seniority=datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            how_long=how_long_working(seniority)
            if how_long >25:
                print('Sprawdź datę zatrudnienia. Pracownik nie może pracować dłużej niż 25 lat')
            else:
                paycheck = float(input('Zakontraktowana kwota wynagrodzenia w PLN'))
                if paycheck>10000:
                    print ('Zadeklarowana kwota wynagrodzenia nie może być wyższa od 10000PLN')
                elif paycheck<3100:
                    print('Zadeklarowana kwota wynagrodzenia nie może być niższa niż 3100zł')
                else:
                    id=int(input('Id pracownika'))
                    extra_information=input('Dodatkowe informacje')
                    employee[id] = {'name':name,'last_name':last_name, 'age':age, 'how_long':how_long, 'paycheck':paycheck,
                            'extra_information':extra_information}
    except ValueError: print ('Wprowadzono błędnie dane. Sprawdź poprawność dat.')


def choice():
    try:
        print('Co chcesz zrobic?')
        print('1 Dodać pracownika')
        print('2 Usunąć pracownika')
        print ('3 Zobaczyć wszystkich pracowników')
        print('0 Wyjście')
        choose = int(input())
        return choose
    except: print ('Wprowadzono zły znak!')



def add(document):
    employee={}
    file = open(document, 'a+')
    add_employee(employee)
    file.write(json.dumps(employee) + '\n')
    file.close()
    employee.clear()

def delete (document):
    file = open(document, 'r+')
    for line in file.readlines():
        print(line)
    file.close()
    with open(document, 'r') as fr:
        lines = fr.readlines()
        ptr = 1
        position = int(input(
            'Wpisz pozycję/wiersz,w którym znajdują się dane do usunięcia'))  # usuwa wskazaną pozycję (wskazany wiersz)
        with open(document, 'w') as fw:
            for line in lines:
                if ptr != position:
                    fw.write(line)
                ptr += 1
    file.close()
    print('usunięto')

def all_workers(document):
    file = open(document, 'r+')
    for line in file.readlines():
        print(line)
    file.close()


def sales():
    document = 'sales_worker.txt'
    while True:
        choose=choice()
        if choose==1:
            add(document)
        elif choose==2:
            delete(document)
        elif choose==3:
            all_workers(document)
        elif choose==0:
            break

def hr():
    document = 'hr_worker.txt'
    while True:
        choose = choice()
        if choose == 1:
            add(document)
        elif choose == 2:
            delete(document)
        elif choose == 3:
            all_workers(document)
        elif choose == 0:
            break

def production():
    document = 'production_worker.txt'
    while True:
        choose = choice()
        if choose == 1:
            add(document)
        elif choose == 2:
            delete(document)
        elif choose == 3:
            all_workers(document)
        elif choose == 0:
            break

def menu():
    try:
        while True:
            print('Witaj w programie do zarzadzania pracownikami?')
            print('W jakim dziale chcesz dokonać zmian?')
            print('1------Sprzedaż')
            print ('2-----HR i płace')
            print ('3-----Produkcja')
            print('0 ---- Wyjście')
            choose= int(input())
            if choose==1:
                sales()
            elif choose ==2:
                hr()
            elif choose==3:
                production()
            elif choose==0:
                break
            else:
                print ('Zły znak, wpisz numer z manu')
    except:print ('Błąd, sprawdź czy wybrałeś dobry znak')


menu() # wywołanie programu