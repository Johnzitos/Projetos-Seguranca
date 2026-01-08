#!/usr/bin/env python3
import sys
import argparse


class C:
    G = '\033[92m' # Green
    Y = '\033[93m' # Yellow
    B = '\033[94m' # Blue
    C = '\033[96m' # Cyan
    E = '\033[0m'  # End


PT_FREQ = {
    'a': 14.63, 'b': 1.04, 'c': 3.88, 'd': 4.99, 'e': 12.57, 'f': 1.02,
    'g': 1.30, 'h': 1.28, 'i': 6.18, 'j': 0.40, 'k': 0.02, 'l': 2.78,
    'm': 4.74, 'n': 5.05, 'o': 10.73, 'p': 2.52, 'q': 1.20, 'r': 6.53,
    's': 7.81, 't': 4.34, 'u': 4.63, 'v': 1.67, 'w': 0.01, 'x': 0.21,
    'y': 0.01, 'z': 0.47
}

def get_score(text):
    """Calcula uma pontuação baseada na frequência de letras do Português."""
    score = 0
    text = text.lower()
    for char in text:
        if char in PT_FREQ:
            score += PT_FREQ[char]
    return score

def decrypt(text, shift):
    """Desloca os caracteres para trás baseados no shift (chave)."""
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            original_char = chr((ord(char) - start - shift) % 26 + start)
            result.append(original_char)
        else:
            result.append(char)
    return "".join(result)

def print_tutorial():
    print(rf"""{C.B}
  MANUAL DE OPERAÇÃO - CAESAR BREAKER
  ==================================={C.E}

  {C.Y}1. O QUE É ESTA FERRAMENTA?{C.E}
  Este script realiza criptoanálise estatística em textos cifrados com a 
  Cifra de César. Ele não usa força bruta cega; ele analisa a frequência 
  das letras para determinar qual das 26 rotações possíveis mais se 
  assemelha à língua portuguesa.

  {C.Y}2. COMO USAR{C.E}
  Execute o script passando o texto cifrado entre aspas.
  
    {C.G}>>> python caesar_breaker.py "TEXTO CIFRADO AQUI"{C.E}

  {C.Y}3. ENTENDENDO A SAÍDA{C.E}
    - {C.G}MELHOR RESULTADO:{C.E} A frase com maior probabilidade estatística.
    - {C.C}Score:{C.E} Pontuação de similaridade com o português (quanto maior, melhor).
    - {C.Y}Outras Possibilidades:{C.E} Alternativas caso a análise principal falhe.

  {C.B}==================================={C.E}
    """)

def break_cipher(ciphertext):
    print(f"{C.B}[*] Iniciando Análise de Frequência...{C.E}\n")
    
    candidates = []

    for shift in range(26):
        plaintext = decrypt(ciphertext, shift)
        score = get_score(plaintext)
        candidates.append((score, shift, plaintext))

    
    candidates.sort(key=lambda x: x[0], reverse=True)

    best_score, best_shift, best_text = candidates[0]
    

    print(rf"""{C.C}
   ___ __ _  ___ ___  __ _ _ __ 
  / __/ _` |/ _ \/ __|/ _` | '__|
 | (_| (_| |  __/\__ \ (_| | |   
  \___\__,_|\___||___/\__,_|_|   v1.1{C.E}
    """)

    print(f"{C.G}>>> MELHOR RESULTADO (Provável Chave: {best_shift}){C.E}")
    print(f"    Texto: {best_text}")
    print(f"    Score: {best_score:.2f}\n")

    print(f"{C.Y}[Outras Possibilidades]{C.E}")
    for i in range(1, 3):
        score, shift, text = candidates[i]
        print(f"    Shift {shift:02}: {text} (Score: {score:.2f})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Caesar Cipher Frequency Breaker")
    parser.add_argument("text", nargs='?', help="Texto criptografado para quebrar")
    parser.add_argument("-t", "--tutorial", action="store_true", help="Exibe o manual de uso")
    args = parser.parse_args()

    if args.tutorial:
        print_tutorial()
    elif args.text:
        break_cipher(args.text)
    else:
        parser.print_help()
