# дни недели пронумерованы следующим образом: 1-понедельник.., 
# 6 -суббота, 7- воскресенье. Дано целое число K, лежащее в диапазоне 1-365,
# и целое число N, лежащее в диапазоне 1-7. Определить 
# номер дня недели для K-го дня года, если известно, что в этом году 1 января было днем недели с номером N


weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
K = int(input("Введите номер дня года (1-365): "))
N = int(input("Введите номер дня недели (1-7): "))
result = weekdays[(K + N - 2) % 7]
print("Номер дня недели: ", result)
