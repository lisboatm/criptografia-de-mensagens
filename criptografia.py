def encrypt_message(message):
    # Primeira passada: deslocar letras em +3 na tabela ASCII
    first_pass = []
    for char in message:
        if char.isalpha():
            first_pass.append(chr(ord(char) + 3))
        else:
            first_pass.append(char)
    first_pass = ''.join(first_pass)
    
    # Segunda passada: inverter a string
    second_pass = first_pass[::-1]
    
    # Terceira passada: deslocar -1 para cada caractere da segunda metade da string
    n = len(second_pass)
    third_pass = list(second_pass)
    for i in range(n // 2, n):
        third_pass[i] = chr(ord(third_pass[i]) - 1)
    
    return ''.join(third_pass)

# Função principal para leitura da entrada e exibição da saída
def main():
    n = int(input())
    for _ in range(n):
        message = input()
        encrypted_message = encrypt_message(message)
        print(encrypted_message)

if __name__ == "__main__":
    main()
