ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789"
N = len(ALPHABET)

def get_char_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

def encrypt(text, base):
    res = ""
    for i in range(len(text)):
        old_idx = ALPHABET.find(text[i])
        current_shift = (base + i) % N
        new_idx = (old_idx + current_shift) % N
        res += ALPHABET[new_idx]
    return res

def decrypt(text, base):
    res = ""
    for i in range(len(text)):
        old_idx = ALPHABET.find(text[i])
        current_shift = (base + i) % N
        new_idx = (old_idx - current_shift) % N
        res += ALPHABET[new_idx]
    return res

def solve_task(encrypted_text, key_strings):
    for base in range(N):
        attempt = decrypt(encrypted_text, base)

        for key in key_strings:
            key_freq = get_char_frequency(key)
            k_len = len(key)

            for start in range(len(attempt) - k_len + 1):
                substring = attempt[start:start + k_len]
                if get_char_frequency(substring) == key_freq:
                    print(f"\nЗнайдено base: {base}")
                    print(f"Розшифрований текст: {attempt}")
                    print(f"Індекс ключа '{key}': {start}")
                    return

    print("Ключ не знайдено")


print("1 - Зашифрувати")
print("2 - Розшифрувати (підібрати base)")
choice = input("Оберіть режим: ")

if choice == "1":
    text = input("Введіть відкритий текст: ")
    base = int(input("Введіть base: "))
    encrypted = encrypt(text, base)
    print("Зашифрований текст:", encrypted)

elif choice == "2":
    encrypted = input("Введіть зашифрований текст: ")
    keys_input = input("Введіть ключі через пробіл: ")
    keys = keys_input.split()
    solve_task(encrypted, keys)

else:
    print("Невірний вибір")