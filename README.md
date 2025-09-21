🔐 Projeto CyberSecurity – API de Demonstração
📌 Objetivo

Este projeto foi desenvolvido como parte de um desafio acadêmico de Cibersegurança.
A aplicação implementa uma API simples em Python + Flask, utilizada para exercícios práticos de segurança (SAST, DAST, SCA, autenticação e criptografia).

⚠️ Atenção: Este não é um assessor oficial nem um produto pronto para produção. Trata-se de um projeto didático, criado apenas para fins de estudo.

⚙️ Tecnologias

Python 3.12

Flask

Ferramentas de segurança:

SAST → Semgrep

SCA → pip-audit

DAST → OWASP ZAP

Autenticação → Token Bearer simples

Criptografia → uso de variáveis de ambiente simulando segredos

▶️ Como rodar a aplicação

1. Clonar o repositório:

git clone git clone https://github.com/SEU-USUARIO/projeto-cybersecurity.git
cd projeto-cybersecurity/src

cd projeto-cybersecurity/src


2. Instalar dependências:

pip install -r requirements.txt


3. Rodar a API:

python app.py


4. Acessar:

http://127.0.0.1:5000/ → raiz

http://127.0.0.1:5000/investimentos → lista de investimentos

http://127.0.0.1:5000/secure-data → endpoint protegido

🔍 Testes de Segurança

SAST (Semgrep) → análise estática de código

SCA (pip-audit) → auditoria de dependências

DAST (OWASP ZAP) → testes dinâmicos contra a API

Autenticação e Autorização → verificação de acesso com/sem token

Criptografia e Gestão de Segredos → uso de variáveis de ambiente

As evidências dos testes encontram-se na pasta /evidencias.
