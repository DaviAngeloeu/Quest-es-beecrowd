def calcular_imc():
    nomepaciente = input("Digite o nome do paciente")
    telefonepaciente = input("Digite o telefone do paciente")
    peso = float(input('Digite o peso do paciente'))
    altura = float(input("Digite a altura do paciente"))
    imc = peso / (altura*altura)
    print(f'"O imc do paciente",{nomepaciente},é,{imc:.2f}')

calcular_imc()
    