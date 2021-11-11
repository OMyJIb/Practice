n_of_tikets = int(input("Введите количество билетов цыфрами"))

age_list = [int(input("Введите возраст для каждого из участников конференции цыфрами")) for i in range(1, n_of_tikets+1)]

count_free = 0
count_junior = 0
count_adult = 0

for i in age_list:
    if 0 < i < 18:
        count_free += 1
    elif 18 <= i < 25:
        count_junior += 1
    elif 25 <= i:
        count_adult += 1
    else:
        print("Вы ввели возраст неверно")

Total = int(count_junior * 990 + count_adult * 1390)
if n_of_tikets < 3:
    print("Общая стоимость билетов составит:", Total, "руб.")
else:
    Total = int(Total * 90 // 100)
    print("Общая стоимость билетов составит c учетом скидки 10%:", Total, "руб.")

