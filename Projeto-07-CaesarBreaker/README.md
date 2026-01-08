# Caesar Cipher Frequency Breaker

**Ferramenta de Criptoanálise Estatística baseada em Frequência de Linguagem.**
Automação de Quebra de Cifras, Análise Heurística e Recuperação de Texto Plano.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python)
![Security](https://img.shields.io/badge/Security-Cryptography-orange?style=flat)
![Status](https://img.shields.io/badge/Status-Stable-success?style=flat)

---

## Contexto de Negócio

A utilização de algoritmos de criptografia obsoletos ou a implementação de "segurança por obscuridade" representa um risco severo para a integridade da informação:

1.  **Falsa Sensação de Segurança:** Algoritmos de substituição simples (como a Cifra de César) são trivialmente reversíveis, expondo dados confidenciais que se acreditavam protegidos.
2.  **Impacto de Vazamentos:** A interceptação de mensagens cifradas com métodos fracos permite a leitura imediata por adversários, comprometendo a confidencialidade da comunicação corporativa.
3.  **Fundamentação Teórica:** Compreender as vulnerabilidades estatísticas da criptografia clássica é o alicerce para a implementação e auditoria de padrões modernos (AES, RSA).

A tentativa de quebra manual de cifras é ineficiente e não escalável. Este projeto soluciona este problema através da automação da análise estatística de linguagem natural.

---

## Solução Técnica

Esta ferramenta atua como um **Motor de Criptoanálise**, aplicando métodos de frequência de caracteres para deduzir a chave de criptografia e recuperar a mensagem original sem conhecimento prévio (Keyless Decryption).

### Capacidades Principais

* **Análise de Frequência:** Comparação vetorial entre a distribuição de caracteres do texto cifrado e o corpus padrão da língua portuguesa (PT-BR).
* **Autodetecção de Chave:** Identificação automática do deslocamento (shift) utilizado, eliminando a necessidade de intervenção humana.
* **Pontuação Heurística:** Algoritmo de scoring que classifica a legibilidade do texto resultante, priorizando resultados semânticos em detrimento de sequências aleatórias.
* **Processamento de Texto:** Normalização e preservação de estrutura, garantindo a integridade da formatação original após a decifragem.

---

## Arquitetura e Fluxo de Execução

O decodificador opera através de um pipeline linear de processamento estatístico:

```mermaid
graph TD
    A[Input: Texto Cifrado] -->|Normalização| B(Gerador de Permutações)
    B -->|Rotação 0-25| C{Engine de Frequência}
    C -->|Comparação Corpus PT-BR| D[Cálculo de Score]
    D -->|Ordenação| E[Ranking de Probabilidade]
    E -->|Seleção do Melhor Score| F[Output: Texto Plano e Chave]