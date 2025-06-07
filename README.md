
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
Universidade Federal da Paraíba – PPGEP  
Prof. Anand Subramanian

### 🗓️ João Pessoa, Junho de 2025
