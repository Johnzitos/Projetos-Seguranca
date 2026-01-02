# Forensic File Signature Scanner

**Ferramenta de Análise Forense e Detecção de Malware baseada em Magic Numbers.**
Identifica arquivos ocultos, spoofing de extensão e valida integridade de tipos de arquivo.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python)
![Category](https://img.shields.io/badge/Category-Digital_Forensics-blue?style=flat&logo=kalilinux)
![Status](https://img.shields.io/badge/Status-Stable-success?style=flat)

---

## O Problema: Extension Spoofing

Em ataques cibernéticos e cenários de perícia digital, confiar na extensão do arquivo é um erro fatal. O sistema operacional (Windows/Linux) utiliza a extensão (ex: `.jpg`, `.pdf`) para decidir qual programa abrir, mas o conteúdo real do arquivo é definido pelos seus **Magic Bytes** (Assinatura Hexadecimal).

Atacantes frequentemente utilizam a técnica de **Extension Spoofing** (Falsificação de Extensão) para camuflar malwares:
* Renomear um `ransomware.exe` para `fatura.pdf`.
* Esconder um script malicioso dentro de uma pasta de imagens.

Analistas de segurança precisam de ferramentas que ignorem o nome e analisem o **conteúdo binário**.

---

## Solução Técnica

Esta ferramenta implementa um motor de análise de assinaturas estáticas. Ela lê os primeiros bytes (Header) de cada arquivo em disco e compara com um banco de dados interno de assinaturas conhecidas (ELF, PE, PNG, PDF, ZIP, etc.).

### Capacidades
* **Detecção de Spoofing:** Alerta imediato se um executável (EXE/ELF) estiver mascarado com uma extensão inofensiva (JPG/TXT).
* **Identificação Real:** Revela o verdadeiro tipo de arquivos sem extensão ou com extensões corrompidas.
* **Recursividade:** Capacidade de varrer diretórios inteiros em busca de anomalias.
* **Tutorial Integrado:** Possui manual de operação embutido na CLI (`--tutorial`).

---

## Arquitetura

O funcionamento baseia-se na leitura hexadecimal do cabeçalho do arquivo:

```mermaid
graph LR
    A[Arquivo Alvo] -->|Read Binary| B(Extrair 32 Bytes Iniciais)
    B -->|Hex Conversion| C{Comparar com DB}
    C -->|Match| D[Identificar Tipo Real]
    D --> E{Check Extensão}
    E -->|Compatível| F[Status: MATCH]
    E -->|Incompatível & Perigoso| G[Status: SPOOF / ALERT]
