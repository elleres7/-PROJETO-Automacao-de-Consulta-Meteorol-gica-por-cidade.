import requests

# Chave alterada por segurança

chave = "77bf985c"
url = "https://api.hgbrasil.com/weather"

print("\n:: CLIMA HOJE ::\n")

local = input("Digite a cidade: ")
pedido = f"{url}?key={chave}&city_name={local}"
resposta = requests.get(pedido)

if resposta.status_code == 200:
    dado = resposta.json()
    temp = dado['results']['temp']
    clima = dado['results']['description'].lower()
    cidade = dado['results']['city']
        
    print(f"\nPrevisão de agora: {temp}°C ({clima}) - {cidade}.\n")
else:
    print("Erro na leitura!")