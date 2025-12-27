# Auditor de Compliance de Senhas

Ferramenta de linha de comando (CLI) desenvolvida em Python para auditoria de credenciais. O software valida a força de senhas confrontando-as com políticas de segurança corporativas configuráveis e métricas matemáticas de entropia.

## Objetivo
Fornecer um mecanismo automatizado para verificar se credenciais de usuários atendem aos requisitos de complexidade exigidos por normas de segurança (como PCI-DSS e ISO 27001), mitigando vetores de ataque baseados em dicionário e força bruta.

## Funcionalidades Técnicas

### 1. Validação de Política (Compliance)
Verificação booleana contra um conjunto de regras predefinido (`POLITICA_EMPRESA`), assegurando:
* Comprimento mínimo obrigatório.
* Presença de múltiplos conjuntos de caracteres (maiúsculas, numéricos, especiais).
* Rejeição de sequências comuns.

### 2. Cálculo de Entropia de Shannon
Utilização da fórmula de entropia da informação para quantificar a imprevisibilidade da senha em bits:
* H = L * log2(R)
* Onde *L* é o comprimento da senha e *R* é o tamanho do pool de caracteres utilizados.

### 3. Detecção de Padrões
Implementação de heurística para identificar e bloquear padrões previsíveis (ex: sequências numéricas ou alfabéticas) frequentemente explorados em ataques de engenharia social.

## Instalação e Execução

Pré-requisitos: Python 3.x instalado.

```bash
# 1. Clonar o repositório
git clone [https://github.com/Johnzitos/Projetos-Seguranca.git](https://github.com/Johnzitos/Projetos-Seguranca.git)

# 2. Acessar o diretório do projeto
cd Projetos-Seguranca/Projeto-01-Auditor-Senha

# 3. Executar o script
python verificador.py
