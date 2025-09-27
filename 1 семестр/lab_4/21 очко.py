import random

def ask_player_choice():
    while True:
        choice = input("Выберите: [1] Взять карту / [0] Остановиться: ").strip()
        if choice == "1":
            return "hit"
        elif choice == "0":
            return "stand"
        else:
            print("⚠️ Введите 1 (взять) или 0 (остановиться).")

def play_game():
    # Начальная раздача по две карты
    player_cards = [random.randint(2, 11), random.randint(2, 11)]
    dealer_cards = [random.randint(2, 11), random.randint(2, 11)]

    player_sum = sum(player_cards)
    dealer_sum = sum(dealer_cards)

    print(f"Ваши карты: {player_cards} → {player_sum} очков")
    print(f"Открытая карта дилера: {dealer_cards[0]}")

    # Если сразу 21 у кого-то — мгновенный результат
    if player_sum == 21 and dealer_sum == 21:
        return result(player_sum, dealer_sum)
    if player_sum == 21:
        return result(player_sum, dealer_sum)
    if dealer_sum == 21:
        return result(player_sum, dealer_sum)

    # Ход игрока
    while True:
        choice = ask_player_choice()
        if choice == "hit":
            card = random.randint(2, 11)
            player_cards.append(card)
            player_sum += card
            print(f"🃏 Вам выпала карта {card}. Сумма = {player_sum}")
            if player_sum >= 21:
                # при 21 или переборе сразу выходим к результату
                return result(player_sum, dealer_sum)
        else:  # stand
            print(f"Вы остановились на {player_sum} очках\n")
            break

    # Ход дилера (только если игрок не перебрал и не набрал 21)
    print(f"Карты дилера: {dealer_cards} → {dealer_sum} очков")
    while dealer_sum < 17:
        card = random.randint(2, 11)
        dealer_cards.append(card)
        dealer_sum += card
        print(f"(Дилер берёт карту) +{card} → {dealer_sum}")
        if dealer_sum >= 21:
            # при 21 или переборе — сразу выходим
            return result(player_sum, dealer_sum)

    # Итоговый расклад
    return result(player_sum, dealer_sum)

def result(player_sum, dealer_sum):
    print(f"\n🧾 Финал — Игрок: {player_sum} | Дилер: {dealer_sum}\n")
    if player_sum > 21:
        print("❌ Вы проиграли — у вас перебор.")
    elif dealer_sum > 21:
        print("✅ Вы выиграли — у дилера перебор.")
    elif player_sum == 21 and dealer_sum == 21:
        print("🤝 Ничья — оба по 21.")
    elif player_sum == 21:
        print("🎉 Вы выиграли — у вас 21!")
    elif dealer_sum == 21:
        print("🟥 Вы проиграли — у дилера 21.")
    elif player_sum > dealer_sum:
        print("✅ Вы выиграли — у вас больше очков.")
    elif dealer_sum > player_sum:
        print("🟥 Вы проиграли — у дилера больше очков.")
    else:
        print("🤝 Ничья — очки равны.")
    # После вывода результата игра завершена
    return

if __name__ == "__main__":
    play_game()
