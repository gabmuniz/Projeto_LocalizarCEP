import requests

def main():
    print("---Consulta CEP---")
    cep = input("Digite o CEP: ")

    if len(cep) != 8:
        print("Quantidade de dígitos inválido")
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    address_data = request.json()

    if 'erro' not in address_data:
       
        print('CEP: {}'.format(address_data['cep']))
        print('Logradouro: {}'.format(address_data['logradouro']))
        print('Complemento: {}'.format(address_data['complemento']))
        print('Bairro: {}'.format(address_data['bairro']))
        print('Cidade: {}'.format(address_data['localidade']))
        print('Estado: {}'.format(address_data['uf']))
    else:
        print('{}: Cep inválido.'.format(cep))

    option = int(input("Nova consulta ? \n 1. Sim \n 2. Não \n"))
    if option == 1:
        main()

if __name__ == "__main__":
    main()