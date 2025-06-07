!pip install pulp

# Tabela servicos
servicos = [
    {"id": 0, "nome": "Alvenaria (cerâmico)", "precedente": "-", "insumo": "Cimento", "produtividade": 15, "consumo_kg_m2": 4.25, "consumo_diario_kg": 63.75, "consumo_diario_sacos": 1.275, "quant_m2": 1450, "consumo_total_sacos": 123.25, "cura": 3},
    {"id": 1, "nome": "Chapisco (interno)", "precedente": 0, "insumo": "Cimento", "produtividade": 30, "consumo_kg_m2": 2, "consumo_diario_kg": 60, "consumo_diario_sacos": 1.2, "quant_m2": 2105, "consumo_total_sacos": 84.2, "cura": 3},
    {"id": 2, "nome": "Chapisco (externo)", "precedente": 0, "insumo": "Cimento", "produtividade": 20, "consumo_kg_m2": 2, "consumo_diario_kg": 40, "consumo_diario_sacos": 0.8, "quant_m2": 650, "consumo_total_sacos": 26, "cura": 3},
    {"id": 3, "nome": "Reboco (interno)", "precedente": 1, "insumo": "Cimento", "produtividade": 25, "consumo_kg_m2": 7.5, "consumo_diario_kg": 187.5, "consumo_diario_sacos": 3.75, "quant_m2": 2105, "consumo_total_sacos": 315.75, "cura": 21},
    {"id": 4, "nome": "Reboco (externo)", "precedente": 2, "insumo": "Cimento", "produtividade": 15, "consumo_kg_m2": 7.5, "consumo_diario_kg": 112.5, "consumo_diario_sacos": 2.25, "quant_m2": 650, "consumo_total_sacos": 97.5, "cura": 21},
    {"id": 5, "nome": "Contrapiso", "precedente": "0;3;4", "insumo": "Cimento", "produtividade": 40, "consumo_kg_m2": 9, "consumo_diario_kg": 360, "consumo_diario_sacos": 7.2, "quant_m2": 890, "consumo_total_sacos": 160.2, "cura": 14},
    {"id": 6, "nome": "Revest. Piso Interno 60x60", "precedente": 5, "insumo": "Argamassa ACIII", "produtividade": 25, "consumo_kg_m2": 4.7, "consumo_diario_kg": 117.5, "consumo_diario_sacos": 5.875, "quant_m2": 750, "consumo_total_sacos": 176.25, "cura": 0},
    {"id": 7, "nome": "Revest. Piso Externo 60x60", "precedente": 5, "insumo": "Argamassa ACIII", "produtividade": 18, "consumo_kg_m2": 5.5, "consumo_diario_kg": 99, "consumo_diario_sacos": 4.95, "quant_m2": 140, "consumo_total_sacos": 38.5, "cura": 0},
    {"id": 8, "nome": "Revest. Parede Interna 30x60", "precedente": 3, "insumo": "Argamassa ACIII", "produtividade": 20, "consumo_kg_m2": 4.5, "consumo_diario_kg": 90, "consumo_diario_sacos": 4.5, "quant_m2": 770, "consumo_total_sacos": 173.25, "cura": 0},
    {"id": 9, "nome": "Revest. Parede Externa 10x20", "precedente": 4, "insumo": "Argamassa ACIII", "produtividade": 14, "consumo_kg_m2": 5.5, "consumo_diario_kg": 77, "consumo_diario_sacos": 3.85, "quant_m2": 650, "consumo_total_sacos": 178.75, "cura": 0},
]

def encontrar_maximos_consumo(servicos):
    nome_cim_max = None
    valor_cim_max = 0
    serv_argamassa_max = None
    valor_arg_max = 0

    for serv in servicos:
        if serv["insumo"] == "Cimento" and serv["consumo_diario_sacos"] > valor_cim_max:
            valor_cim_max = serv["consumo_diario_sacos"]
            nome_cim_max = serv["nome"]

        if serv["insumo"] == "Argamassa ACIII" and serv["consumo_diario_sacos"] > valor_arg_max:
            valor_arg_max = serv["consumo_diario_sacos"]
            nome_arg_max = serv["nome"]

    return nome_cim_max,valor_cim_max,nome_arg_max,valor_arg_max


from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, value

# Dados

nome_cim_max, valor_cim_max, nome_arg_max, valor_arg_max = encontrar_maximos_consumo(servicos)

Cmax = 3 * valor_cim_max     # consumo máx. cimento (sacos/dia)
Amax = 3 * valor_arg_max   # consumo máx. argamassa (sacos/dia)
Tc = 2          # tempo reposição cimento (dias)
Ta = 1          # tempo reposição argamassa (dias)
Ec = Tc + 1     # estoque segurança cimento
Ea = Ta + 1     # estoque segurança argamassa
pilha_cimento = 10      # sacos/pilha
pilha_argamassa = 15    # sacos/pilha
area_cimento = 0.25     # m²/pilha cimento
area_argamassa = 0.20   # m²/pilha argamassa
custo_cimento = 35
custo_argamassa = 49

print(Cmax)
print(Amax)

# Modelo
model = LpProblem("Dimensionamento_Almoxarifado", LpMinimize)
x = LpVariable("pilhas_cimento", lowBound=0, cat=LpInteger)
y = LpVariable("pilhas_argamassa", lowBound=0, cat=LpInteger)

# Objetivo
model += area_cimento * x + area_argamassa * y

# Restrições
model += pilha_cimento * x >= Cmax * (Tc + Ec)
model += pilha_argamassa * y >= Amax * (Ta + Ea)

# Resolver
model.solve()

# Resultados
print(f"Tamanho mínimo do almoxarifado: {value(model.objective):.2f} m²")
print(f"Nº de pilhas de cimento: {x.varValue}")
print(f"Nº de pilhas de argamassa: {y.varValue}")
print(f"Valor do estoque: {(y.varValue * 15 * custo_argamassa + x.varValue * 10 * custo_cimento):.2f} reais.")
