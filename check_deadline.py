from datetime import date
current_date = date.today()
print(current_date)
dedline = input("Введите дату дедлайна (в формате год-месяц-день,например 2025-01-26): ")
if current_date == dedline:
    print("Дедлайн сегодня!")
elif current_date > dedline:
    print("Дедлайн истек ", current_date-dedline,"дня(дней) назад")
elif current_date < dedline:
 print("Дедлайн через", dedline - current_date)