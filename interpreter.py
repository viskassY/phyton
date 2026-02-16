def text():
    word = "Python"
    print(f"Слово: {word}\n")

    codes = [ord(char) for char in word]
    print(f"Числове представлення: {codes}")

    binary = [bin(code)[2:].zfill(8) for code in codes]
    print(f"Двійковий код: {binary}")

    decoded = "".join([chr(code) for code in codes])
    print(f"\n Зворотне перетворення: {decoded}")

text()