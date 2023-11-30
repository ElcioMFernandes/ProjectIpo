import csv
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
        while len(cpf) != 11 or not cpf.isnumeric():
            print("O CPF deve ter 11 dígitos e conter apenas números. Tente novamente.")
            cpf = input("Digite o CPF do colaborador: ")
        self.cpf = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        self.cnh = []
        with open('database/colaboradores.csv', 'r') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha == ['nome', 'cpf', 'cnh', 'veiculo'] or linha == []:
                    continue
                if linha[1] == self.cpf:
                    print("O CPF digitado já está cadastrado. Tente novamente.")
                    self.adicionar_colaborador()
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
        if len(self.cnh) == 0:
            print("O colaborador deve possuir pelo menos uma CNH.")
            return
        self.veiculo = 0
        print('-'*30)
        with open('DATABASE/colaboradores.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([self.nome, self.cpf, self.cnh, self.veiculo])

    def apresentar_colaborador(self):
        print("DADOS DO COLABORADOR")
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("CNH:", ', '.join(self.cnh))
        print("Veículo:", self.veiculo)
        print('-'*30)

    def apresentar_todos_os_colaboradores(self):
        with open('DATABASE/colaboradores.csv', 'r') as file:
            reader = csv.reader(file)
            print(f"LISTA DE COLABORADORES\n{'-'*30}\n")
            for linha in reader:
                if linha == ['nome', 'cpf', 'cnh', 'veiculo'] or linha == []:
                    continue
                print("Nome:", linha[0])
                print("CPF:", linha[1])
                print("CNH:", linha[2])
                print("Veículo:", linha[3])
                print('-'*30)
                