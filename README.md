# Conversor de Moedas (Python)

Conversor de moedas simples via linha de comando. Consome a API pública e
gratuita [Frankfurter](https://frankfurter.dev/) — sem cadastro e sem chave
de API.

## Como usar

```bash
pip install -r requirements.txt
python main.py
```

Informe o valor e os códigos ISO das moedas de origem e destino (ex: `USD`,
`BRL`, `EUR`, `GBP`, `JPY`).

### Exemplo

```
=== Conversor de Moedas ===
(códigos ISO, ex: USD, BRL, EUR, GBP, JPY)

Valor a converter: 100
Moeda de origem: USD
Moeda de destino: BRL

100.00 USD = 542.30 BRL
(taxa: 1 USD = 5.4230 BRL)
```

## Limitações

- A API do Frankfurter cobre um conjunto menor de moedas que provedores
  pagos (não inclui criptomoedas, por exemplo).
- As taxas são atualizadas em dias úteis, não em tempo real.

## Próximos passos

- Interface gráfica
- Histórico de conversões salvo localmente
