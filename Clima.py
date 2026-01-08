import requests

class ClimaCidade:
    def __init__(self, cidade, api_key):
        self.cidade = cidade
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/"

    def obter_temperatura_atual(self):
        url = (
            f"{self.base_url}weather?q={self.cidade},BR"
            f"&appid={self.api_key}&units=metric&lang=pt_br"
        )
        resposta = requests.get(url)
        dados = resposta.json()

        if resposta.status_code != 200:
            return {"erro": dados.get("message", "Não foi possível obter dados")}

        return {
    "cidade": self.cidade,
    "temperatura_atual": round(dados["main"]["temp"]),
    "maxima": round(dados["main"]["temp_max"]),
    "minima": round(dados["main"]["temp_min"])
}

    def obter_previsao_semana(self):
        """
        Retorna previsão diária baseada nos dados disponíveis (até 5 dias)
        """
        url = (
            f"{self.base_url}forecast?q={self.cidade},BR"
            f"&appid={self.api_key}&units=metric&lang=pt_br"
        )
        resposta = requests.get(url)
        dados = resposta.json()

        if resposta.status_code != 200:
            return {"erro": dados.get("message", "Não foi possível obter dados")}

        previsoes = []
        lista = dados["list"]

        # Cada 8 registros ≈ 1 dia
        dias_disponiveis = len(lista) // 8

        for i in range(dias_disponiveis):
            indice = i * 8
            dia = lista[indice]

            data = dia["dt_txt"].split(" ")[0]
            temp_max = round(dia["main"]["temp_max"])
            temp_min = round(dia["main"]["temp_min"])
            media = round((temp_max + temp_min) / 2)

            previsoes.append({
                "data": data,
                "maxima": temp_max,
                "minima": temp_min,
                "media": media
            })

        return previsoes

if __name__ == "__main__":
    api_key = "COLAR-SUA-KEY-AQUI" # para que não ocorra problemas, vou deixar assim e sempre atualize a chave quando for usar
    cidade = input("Digite o nome de uma cidade brasileira: ")

    clima = ClimaCidade(cidade, api_key)

    # Temperatura atual
    atual = clima.obter_temperatura_atual()

    if "erro" in atual:
        print("Erro:", atual["erro"])
    else:
        print("\n=== Temperatura Atual ===")
        print(f"Cidade: {atual['cidade']}")
        print(f"Atual: {atual['temperatura_atual']}°C")
        print(f"Máxima: {atual['maxima']}°C")
        print(f"Mínima: {atual['minima']}°C")

    # Previsão da semana
    semana = clima.obter_previsao_semana()

    if isinstance(semana, dict) and "erro" in semana:
        print("Erro:", semana["erro"])
    else:
        print("\n=== Previsão da Semana ===")
        for dia in semana:
            print(
                f"{dia['data']} -> "
                f"Máx: {dia['maxima']}°C | "
                f"Mín: {dia['minima']}°C | "
                f"Média: {dia['media']:.1f}°C"
            )
