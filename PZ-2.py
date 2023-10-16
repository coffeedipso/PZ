def get_weekday(K, N):
    weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    return weekdays[(K + N - 2) % 7]

K = int(input("Введите номер дня года (1-365): "))
N = int(input("Введите номер дня недели (1-7): "))

weekday = get_weekday(K, N)
print("Номер дня недели: ", weekday)