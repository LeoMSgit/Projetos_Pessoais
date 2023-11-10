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
    PAGato = int(input('Digite o Peso Atual do animal: '))
    ECCGato = int(input('Digite o ECC do animal: '))
    print('TPPS de 0,5 a 1%: {} a {} Kg'.format(PAGato * 0.005, PAGato * 0.01))
    print('NEPP: {} Kcal'.format(85 * (PAGato) ** 0.4))
    if ECCGato == 8 or ECCGato == 9:
        PMGato = PAGato * 0.85
        print('Peso Meta: {} Kg'.format(PMGato))
    elif ECCGato == 6 or ECCGato == 7:
        PMGato = PAGato * 0.90
        print('Peso Meta: {} Kg'.format(PMGato))
    else:
        print('Opção Inválida')
