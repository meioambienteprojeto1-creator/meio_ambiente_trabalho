#  Projeto Meio Ambiente

##  Descrição

Aplicação web desenvolvida em **Python com Flask** e **Firebase Firestore** para divulgação de campanhas ambientais.  

O sistema permite:
-  Visualização de campanhas
-  Busca de campanhas por título ou descrição
-  Cadastro de usuários
-  Contato via formulário
-  Login básico (usuário/admin)

As páginas usam **Jinja2** para renderização dinâmica dos templates.

---

##  Tecnologias Utilizadas

- Python 3.x
- Flask
- Jinja2
- Firebase Firestore
- Firebase Admin SDK
- Flask-Mail
- Werkzeug (para hash de senha)
- HTML5 / CSS3
- Git e GitHub


---

##  Instruções de Execução

### 1 Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2 Instalar dependências

```bash
pip install flask firebase-admin flask-mail
```

Ou usando `requirements.txt` (se existir):

```bash
pip install -r requirements.txt
```

### 3 Configurar Firebase

1. Acesse o [Console do Firebase](https://console.firebase.google.com/)
2. Crie um projeto (ou use um existente)
3. Vá em **Configurações do Projeto** → **Contas de Serviço**
4. Clique em **Gerar nova chave privada**
5. Salve o arquivo como `serviceAccountKey.json` na raiz do projeto

### 4 Configurar Firestore

1. No Firebase Console, vá em **Firestore Database**
2. Crie a coleção `campanhas`
3. Adicione documentos com esta estrutura:

```json
{
  "id": 0,
  "titulo": "Nome da Campanha",
  "descricao": "Descrição da campanha ambiental"
}
```

### 5 Configurar Email (Flask-Mail)

No arquivo `main.py`, altere as credenciais de email:

```python
app.config['MAIL_USERNAME'] = 'seu-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'sua-senha-de-app'
```

** Como gerar senha de aplicativo:**
1. Acesse [Conta Google](https://myaccount.google.com/)
2. Vá em **Segurança** → **Verificação em duas etapas** (ative se necessário)
3. Clique em **Senhas de app** e gere uma nova
4. Use essa senha no código

### 6 Estrutura de Pastas

Certifique-se de ter esta estrutura:

```
projeto-meio-ambiente/
│
├── main.py
├── serviceAccountKey.json
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── cadastro.html
│   ├── campanha.html
│   ├── descricao.html
│   └── contato.html
│
└── static/
    └── icons/
        └── favicon.ico
```

### 7 Executar a aplicação

```bash
python main.py
```

 Acesse em: `http://localhost:80`

### 8 Fazer login

**Usuários de teste:**
- **Admin:** usuário `admin` / senha `1234`
- **Usuário:** usuário `usuario` / senha `senha123`

Ou cadastre-se em `/cadastro`

---

##  Rotas da Aplicação

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial com campanhas |
| `/login` | GET, POST | Página de login |
| `/logout` | GET | Logout do sistema |
| `/cadastro` | GET, POST | Cadastro de novos usuários |
| `/campanha?q=busca` | GET | Busca de campanhas |
| `/descricao/<id>` | GET | Detalhes da campanha |
| `/contato` | GET, POST | Formulário de contato |

---

##  Segurança

 **IMPORTANTE antes de colocar em produção:**

1. **Mude a chave secreta:**
```python
app.secret_key = "sua-chave-aleatoria-super-segura"
```

2. **Use variáveis de ambiente** para senhas:
```python
import os
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
```

3. **Crie um arquivo `.gitignore`:**
```
serviceAccountKey.json
*.pyc
__pycache__/
.env
venv/
```

4. **Desative debug em produção:**
```python
app.run(debug=False)
```

---

##  Solução de Problemas

###  Erro: "No module named 'firebase_admin'"
**Solução:**
```bash
pip install firebase-admin
```

###  Erro ao enviar email
**Solução:**
- Verifique se a senha de aplicativo está correta
- Confirme que a verificação em duas etapas está ativada
- Teste com outro email

###  Erro: "Could not open serviceAccountKey.json"
**Solução:**
- Verifique se o arquivo está na raiz do projeto
- Confirme que o nome está correto (case-sensitive)

###  Porta 80 já em uso
**Solução:**
```bash
export PORT=8080
python main.py
```

---

##  Licença

Este projeto foi desenvolvido para fins educacionais.

---

##  Contato

Para dúvidas ou sugestões, entre em contato através do formulário da aplicação ou envie email para: `meioambienteprojeto1@gmail.com`

---

