import threading

def create_file(index):
    filename = f"file_{index}.txt"
    with open(filename, 'w') as f:
        f.write(f"File number: {index}")

def create_files_concurrently():
    threads = []

    for i in range(1, 11):  # Создаем 10 файлов
        thread = threading.Thread(target=create_file, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Ожидаем завершения всех потоков

if __name__ == "__main__":
    create_files_concurrently()
    print("Файлы созданы успешно.")
