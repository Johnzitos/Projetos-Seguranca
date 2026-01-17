import sys
import time
import logging
from collections import defaultdict
from scapy.all import sniff, IP, TCP, conf

# Configuração de Logging (Arquivo continua registrando tudo)
logging.basicConfig(
    filename='dos_security_events.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class DoSDetector:
    def __init__(self, interface="eth0", threshold_pkt=1000, threshold_syn=100, time_window=10):
        self.interface = interface
        self.threshold_pkt = threshold_pkt
        self.threshold_syn = threshold_syn
        self.time_window = time_window
        
        self.ip_count = defaultdict(int)
        self.syn_count = defaultdict(int)
        self.start_time = time.time()
        self.blocked_ips = set()
        self.last_print_time = 0

    def _reset_counters(self):
        """Reseta contadores silenciosamente."""
        self.ip_count.clear()
        self.syn_count.clear()
        self.blocked_ips.clear()
        self.start_time = time.time()

    def _log_alert(self, message, src_ip, level="WARNING"):
        """Quebra a linha de status e exibe o alerta."""
        if src_ip not in self.blocked_ips:
            # Pula uma linha para não sobrescrever o status atual
            print("\n") 
            color = Colors.FAIL if level == "CRITICAL" else Colors.WARNING
            
            alert_msg = f"{color}{Colors.BOLD}>>> ALERTA DE SEGURANÇA DETECTADO <<<{Colors.ENDC}"
            detail_msg = f"{color}[!] {message}{Colors.ENDC}"
            
            print(alert_msg)
            print(detail_msg)
            print("-" * 50) # Separador visual
            
            logging.warning(message)
            self.blocked_ips.add(src_ip)

    def packet_callback(self, packet):
        current_time = time.time()
        
        # 1. Reset da Janela
        if current_time - self.start_time > self.time_window:
            self._reset_counters()

        # 2. Coleta de Dados (Background)
        if IP in packet:
            src_ip = packet[IP].src
            self.ip_count[src_ip] += 1

            if TCP in packet and packet[TCP].flags == 'S':
                self.syn_count[src_ip] += 1

            # 3. Visualização "Heartbeat" (Status OK)
            # Atualiza apenas a cada 2 segundos para não piscar a tela
            if current_time - self.last_print_time >= 2.0:
                timestamp = time.strftime('%H:%M:%S')
                # \r retorna o cursor para o inicio da linha, permitindo sobrescrever
                sys.stdout.write(f"\r{Colors.GREEN}[*] Status [{timestamp}]: ✔️  Rede Operacional (Nenhuma anomalia detectada){Colors.ENDC}   ")
                sys.stdout.flush()
                self.last_print_time = current_time

            # 4. Motor de Detecção
            if self.ip_count[src_ip] > self.threshold_pkt:
                self._log_alert(f"Tráfego Volumétrico: IP {src_ip} enviou {self.ip_count[src_ip]} pacotes em {self.time_window}s", src_ip, "CRITICAL")

            if self.syn_count[src_ip] > self.threshold_syn:
                self._log_alert(f"Ataque SYN Flood: IP {src_ip} iniciou {self.syn_count[src_ip]} conexões em {self.time_window}s", src_ip, "WARNING")

    def start(self):
        print(f"{Colors.HEADER}{'='*60}")
        print(f"   SENTINELA - MONITOR DE SEGURANÇA (MODO SILENCIOSO)")
        print(f"{'='*60}{Colors.ENDC}")
        print(f"[*] Interface: {Colors.BOLD}{self.interface}{Colors.ENDC}")
        print(f"[*] Modo: Apenas Alertas Críticos")
        print(f"[*] Log: dos_security_events.log")
        print("-" * 60)
        
        conf.verb = 0 
        
        try:
            sniff(iface=self.interface, prn=self.packet_callback, store=False)
        except KeyboardInterrupt:
            print(f"\n\n{Colors.BLUE}[*] Monitoramento encerrado com segurança.{Colors.ENDC}")
        except Exception as e:
            print(f"\n\n{Colors.FAIL}[!] Erro Crítico: {e}{Colors.ENDC}")

if __name__ == "__main__":
    # Tenta detectar a interface automaticamente, ou usa wlan0/eth0
    target_interface = "wlan0" 
    
    # CONFIGURAÇÃO DE PRODUÇÃO (Valores mais realistas)
    detector = DoSDetector(
        interface=target_interface, 
        threshold_pkt=2000,   # Aumentado para 2000 pacotes a cada 10s
        threshold_syn=200,    # Aumentado para 200 SYNs (início de conexão)
        time_window=10
    )
    detector.start()