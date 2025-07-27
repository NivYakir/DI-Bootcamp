choice = input("Type 'e' to encrypt or 'd' to decrypt: ")
message = input("Enter the message: ")
shift = int(input("Enter the shift number: "))

result = ""

for char in message:
    if choice == 'e':
        result += chr((ord(char) + shift))
    elif choice == 'd':
        result += chr((ord(char) - shift))

print(result)

