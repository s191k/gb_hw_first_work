from NoteHelper import NoteHelper

def main_menu():
    play = True
    note_helper = NoteHelper()
    while play:
        note_helper.read_note_file()
        answer = input("Заметки:\n"
                       "1. Показать все заметки\n"
                       "2. Добавить\n"
                       "3. Поиск\n"
                       "4. Изменение\n"
                       "5. Удаление\n"
                       "6. Выход\n")
        match answer:
            case "1":
                note_helper.show_all()
            case "2":
                note_helper.add_new_note()
            case "3":
                note_helper.search_record()
            case "4":
                note_helper.change_note()
            case "5":
                note_helper.delete_note()
            case "6":
                play = False
            case _:
                print("Try again!\n")


main_menu()