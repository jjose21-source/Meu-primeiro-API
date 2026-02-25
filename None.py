import requests

cep = 86900000

response = requests.get(f"https://viacep.com.br/ws/{cep}/json")
