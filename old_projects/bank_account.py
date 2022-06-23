# a program that is going to imitate back account
# you have certain amount of money that you can withdraw
# and also top up money

from result import Ok, Error

class BankAccount():

    def __init__(self, money=0):
        self.balance = money

    def tryWithdrawMoney(self, amount):
        if (self.balance > amount):
            self.balance -= amount
            return Ok("Wypłacono pieniądze", amount)
        return Error("Nie wypłacono za mało funduszy", amount)

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return str(self.balance)


class BankAccountWithMinimunValue(BankAccount):
    def __init__(self, money, accountLimit =1000):
        super().__init__(money)
        self.accountLimit = accountLimit

    
    def tryWithdrawMoney(self, amount, minimumAccountValue =1000):
        if self.balance - amount >= minimumAccountValue:
            return super().tryWithdrawMoney(amount)
        elif self.balance - amount < minimumAccountValue:
            amountToWithdraw = self.balance - minimumAccountValue
            self.balance == minimumAccountValue
            return Ok("Wypłacono "+str(amountToWithdraw)+" ponieważ kwota którą chciałes wypłacic przekraczała limit twojego konta", "Kwota którą chciałeś wypłacic "+str(amount))

        return Error("Nie wypłacono za mało funduszy", amount)

    



