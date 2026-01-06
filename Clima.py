import requests

class ClimaCidade:
  def __init__(self, cidade, api_key):
    fel.cidade = cidade
    self.api_key = api_key
    self.base_url = "http://api.openweathermap.org/data/2.5/"

def obter_temperatura_atual(self):
""" Temperatura atual, mínima e média do dia ficam aqui"""
  url = f"{self.base_url}weather?q={self.cidade},BR&appid={self.api_key}&units=metric&lang=pt_br"
  resposta = requests.get(url)
  dados = resposta.json()

  if resposta.status_code != 200:
    return f"Erro: {dados.get('message', 'Não foi possível obter dados')}"

temp_atual = dados["main"]["temp"]
temp_max = dados["main"]["temp_max"]
temp_min = dados["main"]["temp_min"]

return {
  "cidade": self.cidade,
  "temperatura_atual": temp_atual,
  "máxima": temp_max,
  "mínima": temp_min
}

def obter_previsao_semana(self): 
  """Retorna previsão para 7 dias (3 antes, hoje e 3 depois)""" 
  url = f"{self.base_url}forecast?q={self.cidade},BR&appid={self.api_key}&units=metric&lang=pt_br" 
  resposta = requests.get(url) 
  dados = resposta.json() 
  
  if resposta.status_code != 200: 
    return f"Erro: {dados.get('message', 'Não foi possível obter dados')}" 
    
  previsoes = []

for i in range(0, 7):
  indice = i * 8
  dia = dados["list"][indice]
  data = dia["dt_txt"].split(" ")[0]
  temp_max = dia["main"]["temp-max"]
  temp_min = dia["main"]["temp-min"]
  media = (temp_max + temp_min) / 2
  previsoes.append({
    "data": data,
    "maxima": temp_max,
    "minima": temp_min,
    "media": media
  })

return previsoes

if __name__ == "__main__":
  api_key = "950d6b72782852edbfa626099e804275"
  cidade = input cidade = input("Digite o nome de uma cidade brasileira: ")
  clima = ClimaCidade(cidade, api_key)

# Temperatura atual
atual = clima.obter_temperatura_atual()
print("\n=== Temperatura Atual ===")
print(f"Cidade: {atual['cidade']}")
print(f"Atual: {atual['temperatura_atual']}°C")
print(f"Máxima: {atual['maxima']}°C")
print(f"Mínima: {atual['minima']}°C")

# previsão da semana
semana = clima.obter_previsao_semana()
print("\n=== Previsão da Semana ===")
for dia in semana:
    print(f"{dia['data']} -> Máx: {dia['maxima']}°C | Mín: {dia['minima']}°C | Média: {dia['media']:.1f}°C")
