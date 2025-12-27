import socket
import sys
from datetime import datetime

def escanear_alvo(alvo, portas):
    print("-" * 50)
    print(f"Alvo: {alvo}")
    print(f"Início: {datetime.now()}")
    print("-" * 50)

    try:
        ip_alvo = socket.gethostbyname(alvo)
        print(f"IP resolvido: {ip_alvo}\n")
        
        for porta in portas:
            print(f"Verificando porta {porta}...", end="\r")
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            
            resultado = s.connect_ex((ip_alvo, porta))
            
            if resultado == 0:
                servico = obter_servico(porta)
                print(f" "*30, end="\r") 
                print(f"[OPEN] Porta {porta}: {servico}")
            
            s.close()
            
    except KeyboardInterrupt:
        print("\n[!] Escaneamento interrompido pelo usuário.")
        sys.exit()
    except socket.gaierror:
        print("\n[!] Erro: Nome do host não pôde ser resolvido.")
        sys.exit()
    except socket.error:
        print("\n[!] Erro: Não foi possível conectar ao servidor.")
        sys.exit()

    print("-" * 50)
    print("Escaneamento finalizado.")

def obter_servico(porta):
    try:
        return socket.getservbyport(porta)
    except:
        return "Desconhecido"

if __name__ == "__main__":
    portas_comuns = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 8080]
    
    target = input("Digite o IP ou domínio para escanear (ex: scanme.nmap.org): ")
    escanear_alvo(target, portas_comuns)