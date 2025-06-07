!pip install pulp

# Dados dos fornecedores (id, insumo, tempo_entrega, custo_unitário)
fornecedores = [
    {"id": 0, "insumo": "cimento", "tempo_entrega": 2, "custo_unit": 36.0},
    {"id": 1, "insumo": "cimento", "tempo_entrega": 1, "custo_unit": 37.9},
    {"id": 2, "insumo": "cimento", "tempo_entrega": 3, "custo_unit": 33.9},
    {"id": 3, "insumo": "cimento", "tempo_entrega": 1, "custo_unit": 40.0},
    {"id": 4, "insumo": "argamassa", "tempo_entrega": 1, "custo_unit": 51.9},
    {"id": 5, "insumo": "argamassa", "tempo_entrega": 1, "custo_unit": 49.9},
    {"id": 6, "insumo": "argamassa", "tempo_entrega": 3, "custo_unit": 36.9},
    {"id": 7, "insumo": "argamassa", "tempo_entrega": 2, "custo_unit": 44.9},
]

from pulp import *

# Parâmetros técnicos
Cmax = 3 * 7.2
Amax = 3 * 5.875
pilha_cimento = 10
pilha_argamassa = 15
area_cimento = 0.25
area_argamassa = 0.20
area_min = 4.0
area_max = 7.5

# Modelo
model = LpProblem("Selecionar_Fornecedores", LpMinimize)
z = {f["id"]: LpVariable(f"z_{f['id']}", cat=LpBinary) for f in fornecedores}
x = LpVariable("pilhas_cimento", cat="Integer", lowBound=0)
y = LpVariable("pilhas_argamassa", cat="Integer", lowBound=0)

# Objetivo: menor custo unitário combinado
model += lpSum([z[f["id"]] * f["custo_unit"] for f in fornecedores])

# Seleção de um fornecedor por insumo
model += lpSum([z[f["id"]] for f in fornecedores if f["insumo"] == "cimento"]) == 1
model += lpSum([z[f["id"]] for f in fornecedores if f["insumo"] == "argamassa"]) == 1

# Pilhas mínimas para cada fornecedor possível
for f in fornecedores:
    dias = f["tempo_entrega"]*2 + 1
    if f["insumo"] == "cimento":
        model += x * pilha_cimento >= z[f["id"]] * Cmax * dias
    else:
        model += y * pilha_argamassa >= z[f["id"]] * Amax * dias

# Área total restrita
model += area_cimento * x + area_argamassa * y >= area_min
model += area_cimento * x + area_argamassa * y <= area_max

# Resolver e imprimir
model.solve()
print("Fornecedor de cimento:", [f for f in fornecedores if z[f["id"]].varValue == 1 and f["insumo"] == "cimento"])
print("Fornecedor de argamassa:", [f for f in fornecedores if z[f["id"]].varValue == 1 and f["insumo"] == "argamassa"])
print(f"Pilhas cimento: {x.varValue}, pilhas argamassa: {y.varValue}")
print(f"Área total: {value(area_cimento*x + area_argamassa*y):.2f} m²")
print(f"Custo total unitário combinado: {value(model.objective):.2f}")
