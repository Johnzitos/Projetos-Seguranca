# Network Port Scanner (TCP)

Ferramenta de reconhecimento de rede (Recon) desenvolvida em Python. O script utiliza sockets brutos para identificar serviços ativos em um host alvo, simulando a etapa de "Scanning" de um teste de intrusão.

## Descrição Técnica
O scanner opera enviando solicitações de conexão TCP (Three-way Handshake parcial) para uma lista de portas padronizada.
* **Biblioteca:** Utiliza `socket` nativo, sem dependências de terceiros (como Nmap ou Scapy), demonstrando compreensão dos fundamentos do protocolo TCP/IP.
* **Mecanismo:** Implementa `socket.connect_ex()` para tratamento de erros sem interrupção da execução.
* **Resolução de Nomes:** Converte automaticamente domínios (DNS) para endereços IPv4.

## Funcionalidades
1. **Varredura de Portas Comuns:** Foca nas portas mais críticas (21, 22, 80, 443, 3306, etc.).
2. **Feedback Visual:** Interface de console que informa o progresso em tempo real, evitando a percepção de travamento (hang) durante timeouts de firewall.
3. **Identificação de Serviços:** Mapeia o número da porta para o nome do serviço padrão (ex: 80 -> http).

## Instalação e Uso

```bash
# 1. Acessar o diretório do projeto
cd Projetos-Seguranca/Projeto-02-PortScanner

# 2. Executar o script
python3 scanner.py
