import os

class Colaborador:
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.cnh = None
        self.veiculo = None

    def adicionar_colaborador(self):
        while True:
            self.nome = input("Digite o nome do colaborador: ")
            if len(self.nome) >= 3 and self.nome.isalpha():
                break
            else:
                print("O nome deve ter pelo menos 3 letras e conter apenas letras. Tente novamente.")
        cpf = input("Digite o CPF do colaborador: ")
        self.cpf = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        self.cnh = []
        cnh_c = input("O colaborador possui CNH do tipo C? (s/n): ")
        if cnh_c.lower() == 's':
            self.cnh.append('C')
            self.cnh.append('B')
        else:
            cnh_b = input("O colaborador possui CNH do tipo B? (s/n): ")
            if cnh_b.lower() == 's':
                self.cnh.append('B')
        cnh_a = input("O colaborador possui CNH do tipo A? (s/n): ")
        if cnh_a.lower() == 's':
            self.cnh.append('A')

        self.veiculo = 0
        print('-'*30)
    
    def apresentar_colaborador(self):
        print("DADOS DO COLABORADOR")
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("CNH:", ', '.join(self.cnh))
        print("Veículo:", self.veiculo)
        print('-'*30)

class Veiculo:
    def __init__(self):
        self.placa = None
        self.modelo = None
        self.marca = None
        self.disponivel = None
        cnh_requerida = None

    def adicionar_veiculo(self):
        placa = input("Digite a placa do veículo: ")
        if "-" not in placa:
            self.placa = "{}-{}".format(placa[:3], placa[3:]).upper()
        else:
            self.placa = placa.upper()
        self.modelo = input("Digite o modelo do veículo: ").upper()
        self.marca = input("Digite a marca do veículo: ").upper()
        self.disponivel = True

    def apresentar_veiculo(self):
        print("DADOS DO VEÍCULO")
        print("Placa :", self.placa)
        print("Modelo :", self.modelo)
        print("Marca :", self.marca)
        print("Disponível :", "SIM" if self.disponivel else "NÃO")
        print("CNH requerida :", self.cnh_requerida)
        print('-'*30)

class Carro(Veiculo):
    def __init__(self):
        self.cnh_requerida = 'B'

class Moto(Veiculo):
    def __init__(self):
        self.cnh_requerida = 'A'

class Caminhao(Veiculo):
    def __init__(self):
        self.cnh_requerida = 'C'

def menu(nome_menu, *opcoes):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"+{'-'*30}+\n|{nome_menu:^30}|\n+{'-'*30}+")
    for opcao in opcoes:
        print(f"|{opcao:<30}|\n+{'-'*30}+")
    try:
        opcao = int(input("Digite a opção desejada: "))
        return opcao
    except:
        print("Opção inválida!")
        input("Você precisa digitar um número. Pressione ENTER para continuar...")
        menu(nome_menu, *opcoes)

def menu_principal():
    op = menu("Menu Principal", "1. Colaborador", "2. Veículo", "3. Sair")
    if op == 1:
        menu_colaborador()
    elif op == 2:
        menu_veiculo()
    elif op == 3:
        exit()
    else:
        print("Opção inválida!")
        input("Você precisa digitar um número. Pressione ENTER para continuar...")
        menu_principal()

def menu_colaborador():
    op = menu("Menu Colaborador", "1. Cadastrar", "2. Voltar")
    if op == 1:
        colaborador = Colaborador()
        colaborador.adicionar_colaborador()
        colaborador.apresentar_colaborador()
        input("Pressione ENTER para continuar...")
        menu_colaborador()
    elif op == 2:
        menu_principal()
    else:
        print("Opção inválida!")
        input("Você precisa digitar um número. Pressione ENTER para continuar...")
        menu_colaborador()

def menu_veiculo():
    op = menu("Menu Veículo", "1. Cadastrar", "2. Alocar","3. Devolver", "4. Voltar")
    if op == 1:
        op = menu("Menu Veículo", "1. Carro", "2. Moto", "3. Caminhão", "4. Voltar")
        if op == 1:
            veiculo = Carro()
            veiculo.adicionar_veiculo()
            veiculo.apresentar_veiculo()
            input("Pressione ENTER para continuar...")
            menu_veiculo()
        elif op == 2:
            veiculo = Moto()
            veiculo.adicionar_veiculo()
            veiculo.apresentar_veiculo()
            input("Pressione ENTER para continuar...")
            menu_veiculo()
        elif op == 3:
            veiculo = Caminhao()
            veiculo.adicionar_veiculo()
            veiculo.apresentar_veiculo()
            input("Pressione ENTER para continuar...")
            menu_veiculo()
        elif op == 4:
            menu_veiculo()  
        else:
            print("Opção inválida!")
            input("Você precisa digitar um número. Pressione ENTER para continuar...")
            menu_veiculo()
    elif op == 2:
        print("Alocar")
    elif op == 3:
        print("Devolver")
    elif op == 4:
        menu_principal()
    else:
        print("Opção inválida!")
        input("Você precisa digitar um número. Pressione ENTER para continuar...")
        menu_veiculo()

menu_principal()