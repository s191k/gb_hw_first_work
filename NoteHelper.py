import json
import os
from os import path

from Note import Note

file_base = "base.json"
if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

class NoteHelper:

    def read_note_file(self):
        global all_data

        if os.stat(file_base).st_size != 0:
            with open(file_base, "r", encoding="utf-8") as file:
                loaded_notse = json.loads(file.read())
                all_data = []
                for x in loaded_notse:
                    all_data.append(Note(int(x['id']), x['head'], x['body'], x['createDate']))
                return all_data


    def save_note_file(self):
        global all_data

        with open(file_base, "w", encoding="utf-8") as file:
            file.write(json.dumps(all_data, default=lambda x: x.__dict__))

    def show_all(self):
        if all_data:
            for x in all_data:
                print(x)
        else:
            print("Заметок нет")

    def add_new_note(self):
        global all_data

        head = input('Введите заголовок заметки:')
        body = input('Введите тело заметки:')
        if os.stat(file_base).st_size != 0:
            all_data.append(Note(all_data[-1].id +1, head,body,None))
        else:
            all_data.append(Note(None, head,body,None))
        self.save_note_file()

    def change_note(self):
        if not self._check_exists_of_data(): return
        self.show_all()
        answer = int(input("Введите номер записи, которую хотите изменить  : "))
        cur_data = all_data[answer-1]
        field_name = input("Введите название поля которое хотите обновить (Возможные варианты id | head) : ")
        new_value = input("Введите новое значение : ")

        match field_name:
            case "id":
                cur_data.id = int(new_value)
            case "head":
                cur_data.head = new_value
        self.save_note_file()

    def delete_note(self):
        if not self._check_exists_of_data(): return
        self.show_all()
        answer = int(input("Введите номер записи, которую хотите удалить : "))
        all_data.pop(answer-1)
        self.save_note_file()

    def search_record(self):
        if not self._check_exists_of_data(): return
        search_type, search_info = input("Введите номер заметки :: id <номер заметки> или head <заголовок заметки>  : ").split(" ")
        for x in all_data:
            if x.id == int(search_info) or x.head == search_info:
                print(x)
                break
        print("Такой записи не найдено")

    def _check_exists_of_data(self):
        self.read_note_file()
        if not all_data:
            print("нет записей")
            return False
        return True