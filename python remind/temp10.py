import numpy as np
import nashpy as nash

# Матрицы выигрышей игроков
A = np.array([[2, 0],
              [0, 1]])

B = np.array([[1, 0],
              [0, 2]])

# Создание биматричной игры
game = nash.Game(A, B)

# Поиск всех равновесий по Нэшу
equilibria = list(game.support_enumeration())

print("ШАГ 1. Находим равновесия по Нэшу и вычисляем соответствующие выигрыши:\n")

# Сохраняем все возможные исходы и их выигрыши
all_outcomes = []
for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        all_outcomes.append(((i, j), (A[i, j], B[i, j])))

for i, eq in enumerate(equilibria, 1):
    p1_strategy = np.round(eq[0], 4)
    p2_strategy = np.round(eq[1], 4)

    p1_payoff = round(np.dot(p1_strategy, A @ p2_strategy), 4)
    p2_payoff = round(np.dot(p2_strategy, B @ p1_strategy), 4)

    current_payoff = (p1_payoff, p2_payoff)

    # Проверка на Парето-оптимальность
    is_pareto_optimal = True
    for outcome, (payoff1, payoff2) in all_outcomes:
        if (payoff1 >= p1_payoff and payoff2 >= p2_payoff) and (payoff1 > p1_payoff or payoff2 > p2_payoff):
            is_pareto_optimal = False
            break

    pareto_status = "Парето-оптимально" if is_pareto_optimal else "НЕ оптимально по Парето"

    print(f"Для равновесия {i}: ({p1_strategy[0]}, {p1_strategy[1]}), ({p2_strategy[0]}, {p2_strategy[1]}), "
          f"выигрыши: ({p1_payoff}, {p2_payoff}) → {pareto_status}")

# ШАГ 2. Ищем стратегию, которая дает максимальную сумму выигрышей (как если бы игроки сотрудничали)
print("\nШАГ 2. Находим стратегию, которая максимизирует сумму выигрышей (если бы игроки сотрудничали):")

max_total = -np.inf
best_i, best_j = -1, -1
best_p1_payoff, best_p2_payoff = 0, 0

for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        p1_payoff = A[i, j]
        p2_payoff = B[i, j]
        total = p1_payoff + p2_payoff

        if total > max_total:
            max_total = total
            best_i, best_j = i, j
            best_p1_payoff = p1_payoff
            best_p2_payoff = p2_payoff

# Средний выигрыш для обоих игроков, если они делят суммарный выигрыш пополам
average_p1_payoff = max_total / 2
average_p2_payoff = max_total / 2

# Вектор средних выигрышей
average_payoffs_vector = (average_p1_payoff, average_p2_payoff)

print(f"\nЕсли бы игроки могли договориться, они бы выбрали:")
print(f"Игрок 1 выбирает стратегию {best_i + 1} ([{int(best_i == 0)}, {int(best_i == 1)}]), "
      f"Игрок 2 выбирает стратегию {best_j + 1} ([{int(best_j == 0)}, {int(best_j == 1)}])")
print(f"Вектор выигрышей: ({best_p1_payoff}, {best_p2_payoff})")
print(f"Средний выигрыш для первого игрока: {average_p1_payoff}")
print(f"Средний выигрыш для второго игрока: {average_p2_payoff}")
print(f"Вектор средних выигрышей: {average_payoffs_vector}")
print(f"Суммарный выигрыш: {max_total}")
