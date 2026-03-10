def binary_search_phonebook(phonebook, target):
    low = 0
    high = len(phonebook) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = phonebook[mid]

        if guess == target:
            return mid 
        if guess > target:
            high = mid - 1 
        else:
            low = mid + 1 

    return -1 

book = ["Moon", "Moore", "Morse", "Mose", "Moss"]

name_to_find = "Moore"
index = binary_search_phonebook(book, name_to_find)

if index != -1:
    print(f"Запис '{name_to_find}' знайдено за індексом {index}")
else:
    print("Запис не знайдено")