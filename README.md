# Bot Discord Modular

Este projeto é um bot para Discord escrito em Python, com arquitetura modular baseada em cogs para facilitar manutenção, extensão e organização.

## Funcionalidades
- Comandos de usuário organizados em cogs
- Listeners de eventos
- Integração com APIs externas
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
1. **Crie e ative o ambiente virtual:**
   - Windows: `discord_bot\Scripts\activate`
2. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure a chave do Discord:**
   - Crie um arquivo `.env` na raiz e adicione:
     ```
     DISCORD_KEY=seu_token_aqui
     ```
4. **Execute o bot:**
   ```sh
   python main.py
   ```

## Como adicionar comandos/eventos
- Crie um novo arquivo cog em `cogs/commands/` ou `cogs/events/`
- Implemente uma classe herdando de `commands.Cog`
- Adicione o caminho do cog na lista de `cogs_loader.py`

## Logs
- O uso de comandos é registrado em arquivos diários na pasta `logs/`
- O formato e a escrita dos logs são gerenciados por `logs_generator.py`

## Dependências principais
- `discord.py`
- `python-dotenv`
- `colorama`

## Observações
- Não há suíte de testes automatizados; recomenda-se testar comandos manualmente via Discord.
- O projeto segue o padrão de não utilizar estado global, mantendo tudo encapsulado nos cogs ou via contexto do bot.

---

Sinta-se livre para abrir issues ou contribuir com novos comandos e melhorias!
