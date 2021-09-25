# Importamos a biblioteca:
import pymysql
import requests
from PyQt5 import uic,QtWidgets
# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='localizarcep', user='root', passwd='12344321')

# Cria um cursor:
cursor = conexao.cursor()

#cursor.execute("INSERT INTO localizar_cep VALUES (3, 'Raphael', 06150350, 'Estrada das Rosas', '', 'Santa Maria', 'Osasco', 'SP')")

#cursor.execute("UPDATE localizar_cep SET complemento = ('blocoD') WHERE id = 2")

conexao.commit()

#def funcao_principal():
    #DesignNome = Design.lineEdit.text()
    #DesignTelefone = Design.lineEdit_2.text()
    #DesignCPF = Design.lineEdit_3.text()
    #DesignCEP = Design.lineEdit_4.text()

op = 0
while op < 5:
    print("""PROJETO LocalizarCEP
    [1] - Consultar ENDEREÇO
    [2] - Consultar DADOS DO CLIENTE
    [3] - Descriptografar CPF
    [4] - Cadastrar DADOS DO CLIENTE E ENDEREÇO
    [5] - SAIR
    """)
    op = int(input("Escolha uma opção: "))
    if op == 1:
        consulta_sql = "select * from localizar_cep"
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        print("_" * 50, "\n")
        print("\nSeus Endereços: \n")
        for linha in linhas:
            print("CEP:", linha[0])
            print("Logradouro:", linha[1])
            print("Complemento:", linha[2])
            print("Bairro:", linha[3])
            print("Cidade:", linha[4])
            print("Estado:", linha[5], "\n")
            print("_" * 50, "\n")
    elif op == 2:
        consulta_sql = "select * from dados_cliente"
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        print("_" * 50, "\n")
        print("\nSeus Dados: \n")
        for linha in linhas:
            print("nome:", linha[0])
            print("telefone:", linha[1])
            print("cpf:", linha[2], "\n")
            print("_" * 50, "\n")    
    elif op == 3:
        AES_DECRYPT = ("SELECT CAST(AES_DECRYPT(cpf,'superman') AS char) FROM dados_cliente")
        cursor.execute(AES_DECRYPT)
        conexao.commit()
        print("cpf descriptografado com sucesso.")
        linhas = cursor.fetchall()
        print("_" * 50, "\n")
        for linha in linhas:
            print("cpf:", linha[0])
            print("_" * 50, "\n")
    elif op == 4:
        def funcao_principal():
            DesignNome = Design.lineEdit.text()
            DesignTelefone = Design.lineEdit_2.text()
            DesignCPF = Design.lineEdit_3.text()
            DesignCEP = Design.lineEdit_4.text()
            sql = "INSERT INTO dados_cliente VALUES (%s, %s, %s)"
            val = (DesignNome, DesignTelefone, DesignCPF)
            cursor.execute(sql, val)
            conexao.commit()
            #elif op == 5:
            request = requests.get('https://viacep.com.br/ws/{}/json/'.format(DesignCEP))

            address_data = request.json()

            if 'erro' not in address_data:
                #idteste = int(input("Digite seu id: "))
                DesignCEP = (address_data['cep'])
                logradouro = (address_data['logradouro'])
                complemento = (address_data['complemento'])
                bairro = (address_data['bairro'])
                cidade = (address_data['localidade'])
                estado = (address_data['uf'])
                myslq = "INSERT INTO localizar_cep VALUES (%s, %s, %s, %s, %s, %s)"
                myval = (DesignCEP, logradouro, complemento, bairro, cidade, estado)
                cursor.execute(myslq, myval)
                conexao.commit()

        app=QtWidgets.QApplication([])
        Design=uic.loadUi("Design.ui")
        Design.pushButton.clicked.connect(funcao_principal)

        Design.show()
        app.exec()
conexao.close()
