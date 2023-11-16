import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",  # Substitua por seu host, se necessário
        user="root",  # Substitua por seu username
        password="1234",  # Substitua por sua senha
        database="ProjetoIPO"  # Substitua pelo nome do seu banco de dados
    )
    cursor = connection.cursor()
    return connection, cursor


connection, cursor = create_connection()

class Veiculo():
    def __init__(self):
        self.placa = None
        self.marca = None
        self.modelo = None
        self.alocado = None
        self.cnh_requirida = None
        self.tipo_combustivel = None
        self.km = None
        self.quantidade_combustivel = None
        self.capacidade_tanque = None

class Carro(Veiculo):
    def __init__(self):
        super().__init__()
        self.tipo_combustivel = 'Gasolina'
        self.cnh_requirida = 'B'
        self.capacidade_tanque = 50


class Moto(Veiculo):
    def __init__(self):
        super().__init__()
        self.tipo_combustivel = 'Gasolina'
        self.cnh_requirida = 'A'
        self.capacidade_tanque = 12

class Caminhao(Veiculo):
    def __init__(self):
        super().__init__()
        self.tipo_combustivel = 'Diesel'
        self.cnh_requirida = 'C'
        self.capacidade_tanque = 150

class Pessoa():
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.cnh = None
        self.permissoes = None
        self.veiculo = None

    def cadastrar_colaborador(self):
        self.nome = input('Nome: ')
        self.cpf = input('CPF: ')
        self.cnh = input('CNH: ')
        self.permissoes = input('Permissões: ')
        self.veiculo = 0

    def apresentar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'CNH: {self.cnh}')
        print(f'Permissões: {self.permissoes}')
        print(f'Veículo: {self.veiculo}')

    def alugar_veiculo(self, cnh):
        cursor.execute(f"SELECT id_veiculo, placa, modelo FROM Veiculos WHERE alocado = 0 and cnh_requirida = '{cnh}'")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

# pessoa = Pessoa()
# pessoa.cadastrar_colaborador()
# pessoa.apresentar_dados()
pessoa = Pessoa()
pessoa.alugar_veiculo('B')