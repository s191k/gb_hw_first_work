import json
import os
from os import path

from Note import Note

file_base = "base.json"
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_note_file():
    global all_data

    if os.stat(file_base).st_size != 0:
        with open(file_base, "r", encoding="utf-8") as file:
                loaded_notse = json.loads(file.read())
                all_data = []
                for x in loaded_notse:
                    all_data.append(Note(int(x['id']), x['head'], x['body'], x['createDate']))
                return all_data


def save_note_file():
    global all_data

    with open(file_base, "w", encoding="utf-8") as file:
        file.write(json.dumps(all_data, default=lambda x: x.__dict__))

def show_all():
    if all_data:
        for x in all_data:
            print(x)
    else:
        print("Заметок нет")

def add_new_note():
    global all_data

    head = input('Введите заголовок заметки:')
    body = input('Введите тело заметки:')
    if os.stat(file_base).st_size != 0:
        all_data.append(Note(all_data[-1].id +1, head,body,None))
    else:
        all_data.append(Note(None, head,body,None))
    save_note_file()

def change_note():
    if not _check_exists_of_data(): return
    show_all()
    answer = int(input("Введите номер записи, которую хотите изменить  : "))
    cur_data = all_data[answer-1]
    field_name = input("Введите название поля которое хотите обновить (Возможные варианты id | headNote) : ")
    new_value = input("Введите новое значение : ")

    match field_name:
        case "id":
            cur_data.id = int(new_value)
        case "head":
            cur_data.head = new_value
    save_note_file()

def delete_note():
    if not _check_exists_of_data(): return
    show_all()
    answer = int(input("Введите номер записи, которую хотите удалить : "))
    all_data.pop(answer-1)
    save_note_file()

def search_record():
    if not _check_exists_of_data(): return
    search_type, search_info = input("Введите номер заметки :: id <номер заметки> или head <заголовок заметки>  : ").split(" ")
    for x in all_data:
        if x.id == int(search_info) or x.head == search_info:
            print(x)
            break
    print("Такой записи не найдено")

def import_in_file(file_path):
    global last_id, all_data
    with open(file_path, encoding="utf-8") as f:
        all_data_new = [i.strip() for i in f]
        if all_data_new:
            for x in all_data_new:
                all_data.append(x)
            _rewrite_indexes()
            _write_data_in_file(all_data)

def _write_data_in_file(new_all_data):
    with open(file_base, "w", encoding="utf-8") as f:
        for x in new_all_data:
            f.write(f"{x}\n")

def _rewrite_indexes():
    global last_id,all_data
    index = 1
    new_all_data = []
    for x in all_data:
        cur_note = x.split(" ")
        cur_note[0] = str(index)
        index += 1
        new_all_data.append(" ".join(cur_note))
    all_data = new_all_data
    last_id = index

def _check_exists_of_data():
    read_note_file()
    if not all_data:
        print("нет записей")
        return False
    return True

def main_menu():
    play = True
    while play:
        read_note_file()
        answer = input("Заметки:\n"
                       "1. Показать все заметки\n"
                       "2. Добавить\n"
                       "3. Поиск\n"
                       "4. Изменение\n"
                       "5. Удаление\n"
                       # "6. Exp/Imp\n"
                       "7. Выход\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_note()
            case "3":
                search_record()
            case "4":
                change_note()
            case "5":
                delete_note()
            # case "6":
            #     import_in_file(input("Введите имя файла"))
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()