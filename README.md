
# Otimização Linear: Dimensionamento de Estoque de Ensacados e Seleção de Fornecedores

Este projeto apresenta um modelo de **programação linear inteira mista** para o **dimensionamento mínimo do estoque de insumos ensacados (cimento e argamassa colante)** em um canteiro de obras, visando garantir a **não interrupção dos serviços** e, simultaneamente, selecionar fornecedores com **menor custo unitário possível** dentro de prazos de entrega compatíveis.

## 📌 Objetivo

Minimizar a área ocupada por pilhas de cimento e argamassa, considerando o consumo diário, tempo de reposição e estoque de segurança, além de escolher fornecedores que garantam o abastecimento sem atrasos e com o menor custo possível.

## 📦 Insumos

### Categoria A: Cimento Portland
- Dimensões: 18 × 32 × 50 cm
- Empilhamento: 10 sacos
- Área por pilha: 0,25 m²
- Validade: 80 dias
- Custo médio: R$ 35,00 a R$ 45,00

### Categoria B: Argamassa Colante ACIII
- Dimensões: 10 × 20 × 46 cm
- Empilhamento: 15 sacos
- Área por pilha: 0,20 m²
- Validade: 220 dias
- Custo médio: R$ 40,00 a R$ 60,00

## 📦 Serviços

Dados de consumo de insumos para cada serviço:

| Serviço | ID | Precedente | Insumo | Produtividade (m²/dia.equipe) | Consumo (kg/m².equipe) | Consumo diário (kg/equipe) | Consumo diário (sacos/equipe) | Qtd. total (m²) | Consumo total (sacos) | Cura (dias) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Alvenaria (cerâmico) | 0 | - | Cimento | 15 | 4,25 | 63,75 | 1,275 | 1450 | 123,25 | 3 |
| Chapisco (interno) | 1 | 0 | Cimento | 30 | 2 | 60 | 1,2 | 2105 | 84,2 | 3 |
| Chapisco (externo) | 2 | 0 | Cimento | 20 | 2 | 40 | 0,8 | 650 | 26 | 3 |
| Reboco (interno) | 3 | 1 | Cimento | 25 | 7,5 | 187,5 | 3,75 | 2105 | 315,75 | 21 |
| Reboco (externo) | 4 | 2 | Cimento | 15 | 7,5 | 112,5 | 2,25 | 650 | 97,5 | 21 |
| Contrapiso | 5 | 0;3;4 | Cimento | 40 | 9 | 360 | 7,2 | 890 | 160,2 | 14 |
| Revest. Piso Interno 60x60 | 6 | 5 | Argamassa ACIII | 25 | 4,7 | 117,5 | 5,875 | 750 | 176,25 | 0 |
| Revest. Piso Externo 60x60 | 7 | 5 | Argamassa ACIII | 18 | 5,5 | 99 | 4,95 | 140 | 38,5 | 0 |
| Revest. Parede Interna 30x60 | 8 | 3 | Argamassa ACIII | 20 | 4,5 | 90 | 4,5 | 770 | 173,25 | 0 |
| Revest. Parede Externa 10x20 | 9 | 4 | Argamassa ACIII | 14 | 5,5 | 77 | 3,85 | 650 | 178,75 | 0 |



## 📈 Modelo Matemático

### Variáveis
- `x`: número de pilhas de cimento (10 sacos cada)
- `y`: número de pilhas de argamassa (15 sacos cada)

### Função objetivo
```
Min Z = 0.25x + 0.20y
```

### Restrições
```
10x ≥ Cmax × (Tc + Ec)
15y ≥ Amax × (Ta + Ea)

x, y ∈ ℤ⁺
```

Onde:
- `Cmax = 3 × maior consumo diário de cimento`
- `Amax = 3 × maior consumo diário de argamassa`
- `Ec = Tc + 1`, `Ea = Ta + 1`

Exemplo:
```
10x ≥ 3 × 7.2 × (2Tc + 1)
15y ≥ 3 × 5.875 × (2Ta + 1)
```

## 🚚 Seleção de Fornecedores

Fornecedores disponíveis com diferentes prazos e preços:

| ID | Produto    | Entrega (dias) | Custo unitário (R$) |
|----|------------|----------------|----------------------|
| 0  | Cimento    | 2              | 36,00                |
| 1  | Cimento    | 1              | 37,90                |
| 2  | Cimento    | 3              | 33,90                |
| 3  | Cimento    | 1              | 40,00                |
| 4  | Argamassa  | 1              | 51,90                |
| 5  | Argamassa  | 1              | 49,90                |
| 6  | Argamassa  | 3              | 36,90                |
| 7  | Argamassa  | 2              | 44,90                |

### Problema de otimização secundário
Selecionar fornecedores que minimizem o custo total e respeitem os tempos máximos de entrega derivados das variáveis `Tc` e `Ta`.

## 🧮 Ferramentas Sugeridas
- Python com `PuLP`
- CBC

## 📄 Autor

**Vinicius Bezerra Cavalcanti Centurion**  
Universidade Federal da Paraíba – PPGEPS 
Prof. Anand Subramanian

### 🗓️ João Pessoa, Junho de 2025
