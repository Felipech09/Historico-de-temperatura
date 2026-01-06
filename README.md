# 🌦️ ClimaCidade - Projeto em Python

Este é um projeto simples em **Python** utilizando **Programação Orientada a Objetos (POO)** para consultar dados de clima de cidades do Brasil.  
O programa consome a API gratuita do [OpenWeatherMap](https://openweathermap.org/api) e mostra:

- Temperatura **atual**, **máxima** e **mínima** do dia.
- Previsão da **semana** (3 dias anteriores, hoje e 3 dias seguintes), incluindo máxima, mínima e média.

---

## 🚀 Tecnologias utilizadas
- Python
- Biblioteca [requests](https://pypi.org/project/requests/) para chamadas HTTP
- API [OpenWeatherMap](https://openweathermap.org/api)

---

## 📂 Estrutura do projeto

- clima.py
- Arquivo único e principal com a classe ClimaCidade e execução do programa

---

## ▶️ Como executar?

No terminal, rode:

- python clima.py
- Digite o nome da cidade (somente cidades do Brasil).

## Saída esperada: 

=== Temperatura Atual ===
Cidade: Brasília
Atual: 27°C
Máxima: 30°C
Mínima: 22°C

=== Previsão da Semana ===
2026-01-04 -> Máx: 29°C | Mín: 21°C | Média: 25.0°C
2026-01-05 -> Máx: 30°C | Mín: 22°C | Média: 26.0°C
2026-01-06 -> Máx: 31°C | Mín: 23°C | Média: 27.0°C
