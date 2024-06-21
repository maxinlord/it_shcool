# Создайте словарь содержащий данные о человеке.
# В качестве строковых ключей используйте его имя, возраст, пол, рост, вес, размер ноги.
human = {
    "name": "John Doe",
    "age": 30,
    "sex": "male",
    "height": 175,
    "weight": 80,
    "foot_size": 42,
}

# Выведите на экран все данные о человеке по ключам.
print(
    human["name"],
    human["age"],
    human["sex"],
    human["height"],
    human["weight"],
    human["foot_size"],
)

# Добавьте в словарь ключ и значение размера ноги
human["foot_size"] = 43

# Удалите из словаря возраст
del human["age"]
