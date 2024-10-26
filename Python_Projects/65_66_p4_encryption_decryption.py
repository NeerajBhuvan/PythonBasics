lower_case_alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
upper_case_alphabets = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# (x(index) + shift_key) % 26 => (0 + 3) % 26 => 3 % 26 = 3
def cryption_operation(cryption, message_array, shift_key):
    def operation_value(crypt, index, key):
        if crypt == "decrypt":
            crypt_value = index - key
            if crypt_value < 0:
                crypt_value += 26
        else:
            crypt_value = index + key
        return crypt_value

    cipher_text = ""
    for k in range(len(message_array)):
        if message_array[k] in upper_case_alphabets:
            index_value = upper_case_alphabets.index(message_array[k])
            operation = operation_value(cryption, index_value, shift_key)
            cipher_text += upper_case_alphabets[operation % 26]
        elif message_array[k] in lower_case_alphabets:
            index_value = lower_case_alphabets.index(message_array[k])
            operation = operation_value(cryption, index_value, shift_key)
            cipher_text += lower_case_alphabets[operation % 26]
        else:
            cipher_text += message_array[k]
    print(f"Here is your text after {cryption}ion: {cipher_text}")


def find_encrypt_decrypt(crypt):
    message = input("Type your message: ")
    shift_key = int(input("Type the shift number: "))
    message_array = []
    for i in range(len(message)):
        message_array.append(message[i])
    if crypt == "encrypt":
        cryption_operation("encrypt", message_array, shift_key)
    else:
        cryption_operation("decrypt",message_array, shift_key)


iteration = 'yes'
while iteration == 'yes':
    type_crypt = input("Type 'encrypt' for encryption, type 'decrypt' for decryption: ")
    if type_crypt == "encrypt" or type_crypt == "decrypt":
        find_encrypt_decrypt(type_crypt)
        iteration = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    else:
        print("Invalid Input!!!")
print("Goodbye!")
