"""
Conversor de Moedas (CLI)

Consome a API pública e gratuita Frankfurter (https://frankfurter.dev/),
que não exige cadastro nem chave de API. As taxas têm como fonte o
Banco Central Europeu e são atualizadas em dias úteis.
"""

import sys
import requests

API_URL = "https://api.frankfurter.dev/v1/latest"


def obter_taxa(moeda_origem: str, moeda_destino: str) -> float:
    """Consulta a taxa de conversão entre duas moedas."""
    params = {"base": moeda_origem, "symbols": moeda_destino}
    resposta = requests.get(API_URL, params=params, timeout=10)
    resposta.raise_for_status()
    dados = resposta.json()

    if moeda_destino not in dados.get("rates", {}):
        raise ValueError(f"Moeda de destino inválida: {moeda_destino}")

    return dados["rates"][moeda_destino]


def converter(valor: float, moeda_origem: str, moeda_destino: str) -> tuple[float, float]:
    """Converte um valor de uma moeda para outra. Retorna (resultado, taxa)."""
    taxa = obter_taxa(moeda_origem, moeda_destino)
    return valor * taxa, taxa


def ler_valor(prompt: str) -> float:
    texto = input(prompt).strip().replace(",", ".")
    return float(texto)


def main() -> None:
    print("=== Conversor de Moedas ===")
    print("(códigos ISO, ex: USD, BRL, EUR, GBP, JPY)\n")

    try:
        valor = ler_valor("Valor a converter: ")
        origem = input("Moeda de origem: ").strip().upper()
        destino = input("Moeda de destino: ").strip().upper()

        resultado, taxa = converter(valor, origem, destino)
        print(f"\n{valor:.2f} {origem} = {resultado:.2f} {destino}")
        print(f"(taxa: 1 {origem} = {taxa:.4f} {destino})")

    except ValueError as erro:
        print(f"\nEntrada inválida: {erro}")
        sys.exit(1)
    except requests.RequestException as erro:
        print(f"\nErro ao consultar a API: {erro}")
        sys.exit(1)


if __name__ == "__main__":
    main()
