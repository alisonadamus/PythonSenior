class FileLineReader:
    def __init__(self, filename, encoding='utf-8'):
        self.filename = filename
        self.encoding = encoding
        self.file = open(self.filename, 'r', encoding=self.encoding)
        self.line_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        self.line_num += 1
        return self.line_num, line.strip()

    def reset(self):
        self.file.seek(0)
        self.line_num = 0

    def close(self):
        self.file.close()


reader = FileLineReader("my_file.txt")

print("=== Перші 20 рядків ===")
for i, (num, line) in enumerate(reader):
    print(f"[Перші 20] Рядок {num}: {line}")
    if i == 19:
        break

print("==========ТЕХНІЧНА ПЕРЕРВА==========")
print("Читаємо далі:")

for num, line in reader:
    print(f"[Далі] Рядок {num}: {line}")

reader.close()
