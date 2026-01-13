# 🚀 Visão Diária Astro RPA

Projeto de automação que coleta a Imagem Astronômica do Dia (APOD) da NASA, traduz para português e envia via WhatsApp diariamente às 20:00.

## 📋 Descrição

Sistema RPA (Robotic Process Automation) que integra a API da NASA para obter a "Astronomy Picture of the Day" (APOD), processa as informações, armazena dados e envia automaticamente via WhatsApp todos os dias.

## 📁 Estrutura do Projeto

```
visao-diaria-astro-rpa/
├── main.py                 # Execução principal
├── README.md               # Este arquivo
├── config/
│   └── settings.json       # Configurações (API key, WhatsApp)
├── model/
│   └── imagem_nasa.py      # Modelo de dados da APOD
├── services/
│   ├── nasa_api_service.py # Integração com API NASA
│   ├── image_service.py    # Download de imagens
│   ├── translation_service.py    # Tradução (Próximo)
│   └── whatsapp_service.py       # WhatsApp (Próximo)
├── repository/
│   └── image_repository.py # Persistência de dados
├── utils/
│   ├── config.py          # Carregamento de config
│   ├── logger.py          # Sistema de logging
│   └── scheduler.py       # Agendador diário (Próximo)
├── data/                   # Banco de dados
├── output/
│   ├── images/            # Imagens baixadas
│   └── reports/           # Relatórios
└── logs/                   # Logs da aplicação
```

## 🎯 Próximos Passos

- [ ] **Traduzir Título e Descrição** para Português
  - Integração com Google Translate ou API de tradução
  - Traduções automáticas de conteúdo da NASA

- [ ] **Enviar via WhatsApp** Diariamente
  - Integração com pywhatkit/Twilio
  - Envio automático de mensagens formatadas
  - Inclui imagem, título e descrição

- [ ] **Agendar Execução** para 20:00 Todos os Dias
  - Uso de APScheduler ou schedule
  - Execução automática sem intervenção manual
  - Configurável para qualquer horário

- [ ] **Persistência em Banco de Dados**
  - Migração de arquivo para SQLite/PostgreSQL
  - Histórico completo de imagens
  - Consultas e relatórios

- [ ] **Melhorias Futuras**
  - Dashboard web para visualizar histórico
  - Tratamento avançado de erros
  - Notificações de falhas por email
  - Suporte a múltiplos idiomas

## 🔧 Configuração

### Pré-requisitos

- Python 3.9+
- Conta NASA API (gratuita em https://api.nasa.gov)
  <img width="1061" height="723" alt="image" src="https://github.com/user-attachments/assets/609764ac-2174-4732-8677-a826468c2ccc" />

- Conta WhatsApp Business ou pywhatkit

### Instalação de Dependências

```bash
pip install requests python-dotenv googletrans pywhatkit schedule apscheduler
```

### Configuração do API Key da NASA

1. Acesse https://api.nasa.gov
2. Preenchaa o [formulário](https://api.nasa.gov/) para receber sua chave API , vá ate "Genarate API Key"
3. Configure em `config/settings.json`:

```json
{
  "nasa_api": {
    "base_url": "https://api.nasa.gov/planetary/apod",
    "api_key": "DEMO_KEY"
  }
}
```

## 🚀 Uso

### Execução Manual

```bash
python main.py
```

Coleta a APOD do dia, faz download da imagem e armazena.

### Com Tradução e WhatsApp (Futuro)

```bash
python main_com_traducao.py
```

Coleta, traduz para português e envia via WhatsApp.

### Agendado Diariamente (Futuro)

```bash
python utils/scheduler.py
```

Executa automaticamente todos os dias às 20:00.

## ✨ Funcionalidades Atuais

- ✅ Coleta APOD da NASA
- ✅ Download de imagens astronômicas
- ✅ Armazenamento em repositório
- ✅ Sistema de logging
- ✅ Tratamento de erros


## 📊 Fluxo de Execução (Futuro)

```
┌─────────────────────────────────────┐
│  AGENDADOR (diariamente às 20:00)  │
└──────────────┬──────────────────────┘
               │
        ┌──────▼──────┐
        │ COLETA APOD │ ← NASA API
        └──────┬──────┘
               │
        ┌──────▼─────────┐
        │  TRADUÇÃO PT   │ ← Google Translate
        └──────┬─────────┘
               │
        ┌──────▼──────────┐
        │ ARMAZENAMENTO   │ ← Repositório
        └──────┬──────────┘
               │
        ┌──────▼────────┐
        │  ENVIO WHATS   │ ← WhatsApp
        └───────────────┘
```



### A API da NASA retorna erro

- Verifique sua API Key em https://api.nasa.gov
- Verifique se o número de requisições não foi excedido (limite: 1000/hora)


## 🔗 Links Úteis

- [NASA APOD API](https://api.nasa.gov)
- [Google Translate API](https://cloud.google.com/translate)
- [pywhatkit Documentation](https://github.com/Shayneobrien/pywhatkit)
- [APScheduler Documentation](https://apscheduler.readthedocs.io/)


## 📜 Licença

MIT

## 👨‍💻 Autor

Projeto de estudo em Python - RPA & Automação

---

**Status do Projeto**: 🔄 Em Desenvolvimento

Próximos passos:
1. ✅ Estrutura base
2. ⏳ Tradução de título e descrição
3. ⏳ Integração com WhatsApp
4. ⏳ Scheduler para execução diária
5. ⏳ Banco de dados persistente
