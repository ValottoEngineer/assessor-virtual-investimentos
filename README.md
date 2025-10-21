🔐 Projeto CyberSecurity – API de Demonstração
📌 Objetivo

Este projeto foi desenvolvido como parte de um desafio acadêmico de Cibersegurança.
A aplicação implementa uma API simples em Python + Flask, utilizada para exercícios práticos de segurança (SAST, DAST, SCA, autenticação e criptografia).

⚠️ Atenção: Este não é um assessor oficial nem um produto pronto para produção. Trata-se de um projeto didático, criado apenas para fins de estudo.

⚙️ Tecnologias e Ferramentas

Python 3.12 | Flask

SAST → Semgrep (análise estática de código)

SCA → pip-audit (verificação de dependências)

DAST → OWASP ZAP (testes dinâmicos de segurança)

Autenticação → JWT com RBAC (perfil user/admin)

Criptografia → variáveis de ambiente para segredos [SECRET_KEY]

▶️ Como rodar a aplicação

1. Clonar o repositório:

git clone git clone https://github.com/SEU-USUARIO/projeto-cybersecurity.git
cd projeto-cybersecurity/src

cd projeto-cybersecurity/src


2. Instalar dependências:

pip install -r requirements.txt


3. Rodar a API:

python app.py


Acesse:

http://127.0.0.1:5000/ – endpoint raiz

/investimentos – lista de investimentos

/secure-data – rota protegida (JWT)

/consent – gerenciamento de consentimento (LGPD)

🔍 Testes de Segurança

| Tipo            | Ferramenta             | Descrição                                     |
| --------------- | ---------------------- | --------------------------------------------- |
| **SAST**        | Semgrep                | análise estática do código-fonte              |
| **SCA**         | pip-audit              | auditoria de dependências Python              |
| **DAST**        | OWASP ZAP              | simulação de ataques HTTP/HTTPS               |
| **Auth / RBAC** | JWT + decorators Flask | controle de acesso por papéis                 |
| **LGPD**        | Consent API            | registro e revogação de consentimento         |
| **CI/CD**       | GitHub Actions         | execução automática de testes pytest + CodeQL |

🧾 Licença

Projeto acadêmico – FIAP (2025).
Uso restrito a fins educacionais.
