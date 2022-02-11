import time
import random
from tqdm import tqdm

a = ['думаю, ДА', "думаю, НЕТ"]
print('У вас есть кириешки?')
for i in range(3):
    time.sleep(1)
    print(i+1, 'sek')
kirieshka = random.choice(a)
print(kirieshka)
#print('Прости, я не могу предоставить тебе сметану')

if kirieshka == "думаю, ДА":
    time.sleep(2)
    print('Дайте две пачки')
    time.sleep(3)
    print('С вас 35 рупис')
    print('Начинаю процесс сметанизации кириешек')
    for i in tqdm(range(int(9e6))):
        pass
    print('Процесс окончен')
else:
    time.sleep(2)
    print('Жалко')
