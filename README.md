# Bot Discord Modular

Este projeto foi desenvolvido por mim, Luis Miguel Perinotte, com o objetivo de aprendizado em Python, APIs e desenvolvimento de bots para Discord. O código está público para fins de portfólio, estudo e inspiração para outros desenvolvedores.

## Sobre o Projeto
Este bot utiliza arquitetura modular baseada em cogs, facilitando manutenção, extensão e organização do código. Ele integra diversas APIs externas e registra logs de uso dos comandos.

## Funcionalidades
- Comandos de usuário organizados em cogs
- Listeners de eventos
- Integração com APIs externas (clima, tradução, Wikipedia, IA)
- Logs diários de uso de comandos

## Estrutura do Projeto
```
cogs_loader.py           # Função para carregar cogs
logs_generator.py        # Gerenciamento de logs
main.py                  # Ponto de entrada do bot
requirements.txt         # Dependências Python
cogs/
  commands/              # Cogs de comandos
  events/                # Cogs de eventos
logs/                    # Logs diários
```

## Como executar
1. **Crie e ative o ambiente virtual (Se for usar o pip):**
   - Windows: `discord_bot\Scripts\activate`
   - **Se for instalar as dependências com uv, não é necessário criar ambiente virtual.**
   
2. **Instale as dependências:**
   - Usando uv (recomendado, mais rápido e seguro):
     ```sh
     uv sync
     ```
   - Se quiser usar o pip tradicional:
     ```sh
     uv export --without-hashes > requirements.txt
     pip install -r requirements.txt
     ```
3. **Configure as chaves de API:**
   - Crie um arquivo `.env` na raiz e adicione:
   ```
   DISCORD_KEY=seu_token_aqui
   HGWEATHER_API_KEY=sua_key_weather
   OPENROUTER_API_KEY=sua_key_ia
   ```
4. **Execute o bot:**
   ```sh
   uv run main.py
   ```

## Como adicionar comandos/eventos
- Crie um novo arquivo cog em `cogs/commands/` ou `cogs/events/`
- Implemente uma classe herdando de `commands.Cog`
- Adicione o caminho do cog na lista de `cogs_loader.py`

## Comandos Disponíveis

**Comandos Gerais**
- `/info` — Exibe informações do servidor atual.
- `/ping` — Mostra a latência do bot.

**Diversão**
- `/ascii` — Gera arte ASCII com o texto e fonte escolhidos.

**APIs**
- `/weather` — Mostra o tempo em uma cidade do Brasil.
- `/translator` — Traduz seu texto para o idioma desejado.
- `/wikipedia` — Pesquisa rápida na Wikipedia sobre um assunto.

**Inteligência Artificial**
- `/ia` — Converse com a IA Sage (nome dado ao bot).
- `/gen` — Gere imagens usando IA.

## Logs
- O uso de comandos é registrado em arquivos diários na pasta `logs/`
- O formato e a escrita dos logs são gerenciados por `logs_generator.py`
- Para receber logs no Discord via webhook, adicione a variável `WEBHOOK_DISCORD_LOG` com a URL do seu webhook no arquivo `.env`:
  ```
  WEBHOOK_DISCORD_LOG=https://discord.com/api/webhooks/...
  ```

## Dependências principais
- `discord.py`
- `python-dotenv`
- `colorama`
- `requests`
- `langdetect`
- `pyfiglet`


Este projeto é aberto para consulta, aprendizado e inspiração. Sinta-se livre para abrir issues, sugerir melhorias ou tirar dúvidas. Se quiser usar parte do código, cite o autor e entre em contato!
