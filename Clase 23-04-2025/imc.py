peso = float(input("Ingrese su peso (KG):"))
altura = float(input("Ingrese su altura(M):"))

#124 kg
#1.72  - 2,9584  - IMC --> 41.9



imc = peso / (altura * altura)

if imc < 18.5:
    print("Bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal (saludable)")
elif imc >= 25.0 and imc <= 29.9:
    print("	Sobrepeso")
elif imc >= 30.0 and imc <=34.9:
    print("Obesidad grado I")
elif imc >= 35.0 and imc <= 39.9:
    print("Obesidad grado II")
else :
    print("Obesidad grado III (mórbida)")


