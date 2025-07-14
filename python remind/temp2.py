def calculate_annual_payment(loan_amount, loan_term, interest_rate):
    # Переводим проценты в десятичную форму
    r = interest_rate / 100
    
    # Расчет ежегодного платежа по формуле аннуитетного платежа
    annual_payment = loan_amount * (r * (1 + r)**loan_term) / ((1 + r)**loan_term - 1)
    
    return annual_payment

# Параметры кредита
loan_amount = 300000  # сумма кредита в рублях
loan_term = 5  # срок кредита в годах
interest_rate = 80  # процентная ставка

# Расчет ежегодного платежа
annual_payment = calculate_annual_payment(loan_amount, loan_term, interest_rate)

print(f"Сумма кредита: {loan_amount} руб.")
print(f"Срок кредита: {loan_term} лет")
print(f"Процентная ставка: {interest_rate}%")
print(f"Ежегодный платеж: {annual_payment:.2f} руб.")

# Расчет общей суммы переплаты
total_payment = annual_payment * loan_term
overpayment = total_payment - loan_amount

print(f"Общая сумма платежей: {total_payment:.2f} руб.")
print(f"Сумма переплаты: {overpayment:.2f} руб.")