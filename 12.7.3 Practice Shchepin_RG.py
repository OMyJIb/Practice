per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print("Процентные ставки по депозитам в банках следующие:", per_cent)

a = int(input("Money"))

tkb = (a/100)*per_cent.get('ТКБ')
skb = (a/100)*per_cent.get('СКБ')
vtb = (a/100)*per_cent.get('ВТБ')
sber = (a/100)*per_cent.get('СБЕР')


list_per_cent = []
list_per_cent.append(tkb)
list_per_cent.append(skb)
list_per_cent.append(vtb)
list_per_cent.append(sber)

print("One-year deposit for every single bank", list_per_cent)
print("Максимальная сумма, которую вы можете заработать", max(list_per_cent))
