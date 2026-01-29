# 🌱 Consciência Ambiental - Plataforma de Campanhas Ambientais

> Uma plataforma web moderna e responsiva dedicada à disseminação de conhecimento e ações concretas para preservar nosso planeta.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-lightblue?logo=flask)](https://flask.palletsprojects.com/)
[![Firebase](https://img.shields.io/badge/Firebase-Active-orange?logo=firebase)](https://firebase.google.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 📚 Índice

- [✨ Características Principais](#características-principais)
- [🛠️ Tecnologias](#tecnologias-utilizadas)
- [🚀 Instalação](#instalação-rápida)
- [🌐 Documentação de API](#documentação-de-api)
- [🤝 Contribuição](#guia-de-contribuição)
- [🐛 Solução de Problemas](#solução-de-problemas)

---

## ✨ Características Principais

- 🌍 **Landing Page Atraente** - Apresentação clara do propósito
- 📱 **Interface Responsiva** - Funciona em desktop, tablet e mobile
- 🔐 **Autenticação Segura** - Login e cadastro com hash de senha
- 📝 **Gerenciamento de Campanhas** - Criar, visualizar e pesquisar
- 🎨 **Design Minimalista** - Interface limpa com tema ambiental
- 💬 **Formulário de Contato** - Comunicação com administradores
- 🖼️ **Upload de Imagens** - Integração com Firebase Storage
- 🔍 **Busca Inteligente** - Procure por título ou descrição

---

## 🛠️ Tecnologias Utilizadas

### Backend

- **Python 3.10+** - Linguagem principal
- **Flask 2.0+** - Framework web minimalista
- **Firebase Admin SDK** - Integração com Google Firebase
- **Flask-Mail** - Sistema de envio de emails
- **Werkzeug** - Hash seguro de senhas

### Frontend

- **HTML5** - Estrutura semântica
- **CSS3** - Estilos responsivos
- **Jinja2** - Templates dinâmicos

### Infraestrutura

- **Firebase Firestore** - Banco de dados NoSQL
- **Firebase Storage** - Armazenamento de imagens
- **SMTP Gmail** - Sistema de emails

---

## 📋 Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes)
- Conta Google com Firebase ativado
- Navegador web moderno

---

## 🚀 Instalação Rápida

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/consciencia-ambiental.git
cd consciencia-ambiental
```

### 2. Criar e Ativar Ambiente Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Firebase

#### 4.1 Obter Credenciais

1. Acesse [Console do Firebase](https://console.firebase.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Vá em **Configurações do Projeto** (⚙️)
4. Acesse **Contas de Serviço**
5. Clique em **Gerar nova chave privada**
6. Salve o JSON como `serviceAccountKey.json` na raiz do projeto

#### 4.2 Configurar Firestore

1. No Firebase Console, acesse **Firestore Database**
2. Crie uma coleção chamada `conteudo`
3. Crie outra coleção chamada `usuarios`
4. A estrutura será criada automaticamente

#### 4.3 Configurar Storage

1. No Firebase Console, acesse **Storage**
2. Crie um novo bucket de armazenamento

### 5. Configurar Email (Opcional)

No arquivo `main.py`, atualize as credenciais:

```python
app.config['MAIL_USERNAME'] = 'seu-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'sua-senha-de-aplicativo'
```

**Gerar senha de aplicativo Google:**

1. Acesse [Conta Google](https://myaccount.google.com/)
2. Vá em **Segurança** > **Verificação em duas etapas** (ative se necessário)
3. Clique em **Senhas de app**
4. Selecione **Mail** e **Windows Computer**
5. Use a senha gerada

### 6. Executar a Aplicação

```bash
python main.py
```

Acesse: **http://localhost:80**

Para usar porta diferente:

```bash
set PORT=8080  # Windows
python main.py
```

---

## 📁 Estrutura do Projeto

```
consciencia-ambiental/
│
├── main.py                    # Aplicação principal
├── requirements.txt           # Dependências Python
├── serviceAccountKey.json     # Credenciais Firebase (não versionar!)
├── README.md                  # Documentação completa
├── devserver.sh               # Script para rodar servidor
│
├── templates/                 # Templates HTML
│   ├── header.html           # Navegação comum
│   ├── index.html            # Página inicial (landing page)
│   ├── campanha.html         # Listagem de campanhas
│   ├── descricao.html        # Detalhes da campanha
│   ├── criar_campanha.html   # Criar campanha
│   ├── login.html            # Login
│   ├── cadastro.html         # Registro
│   └── contato.html          # Contato
│
└── static/                    # Arquivos estáticos
    ├── style.css             # Estilos CSS
    ├── script.js             # JavaScript
    └── icons/                # Ícones
        └── favicon.ico       # Ícone da aba
```

---

## 🗄️ Estrutura do Banco de Dados

### Coleção: `conteudo` (Campanhas)

```json
{
  "id": 1,
  "titulo": "Reflorestamento",
  "descricao": "Campanha para recuperar áreas",
  "descricao_avancada": "Descrição completa...",
  "imagem": "https://firebase-url/imagem.jpg",
  "data": "28/01/2026",
  "autor": "nome_usuario",
  "autor_email": "usuario@email.com"
}
```

### Coleção: `usuarios` (Usuários)

```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "senha": "hash-bcrypt"
}
```

---

## 🌐 Documentação de API

### Autenticação

A aplicação utiliza sessão (session-based authentication). Após login bem-sucedido, a sessão é armazenada no servidor.

### ROTAS PÚBLICAS

#### 1. Página Inicial

**GET** `/`

Retorna a página inicial com informações sobre a plataforma.

**Status:** `200` - Sucesso

---

#### 2. Listar Campanhas

**GET** `/campanha`

Retorna a lista de todas as campanhas ou filtradas por busca.

**Query Parameters:**

```
q (opcional) - string de busca para título ou descrição
```

**Example:**

```
GET /campanha?q=reflorestamento
```

**Status:** `200` - Sucesso | `404` - Nenhuma campanha encontrada

---

#### 3. Detalhes da Campanha

**GET** `/descricao/<id>`

Retorna os detalhes completos de uma campanha específica.

**Path Parameters:**

```
id (required) - ID inteiro da campanha
```

**Example:**

```
GET /descricao/1
```

**Status:** `200` - Sucesso | `404` - Campanha não encontrada

---

#### 4. Formulário de Contato (GET)

**GET** `/contato`

Retorna o formulário de contato.

**Status:** `200` - Sucesso

---

### ROTAS DE AUTENTICAÇÃO

#### 5. Login (GET)

**GET** `/login`

Retorna a página de login.

**Status:** `200` - Sucesso

---

#### 6. Login (POST)

**POST** `/login`

Autentica um usuário.

**Request Body:**

```json
{
  "email": "usuario@email.com",
  "password": "senha123"
}
```

**Status:**

- `200` - Login bem-sucedido
- `401` - Email ou senha incorretos
- `400` - Campos obrigatórios faltando

---

#### 7. Logout

**GET** `/logout`

Encerra a sessão do usuário.

**Status:** `200` - Logout bem-sucedido

---

#### 8. Cadastro (GET)

**GET** `/cadastro`

Retorna o formulário de registro.

**Status:** `200` - Sucesso

---

#### 9. Cadastro (POST)

**POST** `/cadastro`

Registra um novo usuário.

**Request Body:**

```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "password": "senha123",
  "confirmar": "senha123"
}
```

**Validações:**

- Senha mínimo 4 caracteres
- Senhas devem ser iguais
- Email não pode estar duplicado
- Todos os campos são obrigatórios

**Status:**

- `200` - Cadastro bem-sucedido
- `400` - Validação falhou
- `409` - Email já existe

---

### ROTAS DE CONTEÚDO (Requer Autenticação)

#### 10. Criar Campanha (GET)

**GET** `/criar_campanha`

Retorna o formulário para criar uma nova campanha.

**Requer:** Usuário logado

**Status:**

- `200` - Sucesso
- `302` - Redireciona para login se não autenticado

---

#### 11. Criar Campanha (POST)

**POST** `/criar_campanha`

Cria uma nova campanha.

**Requer:** Usuário logado

**Request Body:**

```json
{
  "titulo": "Reflorestamento Mata Atlântica",
  "descricao": "Campanha para recuperar áreas desmatadas",
  "descricao_avancada": "Descrição detalhada da campanha...",
  "data": "28/01/2026"
}
```

**Validações:**

- Título obrigatório
- Descrição obrigatória
- Usuário deve estar autenticado

**Status:**

- `200` - Campanha criada
- `400` - Validação falhou
- `401` - Não autenticado
- `500` - Erro ao salvar

---

#### 12. Formulário de Contato (POST)

**POST** `/contato`

Envia uma mensagem de contato por email.

**Request Body:**

```json
{
  "Nome": "João Silva",
  "Email": "joao@email.com",
  "Mensagem": "Gostaria de informações sobre..."
}
```

**Status:**

- `200` - Email enviado
- `400` - Validação falhou
- `500` - Erro ao enviar email

---

### Tabela Completa de Rotas

| Rota                | Método | Descrição            | Requer Auth |
| ------------------- | ------ | -------------------- | ----------- |
| `/`                 | GET    | Página inicial       | ❌          |
| `/campanha`         | GET    | Listar campanhas     | ❌          |
| `/campanha?q=termo` | GET    | Buscar campanhas     | ❌          |
| `/descricao/<id>`   | GET    | Detalhes da campanha | ❌          |
| `/criar_campanha`   | GET    | Form criar campanha  | ✅          |
| `/criar_campanha`   | POST   | Criar campanha       | ✅          |
| `/login`            | GET    | Página de login      | ❌          |
| `/login`            | POST   | Autenticar usuário   | ❌          |
| `/logout`           | GET    | Logout               | ✅          |
| `/cadastro`         | GET    | Página de registro   | ❌          |
| `/cadastro`         | POST   | Registrar usuário    | ❌          |
| `/contato`          | GET    | Página de contato    | ❌          |
| `/contato`          | POST   | Enviar mensagem      | ❌          |

---

### Códigos de Status HTTP

| Código | Significado  | Descrição                            |
| ------ | ------------ | ------------------------------------ |
| 200    | OK           | Requisição bem-sucedida              |
| 302    | Found        | Redirecionamento (após login/logout) |
| 400    | Bad Request  | Dados inválidos ou faltando          |
| 401    | Unauthorized | Não autenticado                      |
| 404    | Not Found    | Recurso não encontrado               |
| 409    | Conflict     | Email já cadastrado                  |
| 500    | Server Error | Erro interno do servidor             |

---

### Exemplos de Uso com cURL

#### Fazer Login

```bash
curl -X POST http://localhost:80/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "email=usuario@email.com&password=senha123"
```

#### Buscar Campanhas

```bash
curl -X GET "http://localhost:80/campanha?q=reflorestamento"
```

#### Criar Campanha

```bash
curl -X POST http://localhost:80/criar_campanha \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "titulo=Minha%20Campanha&descricao=Descrição&descricao_avancada=Detalhes"
```

#### Enviar Contato

```bash
curl -X POST http://localhost:80/contato \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "Nome=João&Email=joao@email.com&Mensagem=Mensagem%20aqui"
```

---

## 🤝 Guia de Contribuição

Obrigado por estar interessado em contribuir! Aqui está como você pode ajudar.

### 📋 Código de Conduta

Todos os contribuidores devem:

- Ser respeitosos com outras pessoas
- Aceitar críticas construtivas
- Focar no que é melhor para a comunidade
- Demonstrar empatia com outros colaboradores

### 🐛 Reportando Bugs

**Antes de reportar:**

1. Verifique se o bug já foi reportado em Issues
2. Confirme se é um bug real e não um comportamento esperado

**Como reportar:**

```markdown
**Descrição do Bug**
Uma descrição clara do problema.

**Passos para Reproduzir**

1. Vá para '...'
2. Clique em '...'
3. Veja o erro

**Comportamento Esperado**
O que deveria acontecer.

**Comportamento Atual**
O que está acontecendo.
```

### 💡 Sugerindo Melhorias

Crie uma issue com uma descrição clara da melhoria proposta e seu benefício.

### 📝 Processo de Contribuição

#### 1. Fork o Repositório

Clique no botão "Fork" no canto superior direito.

#### 2. Clone seu Fork

```bash
git clone https://github.com/seu-usuario/consciencia-ambiental.git
cd consciencia-ambiental
```

#### 3. Crie uma Branch

```bash
git checkout -b feature/sua-feature
# ou
git checkout -b fix/seu-bug
```

**Convenção de Nomes:**

- `feature/nome-descritivo` - Para novas features
- `fix/nome-descritivo` - Para correções de bugs
- `docs/nome-descritivo` - Para documentação
- `style/nome-descritivo` - Para estilos CSS/formatação

#### 4. Faça suas Mudanças

- Mantenha as mudanças focadas em um único objetivo
- Siga o estilo de código existente
- Adicione comentários quando necessário

#### 5. Commit suas Mudanças

```bash
git add .
git commit -m "Descrição breve das mudanças"
```

**Mensagens de Commit:**

- Use imperativo ("Adiciona recurso" não "Adicionou recurso")
- Primeira linha com até 50 caracteres
- Feche issues com `Closes #123`

#### 6. Push para sua Branch

```bash
git push origin feature/sua-feature
```

#### 7. Abra um Pull Request

1. Vá para o repositório original
2. Clique em "New Pull Request"
3. Descreva as mudanças

### 🎨 Guia de Estilo

#### Python

```python
# Siga PEP 8
# Nomes descritivos
def create_campaign(title, description):
    """Criar uma nova campanha."""
    pass

# Comentários úteis
user_email = "user@example.com"  # Email do usuário - BOM
```

#### HTML

```html
<!-- Use indentação de 2 espaços -->
<!-- Classes descritivas -->
<div class="campaign-card fade-in">
  <h3 class="campaign-title">{{ title }}</h3>
</div>
```

#### CSS

```css
/* Use as variáveis do projeto */
.button {
  padding: var(--space-md);
  background-color: var(--primary);
  border-radius: var(--radius-lg);
}
```

### 🧪 Testes

Antes de submeter um PR:

1. Teste localmente todas as mudanças
2. Verifique se não quebrou funcionalidades existentes
3. Teste em diferentes browsers se alterou frontend
4. Verifique a responsividade se alterou layout

---

## 🔐 Segurança

⚠️ **Antes de PRODUÇÃO:**

1. **Altere a chave secreta:**

   ```python
   app.secret_key = "gere-uma-chave-forte-aleatoria"
   ```

2. **Use variáveis de ambiente:**

   ```bash
   # Crie .env
   FLASK_ENV=production
   MAIL_PASSWORD=sua_senha
   SECRET_KEY=sua_chave
   ```

3. **Crie `.gitignore`:**

   ```
   serviceAccountKey.json
   .env
   __pycache__/
   *.pyc
   venv/
   ```

4. **Desative Debug:**

   ```python
   app.run(debug=False)
   ```

5. **Configure HTTPS**

6. **Valide todas as entradas**

7. **Implemente rate limiting**

---

## 🐛 Solução de Problemas

### Erro: "No module named 'firebase_admin'"

```bash
pip install firebase-admin
```

### Erro: "Could not open serviceAccountKey.json"

- Verifique se o arquivo está na raiz do projeto
- Confirme o nome exato (case-sensitive)
- **Nunca compartilhe este arquivo!**

### Erro ao enviar email

- Verifique credenciais do Gmail
- Confirme verificação em duas etapas ativada
- Use [App Passwords](https://myaccount.google.com/apppasswords)

### Porta 80 em uso

```bash
# Use porta diferente em main.py:
app.run(port=8080)
```

### Firebase retorna erro de autenticação

- Verifique se `serviceAccountKey.json` é válido
- Confirme se as APIs estão habilitadas
- Regenere as credenciais se necessário

---

## 📱 Responsividade

A aplicação foi otimizada para:

- ✅ Desktop (1200px+)
- ✅ Tablet (768px - 1199px)
- ✅ Mobile (até 767px)

---

## 🚢 Deploy (Produção)

### Opções Recomendadas

- **Heroku** - Gratuito inicialmente
- **Google Cloud** - Integração Firebase nativa
- **AWS** - Escalabilidade máxima
- **PythonAnywhere** - Simplicidade Python

### Passos Básicos

1. Configure variáveis de ambiente
2. Desative debug (`debug=False`)
3. Use HTTPS
4. Implemente logging
5. Configure backups automáticos

---

## 📄 Licença

MIT License - Este projeto está licenciado sob a MIT License.

---

## 📞 Contato e Suporte

- **Email**: meioambienteprojeto1@gmail.com
- **GitHub Issues**: [Reporte problemas aqui](https://github.com/seu-usuario/consciencia-ambiental/issues)
- **Formulário de Contato**: Disponível na aplicação

---

## 🙏 Agradecimentos

- [Flask](https://flask.palletsprojects.com/) - Framework web
- [Firebase](https://firebase.google.com/) - Backend e armazenamento
- [MDN Web Docs](https://developer.mozilla.org/) - Documentação web
- Comunidade open-source

---

## 📊 Status do Projeto

- ✅ Landing Page funcional
- ✅ Autenticação completa
- ✅ Gerenciamento de campanhas
- ✅ Busca inteligente
- ✅ Formulário de contato
- 🔄 Integração com redes sociais (em desenvolvimento)
- 🔄 Mapa interativo de campanhas (planejado)

---

## 🎯 Roadmap Futuro

- [ ] Integração com redes sociais (compartilhar campanhas)
- [ ] Sistema de comentários em campanhas
- [ ] Gamificação (pontos, badges)
- [ ] Dashboard de estatísticas para admins
- [ ] App mobile (React Native)
- [ ] Chat em tempo real
- [ ] Suporte multidioma
- [ ] Newsletter por email

---

**Desenvolvido com ❤️ para um planeta mais sustentável** 🌍

_Última atualização: 28/01/2026_
