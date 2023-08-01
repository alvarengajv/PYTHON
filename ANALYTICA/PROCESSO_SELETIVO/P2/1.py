def angulo_relogio(horario):
    horas, minutos = map(int, horario.split(':'))

    if len(horario) != 5:
        print("Input inválido")
        return None

    if horas < 0 or minutos < 0 or horas > 23 or minutos > 59:
        print("Input inválido")
        return None

    horas %= 12

    angulo_minutos = (360 / 60) * minutos
    angulo_horas = (360 / 12) * horas + ((minutos / 60) * (360 / 12))

    angulo_ponteiros = abs(angulo_horas - angulo_minutos)

    angulo_complementar = 360 - angulo_ponteiros

    menor_angulo_ponteiros = min(360 - angulo_ponteiros, angulo_complementar)

    return menor_angulo_ponteiros


def main():
    while True:
        horario = input("Digite o horário no formato 'hh:mm' (ou 'f' para encerrar): ")
        if horario == 'f':
            print("Programa encerrado")
            break

        else:
            angulo = angulo_relogio(horario)
            if angulo is not None:
                print(f"O menor ângulo é de {angulo}°")

            else:
                continue


if __name__ == "__main__":
    main()
