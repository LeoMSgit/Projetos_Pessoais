# Refatoração do código de cálculo de IMC e protocolo de perda de peso para cães e gatos

def calcular_tpps(peso_atual, porcentagem_min, porcentagem_max):
    """Calcula a Taxa de Perda de Peso Sugerida (TPPS) com base no peso atual."""
    return peso_atual * porcentagem_min, peso_atual * porcentagem_max

def calcular_peso_meta(peso_atual, ecc, fator_cao, fator_gato):
    """Calcula o Peso Meta e valida ECC."""
    if ecc == 8 or ecc == 9:
        return peso_atual * fator_cao
    elif ecc == 6 or ecc == 7:
        return peso_atual * fator_gato
    else:
        return None  # ECC inválido

def calcular_nepp(peso_meta, is_cao=True):
    """Calcula a Necessidade Energética para Perda de Peso (NEPP)."""
    if is_cao:
        return 70 * (peso_meta ** 0.75)
    else:
        return 85 * (peso_meta ** 0.4)

def protocolo_perda_peso():
    # Entrada de dados do usuário
    try:
        animal = int(input('Escolha o animal (1) Cão; (2) Gato: '))
        if animal not in [1, 2]:
            raise ValueError("Opção inválida. Escolha 1 para Cão ou 2 para Gato.")
        
        if animal == 1:
            print('Calculando para: Cão')
            peso_atual = float(input('Digite o Peso Atual do animal (Kg): '))
            ecc = int(input('Digite o ECC do animal (6-9): '))

            tpps_min, tpps_max = calcular_tpps(peso_atual, 0.01, 0.02)
            print(f'TPPS de 1 a 2%: {tpps_min:.2f} a {tpps_max:.2f} Kg')

            peso_meta = calcular_peso_meta(peso_atual, ecc, 0.80, 0.85)
            if peso_meta:
                print(f'Peso Meta: {peso_meta:.2f} Kg')
                nepp = calcular_nepp(peso_meta, is_cao=True)
                print(f'NEPP: {nepp:.2f} Kcal')
            else:
                print("ECC inválido. Por favor, insira um valor entre 6 e 9.")

        elif animal == 2:
            print('Calculando para: Gato')
            peso_atual = float(input('Digite o Peso Atual do animal (Kg): '))
            ecc = int(input('Digite o ECC do animal (6-9): '))

            tpps_min, tpps_max = calcular_tpps(peso_atual, 0.005, 0.01)
            print(f'TPPS de 0,5 a 1%: {tpps_min:.2f} a {tpps_max:.2f} Kg')
            print(f'NEPP: {calcular_nepp(peso_atual, is_cao=False):.2f} Kcal')

            peso_meta = calcular_peso_meta(peso_atual, ecc, 0.85, 0.90)
            if peso_meta:
                print(f'Peso Meta: {peso_meta:.2f} Kg')
            else:
                print("ECC inválido. Por favor, insira um valor entre 6 e 9.")

    except ValueError as e:
        print(f"Erro de entrada: {e}")

# protocolo_perda_peso()