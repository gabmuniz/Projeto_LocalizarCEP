# Importamos a biblioteca:
import pymysql
import requests

# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='localizarcep', user='root', passwd='Start@2020')

# Cria um cursor:
cursor = conexao.cursor()

#cursor.execute("INSERT INTO localizar_cep VALUES (3, 'Raphael', 06150350, 'Estrada das Rosas', '', 'Santa Maria', 'Osasco', 'SP')")

#cursor.execute("UPDATE localizar_cep SET complemento = ('blocoD') WHERE id = 2")

conexao.commit()



op = 0
while op < 6:
    print("""PROJETO LocalizarCEP
    [1] - Criação da linha de uma tabela
    [2] - Leitura de endereços
    [3] - Leitura de dados cliente
    [4] - Atualização do banco de dados
    [5] - Deletando uma linha de uma tabela
    [6] - SAIR
    """)
    op = int(input("Escolha uma opção: "))
    if op == 1:

            print("---Consulta CEP---")
            cep = input("Digite o CEP: ")

            if len(cep) != 8:
                print("Quantidade de dígitos inválido")
                exit()

            request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

            address_data = request.json()

            if 'erro' not in address_data:
        
                #idteste = int(input("Digite seu id: "))
                cep = (address_data['cep'])
                logradouro = (address_data['logradouro'])
                complemento = (address_data['complemento'])
                bairro = (address_data['bairro'])
                cidade = (address_data['localidade'])
                estado = (address_data['uf'])
                myslq = "INSERT INTO localizar_cep VALUES (%s, %s, %s, %s, %s, %s)"
                myval = (cep, logradouro, complemento, bairro, cidade, estado)
                cursor.execute(myslq, myval)
                conexao.commit()

    elif op == 2:
        consulta_sql = "select * from localizar_cep"
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        print("_" * 50, "\n")
        print("\nSeus Dados: \n")
        for linha in linhas:
            print("CEP:", linha[0])
            print("Logradouro:", linha[1])
            print("Complemento:", linha[2])
            print("Bairro:", linha[3])
            print("Cidade:", linha[4])
            print("Estado:", linha[5], "\n")
            print("_" * 50, "\n")
    elif op == 3:
        consulta_sql = "select * from dados_cliente"
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        print("_" * 50, "\n")
        print("\nSeus Dados: \n")
        for linha in linhas:
            print("Nome:", linha[0])
            print("Telefone:", linha[1])
            print("CPF:", linha[2], "\n")
            print("_" * 50, "\n")
    elif op == 4:
        consulta_sql = ("select * from localizar_cep")
        update_linhasql = ("update localizar_cep set complemento = ('apto 22 bloco D') WHERE cidade = ('Osasco')")
        cursor.execute(update_linhasql)
        cursor.execute(consulta_sql)
        conexao.commit()
        print("linha atualizada com sucesso.")
        linhas = cursor.fetchall()

        print("_" * 50, "\n")
        print("\nSeus Dados: \n")
        for linha in linhas:
            print("CEP:", linha[0])
            print("Logradouro:", linha[1])
            print("Complemento:", linha[2])
            print("Bairro:", linha[3])
            print("Cidade:", linha[4])
            print("Estado:", linha[5], "\n")
            print("_" * 50, "\n")
    elif op == 5:
        consulta_sql = "select * from localizar_cep"
        delete_linhasql = "delete from localizar_cep where cidade = ('Osasco')"
        cursor.execute(delete_linhasql)
        cursor.execute(consulta_sql)
        conexao.commit()
        print("linha excluida com sucesso.")

        linhas = cursor.fetchall()

        print("_" * 50, "\n")
        print("\nSeus Dados: \n")
        for linha in linhas:
            print("CEP:", linha[0])
            print("Logradouro:", linha[1])
            print("Complemento:", linha[2])
            print("Bairro:", linha[3])
            print("Cidade:", linha[4])
            print("Estado:", linha[5], "\n")
            print("_" * 50, "\n")

conexao.close()

"""

#leitura do Banco de Dados

consulta_sql = "select * from localizar_cep"
cursor.execute(consulta_sql)
linhas = cursor.fetchall()

print("_" * 50, "\n")
print("\nEndereços Localizados: \n")
for linha in linhas:
    print("CEP:", linha[0])
    print("Logradouro:", linha[1])
    print("Complemento:", linha[2])
    print("Bairro:", linha[3])
    print("Cidade:", linha[4])
    print("Estado:", linha[5], "\n")
    print("_" * 50, "\n")

#Deletando uma linha

delete_linhasql = "delete from localizar_cep where cidade = ('Osasco')"
cursor.execute(delete_linhasql)
conexao.commit()
print("linha excluida com sucesso.")

#Atualizando uma linha

update_linhasql = ("update localizar_cep set complemento = ('apto 22 bloco D') WHERE cidade = ('Osasco')")
cursor.execute(update_linhasql)
conexao.commit()
print("linha atualizada com sucesso.")



#Criptografando um campo

AES_ENCRYPT = ("UPDATE dados_cliente SET cpf = AES_ENCRYPT(cpf,'superman')")
AES_SELECT = ("SELECT * FROM dados_cliente")
cursor.execute(AES_ENCRYPT)
cursor.execute(AES_SELECT)
conexao.commit()
print("campo criptografado com sucesso.")
linhas = cursor.fetchall()

print("_" * 50, "\n")
for linha in linhas:
    print("nome:", linha[0])
    print("telefone:", linha[1])
    print("cpf:", linha[2])
    print("_" * 50, "\n")



#Descriptografando um campo

AES_DECRYPT = ("SELECT CAST(AES_DECRYPT(cpf,'superman') AS char(255)) FROM dados_cliente")
cursor.execute(AES_DECRYPT)
conexao.commit()
print("campo descriptografado com sucesso.")
linhas = cursor.fetchall()

print("_" * 50, "\n")
for linha in linhas:
    print("cpf:", linha[0])
    print("_" * 50, "\n")

"""