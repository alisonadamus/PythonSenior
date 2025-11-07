my_list = [10, 20, 30]
# my_list = "Homework"

it = iter(my_list)

print(next(it))
print("some code")
print(next(it))
print("tu-tu-tu-tu")
print(next(it))
try:
    print(next(it))
except StopIteration as e:
    print("end of iteration", e)


with open("my_file.txt", 'r', encoding='utf-8') as f:
    line_num = 0
    for i in range(20):
        line_num = i + 1
        line = f.readline()
        print(f"[Перші 20] Рядок {line_num}: {line.strip()}")

    print("==========ТЕХНІЧНА ПЕРЕРВА==========")
    print("Читаємо далі:")
    line_num = 20

    for line in f:
        line_num += 1
        print(f"[Далі] Рядок {line_num}: {line.strip()}")
