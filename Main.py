from GetData.sum_data import sum_data
from GetData.SaveResult import save_result
from HelpPrice.learning_price import learning_price


cars = sum_data()

save_result(cars)

data = []

for i in range(3):
    k = input()
    data.append(k)

answer = learning_price(data)

print(answer)