import requests

def get_data(api_url, input_id):
    '''
        Estabelece uma conexão com a API, realiza a solicitação de dados e os converte para o formato JSON.
        Caso ocorra algum erro durante a operação, uma mensagem de erro personalizada é retornada.
    '''
    try:
        response = requests.get(f"{api_url}/{input_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados: {e}")
        return None

def categorize_age(age):
    '''
        Categoriza faixa etária. 
    '''
    if age < 30:
        return "Jovem"
    elif 30 <= age <= 40:
        return "Adulto"
    else:
        return "Sênior"

def main():
    '''
        Recebe input do usuário e chama os métodos get_data e categorize_age com esta informação.
        Organiza e escreve as informações referentes ao ID escolhido pelo usuário e a faixa etária pertencente. 
    '''
    api_url = "http://localhost:5226/"
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