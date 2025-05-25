<p align="center">

  <!-- Linguagem principal -->
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  </a>

  <!-- Framework Web -->
  <a href="https://flask.palletsprojects.com/">
    <img src="https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask" />
  </a>

  <!-- APIs Meteorológicas -->
  <a href="https://content.meteoblue.com/en/access/weather-apis">
    <img src="https://img.shields.io/badge/-Meteoblue-0082C8?style=flat-square&logo=cloud&logoColor=white" alt="Meteoblue API" />
  </a>
  <a href="https://openweathermap.org/api">
    <img src="https://img.shields.io/badge/-OpenWeatherMap-EA7600?style=flat-square&logo=openweathermap&logoColor=white" alt="OpenWeatherMap" />
  </a>

  <!-- Manipulação e Requisições HTTP -->
  <a href="https://pypi.org/project/python-dotenv/">
    <img src="https://img.shields.io/badge/-Dotenv-ECD53F?style=flat-square&logo=python&logoColor=black" alt="Dotenv" />
  </a>
  <a href="https://requests.readthedocs.io/">
    <img src="https://img.shields.io/badge/-Requests-20232A?style=flat-square&logo=python&logoColor=white" alt="Requests" />
  </a>

  <!-- Testes -->
  <a href="https://docs.pytest.org/">
    <img src="https://img.shields.io/badge/-Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white" alt="Pytest" />
  </a>

  <!-- Containerização -->
  <a href="https://www.docker.com/">
    <img src="https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
  </a>
  <a href="https://docs.docker.com/compose/">
    <img src="https://img.shields.io/badge/-Docker%20Compose-3855D6?style=flat-square&logo=docker&logoColor=white" alt="Docker Compose" />
  </a>

  <!-- Licença e Status -->
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square" alt="Status: Em desenvolvimento" />
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT License" />

</p>

![logoClimaBlue](https://github.com/user-attachments/assets/f5712693-cb8c-417c-9dbe-69cd93aee1c7)

# 🌤️ 🌾 Previsão Meteorológica Inteligente: Sistema de Visualização de Meteogramas Focado no Agronegócio
A meteorologia sempre foi uma aliada estratégica do agronegócio. Seja no planejamento de safras, no manejo de irrigação ou na prevenção de perdas por eventos extremos, o conhecimento antecipado das condições climáticas é vital. Pensando nisso, desenvolvi uma aplicação web focada na visualização de meteogramas – gráficos detalhados que mostram a previsão do tempo de forma visual e intuitiva – com integração à API da Meteoblue, uma das mais confiáveis do mundo.

🌾 Impacto para o Agronegócio
O Brasil é uma potência agrícola, mas também um país vulnerável a eventos climáticos severos, como: Geadas no Sul, Longos períodos de seca no Centro-Oeste, Chuvas excessivas na Região Norte e Nordeste.

Aplicação web desenvolvida em Flask para visualização interativa de meteogramas a partir da API Meteoblue. Suporte a diversos tipos de meteogramas e seleção dinâmica de capitais brasileiras.

---

## 📌 Descrição
Esta aplicação permite ao usuário escolher um **estado brasileiro**; automaticamente, ela identifica as coordenadas da capital correspondente e gera diferentes tipos de meteogramas usando a API Meteoblue. Com uma interface moderna, amigável e responsiva, construída com Bootstrap 5, proporciona uma experiência intuitiva. O backend em Flask gera URLs personalizadas dos meteogramas, com parâmetros ajustáveis, incluindo o idioma em português. (Assista ao vídeo 

---

## ⚙️ Funcionalidades
- 🗺️ Seleção dinâmica de estado brasileiro com preenchimento automático de latitude e longitude.
- 🌡️ Escolha entre diversos tipos de meteogramas suportados pela API Meteoblue.
- 🚩 Suporte opcional para altitude, aumentando a precisão dos meteogramas.
- 📊 Visualização direta e interativa do meteograma na página.
- 🚫 Tratamento e exibição de erros em tempo real.
- 📱 Interface responsiva com Bootstrap 5.
- 🐍 Backend em Python com Flask.
- 🇧🇷 Suporte ao idioma português nos meteogramas.

## 🧪 Exemplo de Uso
https://github.com/user-attachments/assets/6a80e69e-80a0-4a28-b001-b59b6309f86f

---

## 💻 Tecnologias Utilizadas
- Python 3.x
- Flask
- Jinja2
- Bootstrap 5
- API Meteoblue

---

## 🌍 Fontes de Dados
| Fonte | Descrição | Frequência |
|-------|------------|--------------|
| [Meteoblue](https://www.meteoblue.com/) | Dados meteorológicos | Horária |

---

## 🗂️ Estrutura do Projeto
```bash  
project_root/  
│  
├── app/  
│   ├── __init__.py                 # Inicializa a aplicação Flask  
│   ├── config.py                   # Configurações (ex: API keys, env vars)  
│   ├── routes.py                   # Rotas Flask (endpoints e páginas)  
│   ├── services/  
│   │   ├── __init__.py  
│   │   └── meteogram_generator.py # Geração das URLs dos meteogramas  
│   ├── templates/  
│   │   └── index.html              # Página principal (template Jinja2)  
│   ├── static/                     # Arquivos estáticos (CSS, JS, imagens)  
│   └── utils/  
│       └── __init__.py             # Funções auxiliares (se necessário)  
│  
├── tests/  
│   └── test_meteogram_generator.py # Testes unitários  
│  
├── requirements.txt               # Dependências do Python  
├── run.py                         # Script para rodar a aplicação  
├── .env                           # Variáveis de ambiente (API key, configs)  
└── README.md                      # Documentação do projeto  
```

## 🚀 Como começar
## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/LeviLucena/ClimaBlue_Brasil.git
cd ClimaBlue_Brasil
```

2. Crie e ative um ambiente virtual (recomendado):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure sua API Key
No arquivo .env na raiz do projeto, inclua sua chave da API Meteoblue:
```bash
METEOBLUE_API_KEY=SUA_CHAVE_API_AQUI
```

5. Rode a aplicação
Para rodar a aplicação localmente:
```bash
python run.py
```
Acesse no navegador em: http://127.0.0.1:5000.

## 🤝 Contribuições
Sinta-se à vontade para contribuir, sugerir melhorias ou relatar problemas para ajudar a desenvolver este projeto.

## 📄 Licença
Este projeto está licenciado sob a licença MIT — veja [LICENSE](https://github.com/github/gitignore/blob/main/LICENSE) para detalhes.
