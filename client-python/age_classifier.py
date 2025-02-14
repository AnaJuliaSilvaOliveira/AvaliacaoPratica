import requests

def get_data(api_url, input_id):
    try:
        response = requests.get(f"{api_url}/{input_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados: {e}")
        return None

def categorize_age(age):
    if age < 30:
        return "Jovem"
    elif 30 <= age <= 40:
        return "Adulto"
    else:
        return "Sênior"

def main():
    api_url = "http://localhost:5000/api/dados"  # Substitua pelo URL real da API
    input_id = input("Digite o ID de interesse: ")
    
    data = get_data(api_url, input_id)
    
    if data:
        age_category = categorize_age(data.get("idade", 0))
        print(f"\n=== Dados Referentes ao Id {data.get('Id')} ===")
        print(f"ID: {data.get('Id')}")
        print(f"Nome: {data.get('Nome')}")
        print(f"Idade: {data.get('Idade')} ({age_category})")
        print(f"Cidade: {data.get('Cidade')}")
        print(f"Profissão: {data.get('Profissao')}")
    else:
        print("Registro não encontrado.")

if __name__ == "__main__":
    main()