"""Game guess the number"""

import numpy as np
number = np.random.randint(1, 101)

count = 0 

while True:
    count+=1
    predict_number = int(input("угадай число от 1 до 100: "))
    
    if predict_number > number:
        print("меньше")
    elif predict_number < number:
        print("больше")
    else:
        print(f"вы угадали за {count} попыток")
        break
    