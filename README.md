# Password Compliance Auditor

Script em Python para validação de força de senhas e verificação de conformidade com políticas de segurança customizáveis.

## Descrição
Diferente de validadores simples baseados apenas em comprimento (`len`), esta ferramenta implementa:
1.  **Cálculo de Entropia de Shannon:** Medição quantitativa da incerteza da senha em bits.
2.  **Validação de Regras (Regex):** Checagem booleana contra requisitos de complexidade (maiúsculas, dígitos, símbolos).
3.  **Heurística de Padrões:** Detecção de sequências comuns e strings previsíveis que falhariam em ataques de dicionário.

## Funcionalidades
* Configuração de política de segurança via dicionário (`POLITICA_EMPRESA`).
* Feedback granular sobre o motivo da rejeição (ex: entropia insuficiente vs. falta de caracteres especiais).
* Execução via CLI (Command Line Interface).

## Instalação e Uso

```bash
# Clonar repositório
git clone [https://github.com/Johnzitos/auditor-compliance-senhas.git](https://github.com/Johnzitos/auditor-compliance-senhas.git)

# Executar
python verificador.py
