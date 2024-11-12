def main ():
    total_dias = int(input("Informe sua idade em dias: "))
    dias = total_dias

    anos = dias // 365
    dias = dias % 365

    meses = dias // 30
    dias = dias % 30

    dias = dias % 7

    print("Sua idade em dias é {0} dias\n".format(total_dias))
    print("Isso equivale a:")
    print("{0} anos".format(anos))
    print("{0} meses".format(meses))
    print("{0} dias".format(dias))

main()