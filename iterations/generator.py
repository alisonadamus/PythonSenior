import random
import time

def sensor_data():
    while True:
        yield random.uniform(20.0, 25.0)
        time.sleep(1)

for temp in sensor_data():
    print(f"Temperature: {temp:.2f}°C")
    if temp > 24.5:
        print("Too hot! Stop reading.")
        break



def squares(n):
    for i in range(1, n + 1):
        yield i * i

print(list(squares(49)))



gen = (x * 10 for x in range(5))
print(next(gen))
print(next(gen))
print(list(gen))

