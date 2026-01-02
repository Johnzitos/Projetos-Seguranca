#!/usr/bin/env python3
import sys
import os
import json
import argparse
import binascii

class C:
    G = '\033[92m'
    R = '\033[91m'
    Y = '\033[93m'
    B = '\033[94m'
    C = '\033[96m'
    E = '\033[0m'

class FileSignatureScanner:
    def __init__(self, targets=None, sig_file="signatures.json"):
        # Garante que targets seja sempre uma lista, mesmo que vazio
        self.targets = targets if targets else []
        self.signatures = self.load_signatures(sig_file)
        self.scan_count = 0
        self.mismatch_count = 0
        
        # Arquivos do próprio projeto para ignorar automaticamente
        self.ignore_list = ["sig_scanner.py", "signatures.json", "README.md", "requirements.txt", ".gitignore"]

    def load_signatures(self, path):
        try:
            if not os.path.exists(path): return {}
            with open(path, "r") as f:
                return json.load(f)
        except: return {}

    def get_file_signature(self, filepath):
        try:
            with open(filepath, "rb") as f:
                header = f.read(32)
                return binascii.hexlify(header).decode().upper()
        except: return None

    def analyze_file(self, filepath):
        filename = os.path.basename(filepath)
        
        # Filtro Inteligente: Pula arquivos do sistema da ferramenta
        if filename in self.ignore_list or filename.startswith("."):
            return

        file_hex = self.get_file_signature(filepath)
        if not file_hex: return

        detected_type = "Unknown"
        longest_match = 0

        for magic, filetype in self.signatures.items():
            if file_hex.startswith(magic):
                if len(magic) > longest_match:
                    longest_match = len(magic)
                    detected_type = filetype

        try: ext = os.path.splitext(filename)[1].lower()
        except: ext = ""
        
        status_msg = f"{C.C}MATCH{C.E}"
        warning = ""

        # Lógica de Detecção
        if "Executable" in detected_type and ext not in ['.exe', '.dll', '.bin', '.elf']:
            status_msg = f"{C.R}SPOOF{C.E}"
            warning = f" {C.R}[!!!] SUSPICIOUS: Hidden Executable as {ext}{C.E}"
            self.mismatch_count += 1
        elif detected_type == "Unknown":
            status_msg = f"{C.Y}UNKNW{C.E}"

        print(f"[{status_msg}] {filename:<25} | Magic: {file_hex[:8]}... | Type: {detected_type}{warning}")
        self.scan_count += 1

    def print_tutorial(self):
        print(rf"""{C.B}
  MANUAL DE OPERAÇÃO - MAGIC BYTES FORENSICS
  =========================================={C.E}

  {C.Y}1. O QUE É ESTA FERRAMENTA?{C.E}
  Scanner de assinatura hexadecimal para detectar extensão falsa (Spoofing).

  {C.Y}2. COMO USAR (AGORA COM MULTI-TARGET){C.E}
  
    {C.G}>>> Escanear arquivos específicos (pula o resto):{C.E}
    python sig_scanner.py notas.txt praia_ferias.jpg

    {C.G}>>> Escanear tudo na pasta (excluindo o próprio script):{C.E}
    python sig_scanner.py .

  {C.Y}3. LEGENDA{C.E}
    [{C.C}MATCH{C.E}] Seguro.
    [{C.R}SPOOF{C.E}] Perigo! Extensão falsa detectada.

  {C.B}=========================================={C.E}
        """)

    def run(self):
        print(rf"""{C.C}
  ______ _ _        _____ _       
 |  ____(_) |      / ____(_)      
 | |__   _| | ___ | (___  _  __ _ 
 |  __| | | |/ _ \ \___ \| |/ _` |
 | |    | | |  __/ ____) | | (_| |
 |_|    |_|_|\___||_____/|_|\__, |
                             __/ |
                            |___/ v1.2{C.E}
  >> Magic Number Forensics Tool
        """)

        if not self.targets: return

        # Itera sobre CADA alvo passado na linha de comando
        for target in self.targets:
            if os.path.isfile(target):
                self.analyze_file(target)
            elif os.path.isdir(target):
                for root, _, files in os.walk(target):
                    for file in files:
                        self.analyze_file(os.path.join(root, file))
            else:
                print(f"{C.Y}[!] Target not found: {target}{C.E}")
        
        print(f"\n{C.G}[+] Scan Complete.{C.E} Files: {self.scan_count} | Alerts: {self.mismatch_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Forensic File Signature Scanner")
    # nargs='*' permite ZERO ou MAIS argumentos (cria uma lista)
    parser.add_argument("targets", nargs='*', help="Files or Directories to scan")
    parser.add_argument("-t", "--tutorial", action="store_true", help="Show usage manual")
    args = parser.parse_args()

    scanner = FileSignatureScanner(args.targets)

    if args.tutorial:
        scanner.print_tutorial()
    elif args.targets:
        scanner.run()
    else:
        parser.print_help()