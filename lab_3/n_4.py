class BankAccount:
    """
    Класс банковского счёта с инкапсуляцией.
    Хранит баланс, владельца и историю транзакций.
    """

    def __init__(self, owner):
        """
        Инициализирует счёт с нулевым балансом и владельцем.
        """
        self.owner = owner
        self._balance = 0
        self._transactions = []

    def deposit(self, amount):
        """
        Вносит деньги на счёт.
        Логирует операцию как 'Пополнение'.
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount
        self._transactions.append(f"Пополнение: +{amount}")

    def withdraw(self, amount):
        """
        Снимает деньги со счёта.
        Логирует операцию как 'Снятие'.
        """
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount
        self._transactions.append(f"Снятие: -{amount}")

    @property
    def balance(self):
        """
        Возвращает текущий баланс счёта.
        """
        return self._balance

    def get_transactions(self):
        """
        Возвращает список всех транзакций.
        """
        return self._transactions



if __name__ == "__main__":
    acc = BankAccount("Юля")
    acc.deposit(1000)
    acc.withdraw(333)
    print("Баланс:", acc.balance)
    print("Операции:")
    for t in acc.get_transactions():
        print(t)
