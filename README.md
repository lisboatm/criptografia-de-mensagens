# 📄 Desafio K: Criptografia de Mensagens

## Descrição do Problema
Você foi solicitado a criar um programa simples de criptografia que permita enviar mensagens codificadas para que ninguém consiga lê-las diretamente. O processo de criptografia é dividido em três etapas:

### **Etapas da Criptografia**
1. **Deslocamento de Caracteres**:
   - Para cada caractere na linha:
     - Letras minúsculas (`a-z`) e maiúsculas (`A-Z`) devem ser deslocadas **3 posições para a direita** na tabela ASCII.
     - Outros caracteres (números, espaços, símbolos) **não sofrem alterações**.

2. **Inversão da String**:
   - A string resultante da primeira etapa é **invertida**.

3. **Deslocamento Parcial**:
   - A partir da **metade da string invertida** (arredondada para baixo), cada caractere é deslocado **1 posição para a esquerda** na tabela ASCII.

## 📥 Entrada
- A primeira linha contém um número inteiro `N` (1 ≤ N ≤ 100), representando o número de linhas que precisam ser criptografadas.
- As próximas `N` linhas contêm mensagens com até **1.000 caracteres** cada, que precisam ser processadas conforme as etapas descritas.

## 📤 Saída
- Para cada linha de entrada, o programa deve imprimir a mensagem criptografada após as três etapas de codificação.

## 📌 Exemplo

**Entrada:**
```
4
Texto #3
vxpdylY .ph
vv.xwfxo.fd
gi.r{h
```

**Saída esperada:**
```
3# rvzgV
3vCw pm.
gi.r{h
gi.r{h
```

---

## 💡 Lógica Utilizada na Solução

### **Etapa 1: Deslocamento de Caracteres (+3)**
- Para cada caractere da linha:
  - Se for uma letra (`a-z` ou `A-Z`), deslocar **+3 posições** na tabela ASCII.
  - Se for um caractere especial (número, espaço ou símbolo), **não alterar**.

### **Etapa 2: Inversão da String**
- Inverter a string resultante da primeira etapa.

### **Etapa 3: Deslocamento Parcial (-1)**
- A partir da **segunda metade da string invertida** (usando o índice `len(string) // 2`), deslocar cada caractere **-1 posição** na tabela ASCII.

## 🛠️ Implementação em Python

```python
def encrypt_message(message):
    # Primeira etapa: deslocar letras em +3 na tabela ASCII
    first_pass = []
    for char in message:
        if char.isalpha():
            first_pass.append(chr(ord(char) + 3))
        else:
            first_pass.append(char)
    first_pass = ''.join(first_pass)
    
    # Segunda etapa: inverter a string
    second_pass = first_pass[::-1]
    
    # Terceira etapa: deslocar -1 para cada caractere da segunda metade da string
    n = len(second_pass)
    third_pass = list(second_pass)
    for i in range(n // 2, n):
        third_pass[i] = chr(ord(third_pass[i]) - 1)
    
    return ''.join(third_pass)

def main():
    n = int(input())
    for _ in range(n):
        message = input()
        encrypted_message = encrypt_message(message)
        print(encrypted_message)

if __name__ == "__main__":
    main()
```

---

## ⚙️ Como Executar o Código

1. **Copie o código acima** para um arquivo Python, por exemplo, `criptografia.py`.
2. **Execute** o programa em um terminal:
   ```bash
   python3 criptografia.py
   ```
3. **Insira o número de linhas e as mensagens** conforme o exemplo de entrada.

---

## 🧩 Complexidade
- A complexidade do programa é \( O(n) \) para cada linha, onde \( n \) é o número de caracteres na linha.
- O programa é altamente eficiente, suportando até **100 linhas** com **1.000 caracteres** cada.

---

## 🛠️ Possíveis Problemas e Soluções
- **Erros de execução (Runtime Error)**: Certifique-se de que a entrada está no formato correto.
- **Erros de apresentação (Presentation Error)**: Verifique que não há espaços ou quebras de linha adicionais na saída.

---

## 📚 Referências
- Funções nativas do Python:
  - `ord()`: Obtém o código ASCII de um caractere.
  - `chr()`: Obtém o caractere a partir de um código ASCII.
  - `[::-1]`: Inverte uma string.
