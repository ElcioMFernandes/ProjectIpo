import csv
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
        with open('DATABASE/veiculos.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([self.placa, self.modelo, self.marca, self.disponivel, self.cnh_requerida])

    def apresentar_veiculo(self):
        print("DADOS DO VEÍCULO")
        print("Placa :", self.placa)
        print("Modelo :", self.modelo)
        print("Marca :", self.marca)
        print("Disponível :", "SIM" if self.disponivel else "NÃO")
        print("CNH requerida :", self.cnh_requerida)
        print('-'*30)
    
    def apresentar_todos_os_veiculos(self):
        with open('DATABASE/veiculos.csv', 'r') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha == ['placa', 'modelo', 'marca', 'disponivel', 'cnh_requerida'] or linha == []:
                    continue
                self.placa = linha[0]
                self.modelo = linha[1]
                self.marca = linha[2]
                self.disponivel = linha[3]
                self.cnh_requerida = linha[4]
                self.apresentar_veiculo()

    def alocar_veiculo(self):
        cpf = input("Digite o CPF do colaborador: ")
        while len(cpf) != 11 or not cpf.isnumeric():
            print("O CPF deve ter 11 dígitos e conter apenas números. Tente novamente.")
            cpf = input("Digite o CPF do colaborador: ")
        cpf = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        with open('DATABASE/colaboradores.csv', 'r') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha == ['nome', 'cpf', 'cnh', 'veiculo'] or linha == []:
                    continue
                if linha[1] == cpf:
                    if linha[3] != '0':
                        print("O colaborador já possui um veículo alocado.")
                        return
                    else:
                        cnh = linha[2]
                        break
            else:
                print("O colaborador não foi encontrado.")
                return
        placa = input("Digite a placa do veículo: ")
        if "-" not in placa:
            placa = "{}-{}".format(placa[:3], placa[3:]).upper()
        else:
            placa = placa.upper()
        with open('DATABASE/veiculos.csv', 'r') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha == ['placa', 'modelo', 'marca', 'disponivel', 'cnh_requerida'] or linha == []:
                    continue
                if linha[0] == placa:
                    if linha[3] == '0':
                        print("O veículo não está disponível.")
                        return
                    else:
                        cnh_requerida = linha[4]
                        break
            else:
                print("O veículo não foi encontrado.")
                return
            if cnh_requerida not in cnh:
                print("O colaborador não possui a CNH requerida para este veículo.")
                return
            with open('DATABASE/colaboradores.csv', 'r') as file:
                reader = csv.reader(file)
                for linha in reader:
                    if linha == ['nome', 'cpf', 'cnh', 'veiculo'] or linha == []:
                        continue
                    if linha[1] == cpf:
                        linha[3] = placa
                        break
                    