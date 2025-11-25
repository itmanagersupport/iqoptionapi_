# README - Documentação da API IQ Option


<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUTW6k88_IRCwenPq8FiDJipg8ILuiqRveNg&s" alt="Logo IQ Option API" width="200">
</p>

Este arquivo contém a documentação dos métodos disponíveis na classe `IQ Option` e exemplos de como utilizá-los.

## Classe Principal
A classe principal para interagir com a API da IQ Option é a `IQ Option`.

---

## Inicialização
Para começar, inicialize a classe `IQ_Option` com seu e-mail e senha:

```python
from iqoptionapi.stable_api import IQ_Option

email = "seu_email@example.com"
senha = "sua_senha"
api = IQ_Option(email, senha)
```

---

## Métodos Disponíveis

### 1. Conexão e Sessão
- **`connect(sms_code=None)`**  
  Conecta à API. Retorna `(True, None)` em caso de sucesso ou `(False, mensagem)` em caso de falha.

- **`connect_2fa(sms_code)`**  
  Conecta utilizando autenticação de dois fatores (2FA).

- **`check_connect()`**  
  Verifica se a conexão está ativa. Retorna `True` ou `False`.

- **`set_session(header, cookie)`**  
  Define cabeçalhos e cookies para a sessão.

#### Exemplo:
```python
status, message = api.connect()
if status:
    print("Conectado com sucesso!")
else:
    print(f"Erro na conexão: {message}")
```

---

### 2. Informações da Conta
- **`get_balance()`**  
  Retorna o saldo da conta ativa.

- **`get_balance_mode()`**  
  Retorna o tipo de conta ativa (`REAL`, `PRACTICE`, `TOURNAMENT`).

- **`get_currency()`**  
  Retorna a moeda da conta ativa.

- **`change_balance(Balance_MODE)`**  
  Altera o tipo de conta ativa (`REAL`, `PRACTICE`, `TOURNAMENT`).

- **`reset_practice_balance()`**  
  Reseta o saldo da conta prática.

#### Exemplo:
```python
api.change_balance("PRACTICE")
print("Saldo:", api.get_balance())
print("Tipo de conta:", api.get_balance_mode())
```

---

### 3. Ativos e Instrumentos
- **`update_ACTIVES_OPCODE()`**  
  Atualiza os códigos dos ativos disponíveis.

- **`get_all_ACTIVES_OPCODE()`**  
  Retorna todos os ativos disponíveis.

- **`get_instruments(type)`**  
  Retorna instrumentos disponíveis para um tipo específico (`crypto`, `forex`, `cfd`).

- **`get_name_by_activeId(activeId)`**  
  Retorna o nome do ativo pelo ID.

#### Exemplo:
```python
api.update_ACTIVES_OPCODE()
ativos = api.get_all_ACTIVES_OPCODE()
print("Ativos disponíveis:", ativos)
```

---

### 4. Operações Binárias
- **`buy(price, ACTIVES, ACTION, expirations)`**  
  Executa uma operação binária.
  - `price`: Valor da operação.
  - `ACTIVES`: Nome do ativo.
  - `ACTION`: Direção (`"call"` ou `"put"`).
  - `expirations`: Tempo de expiração em minutos.

- **`check_win_v4(order_id)`**  
  Verifica o resultado de uma operação binária.

#### Exemplo:
```python
status, order_id = api.buy(1, "EURUSD", "call", 1)
if status:
    print("Ordem executada com sucesso!")
    result = api.check_win_v4(order_id)
    print("Resultado:", result)
```

---

### 5. Operações Digitais
- **`buy_digital_spot_v2(active, amount, action, duration)`**  
  Executa uma operação digital.
  - `active`: Nome do ativo.
  - `amount`: Valor da operação.
  - `action`: Direção (`"call"` ou `"put"`).
  - `duration`: Duração em minutos (1, 5, 15).

- **`check_win_digital_v2(order_id)`**  
  Verifica se a ordem digital fechou e retorna o lucro.
  Nota: Requer um loop de verificação (polling).

- **`close_digital_option(order_id)`**
  Vende a ordem digital antecipadamente.

#### Exemplo:
```python
import time

status, order_id = api.buy_digital_spot_v2("EURUSD", 10, "put", 5)

if status:
    print("Ordem Digital executada:", order_id)
    while True:
        status_win, lucro = api.check_win_digital_v2(order_id)
        if status_win:
            print("Resultado Digital:", lucro)
            break
        time.sleep(1)
```

---

### 6. Operações Blitz
- **`buy_blitz(active, price, direction, expiration)`**
  Executa operações rápidas (Blitz).

- **`expiration`**
  Tempo em segundos (ex: 5, 10, 30).

- **`get_blitz_payout(active)`**
  Retorna o payout atual para blitz.

#### Exemplo:
```python
status, order_id = api.buy_blitz("EURUSD", 5, "call", 30) # 30 segundos
if status:
    print("Blitz iniciada!")
    print(api.check_win_v4(order_id)) # Usa o mesmo check das binárias
```

---

### 7. Histórico e Velas
- **`get_candles(ACTIVES, interval, count, endtime)`**  
  Retorna o histórico de candles.
  - `ACTIVES`: Nome do ativo.
  - `interval`: Intervalo em segundos (ex.: `60` para 1 minuto).
  - `count`: Número de candles.
  - `endtime`: Timestamp final.

- **`start_candles_stream(ACTIVE, size, maxdict)`**  
  Inicia o stream de candles em tempo real.

- **`stop_candles_stream(ACTIVE, size)`**  
  Para o stream de candles.

#### Exemplo:
```python
candles = api.get_candles("EURUSD", 60, 10, int(time.time()))
for candle in candles:
    print(candle)
```

---

### 8. Ferramentas de Análise
- **`get_technical_indicators(ACTIVES)`**
  Retorna dados de indicadores técnicos (Médias Móveis, RSI, Bollinger, etc) calculados pela corretora.

- **`get_traders_mood(ACTIVES)`**
  Retorna o sentimento dos traders (porcentagem de compra vs venda).

#### Exemplo:
```python
indicadores = api.get_technical_indicators("EURUSD")
print(indicadores)

sentimento = api.get_traders_mood("EURUSD")
print(f"Sentimento de Mercado: {sentimento}")
```

---

### 9. Outros Métodos
- **`get_digital_payout(active, seconds=0)`**  
  Retorna o payout digital para um ativo.

- **`get_position_history(instrument_type)`**  
  Retorna o histórico de posições.

- **`logout()`**  
  Encerra a sessão.

---

## Notas
- Certifique-se de que a conexão está ativa antes de executar qualquer operação.
- Ativos OTC: Para operar em OTC, adicione "-OTC" ao nome do ativo (ex: "EURUSD-OTC").
- Ativos OP: Para operar adicione "-op" ao nome do ativo (ex: "EURUSD-op").
- Delay: Sempre utilize time.sleep em loops de verificação para evitar sobrecarga e desconexão da API.
- Tratamento de Erros: Use blocos try-except ao fazer chamadas de rede para garantir estabilidade.
