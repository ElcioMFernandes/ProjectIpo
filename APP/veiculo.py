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
        file.close()

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
            rows = list(reader)
            for row in rows[1:-1]:
                if row:  # Check if row is not empty
                    if len(row) >= 5:  # Check if row has at least 5 columns
                        print('-'*30)
                        print("DADOS DO VEÍCULO")
                        print('-'*30)
                        print("Placa :", row[0])
                        print("Modelo :", row[1])
                        print("Marca :", row[2])
                        print("Disponível :", "SIM" if row[3] == "True" else "NÃO")
                        print("CNH requerida :", row[4])
            print('-'*30)
        file.close()

    def alocar_veiculo(self):
        placa = input("Digite a placa do veículo: ").upper()
        placa = "{}-{}".format(placa[:3], placa[3:])
        with open('DATABASE/veiculos.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        for row in rows[1:-1]:
            if row and row[0] == placa and row[3] == "True":
                row[3] = "False"
        with open('DATABASE/veiculos.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            