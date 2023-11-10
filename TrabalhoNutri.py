Animal = int(input('Escolha o animal (1) Cão; (2) Gato: '))

if Animal == 1:
    print('Calculando para: Cão')
    PACão = int(input('Digite o Peso Atual do animal: '))
    ECCCão = int(input('Digite o ECC do animal: '))
    print('TPPS de 1 a 2%: {} a {} Kg'.format(PACão * 0.01, PACão * 0.02))
    if ECCCão == 8 or ECCCão == 9:
        PMCão = PACão * 0.80
        print('Peso Meta: {} Kg'.format(PMCão))
        print('NEPP: {} Kcal'.format(70 * (PMCão)**0.75))
    elif ECCCão == 6 or ECCCão == 7:
        PMCão = PACão * 0.85
        print('Peso Meta: {} Kg'.format(PMCão))
        print('NEPP: {} Kcal'.format(70 * (PMCão)**0.75))
    else:
        print('Opção Inválida')

elif Animal == 2:
    print('Calculando para: Gato')