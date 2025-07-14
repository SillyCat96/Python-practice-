import math
import random

def simulate_lottery(lottery_total: int, lottery_pick: int, players: int, tickets_per_player: int, ticket_price: int, prize_fund_ratio: float):
    winning_numbers = set(random.sample(range(1, lottery_total + 1), lottery_pick))
    
    base_prizes = {
        6: 5_000_000,
        5: 100_000,
        4: 1_000,
        3: 100,
        2: 10
    }
    
    total_tickets = players * tickets_per_player
    total_revenue = total_tickets * ticket_price
    prize_fund = total_revenue * prize_fund_ratio
    
    winnings_per_category = {k: 0 for k in base_prizes}
    ticket_count_per_category = {k: 0 for k in base_prizes}  # Считаем количество билетов по категориям
    player_results = []
    
    for player in range(players):
        player_winnings = 0
        for _ in range(tickets_per_player):
            ticket_numbers = set(random.sample(range(1, lottery_total + 1), lottery_pick))
            matches = len(winning_numbers.intersection(ticket_numbers))
            winnings = base_prizes.get(matches, 0)
            player_winnings += winnings
            if matches in winnings_per_category:
                winnings_per_category[matches] += winnings
                ticket_count_per_category[matches] += 1  # Увеличиваем счетчик для данной категории
        net_result = player_winnings - (tickets_per_player * ticket_price)
        player_results.append((player + 1, player_winnings, net_result))
    
    total_payout = sum(winnings_per_category.values())
    
    adjustment_ratio = prize_fund / total_payout if total_payout > 0 else 1.0
    percentage_change = (adjustment_ratio - 1) * 100
    
    for i in range(len(player_results)):
        player_results[i] = (
            player_results[i][0],
            int(player_results[i][1] * adjustment_ratio),
            int((player_results[i][1] * adjustment_ratio) - (tickets_per_player * ticket_price))
        )
    total_payout = prize_fund
    
    print(f"Общий сбор: {total_revenue} руб.")
    print(f"Призовой фонд ({prize_fund_ratio * 100}%): {prize_fund} руб.")
    print(f"Общая сумма выигрышей: {total_payout} руб.")
    
    winners = sorted([res for res in player_results if res[2] > 0], key=lambda x: x[1], reverse=True)[:50]
    losers = [res for res in player_results if res[2] <= 0]
    
    adjustment_status = "увеличено" if percentage_change > 0 else "уменьшено"
    print(f"\n🏆 Победители ({adjustment_status} на {abs(percentage_change):.2f}%)")
    
    if winners:
        for player_id, winnings, net in winners:
            print(f"Игрок {player_id}: Выиграл {winnings} руб. (Чистая прибыль: +{net} руб.)")
    else:
        print("😞 Никто не выиграл значительных сумм.")
    
    print("\n❌ Проигравшие:")
    for player_id, winnings, net in losers[:10]:
        print(f"Игрок {player_id}: Выиграл {winnings} руб. (Чистый убыток: {net} руб.)")

    # Расчет процентов выигрышей по категориям с учетом корректировки
    print("\n📊 Таблица выигрышей по категориям:")
    for matches in base_prizes.keys():
        total_category_payout = winnings_per_category[matches] * adjustment_ratio  # Корректируем суммы выигрышей
        category_percentage = (total_category_payout / total_payout) * 100 if total_payout > 0 else 0
        total_winners_in_category = ticket_count_per_category[matches]  # Количество победителей в категории
        print(f"{matches}/6: {total_category_payout:.0f} руб. ({category_percentage:.2f}%) - Победителей: {total_winners_in_category}")
    
    return player_results

if __name__ == "__main__":
    lottery_total = 49
    lottery_pick = 6
    players = 2_500_000
    tickets_per_player = 6
    ticket_price = 10
    prize_fund_ratio = 0.7
    results = simulate_lottery(lottery_total, lottery_pick, players, tickets_per_player, ticket_price, prize_fund_ratio)
