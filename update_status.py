status = input("Введите статус(выполнено, в процессе, отложено) ")
print("Статус:", status)
status1 = "выполнено"
status2= "в процессе"
status3 = "отложено"
status_update = int(input("""Выберите новый статус заметки:
1. выполнено
2. в процессе
3. отложено
 """))
if status_update == 1:
    print("Статус заметки успешно обновлён на:", status1)
elif status_update == 2:
    print("Статус заметки успешно обновлён на:", status2)
elif status_update == 3:
    print("Статус заметки успешно обновлён на:", status3)
else: print("Значение неверно")