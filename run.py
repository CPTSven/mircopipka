import time
import random

a = ['думаю, ДА', "думаю, НЕТ"]
print('У вас есть кириешки?')
for i in range(3):
    time.sleep(1)
    print(i+1, 'sek')
print(random.choice(a))
#print('Прости, я не могу предоставить тебе сметану')
