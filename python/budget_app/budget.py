class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def get_balance(self):
        return self.balance

    def check_funds(self, check):
        if self.balance < check:
            return False
        else:
            return True

    def deposit(self, amount, description=""):
        self.balance += amount
        transaction = {"amount": amount, "description": description}
        self.ledger.append(transaction)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            transaction = {"amount": -amount, "description": description}
            self.ledger.append(transaction)
            return True
        else:
            return False

    def transfer(self, amount, transferee=""):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {transferee.name}")
            transferee.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def __str__(self):

        star_count = (30 - len(self.name)) // 2
        title_line = "*" * star_count + self.name + "*" * star_count
        if len(title_line) != 30:
            title_line += "*"
        title_line += "\n"

        transaction_lines = ""
        for transaction in self.ledger:
            amt = transaction.get("amount")
            amt = "%0.2f" % amt
            descr = transaction.get("description")
            descr = descr[:23]
            transaction_lines += descr + (
                str(amt)[:7]).rjust(30 - len(descr)) + "\n"

        total_line = f"Total: {self.balance}"

        object_string = title_line + transaction_lines + total_line

        return object_string


def create_spend_chart(categories):
    total = 0
    subtotals = dict()
    percentage = dict()

    for categor in categories:
        subtotal = 0
        for transaction in categor.ledger:
            amt = transaction.get("amount")
            if amt < 0:
                amt *= -1
                subtotal += amt
        subtotals[categor.name] = subtotal
        total += subtotal

    for key, value in subtotals.items():
        percentage[key] = (subtotals.get(key)) / total * 100
        percentage[key] = percentage.get(key) - (percentage.get(key) % 10)

    ordered_perc = [(v, k) for (k, v) in percentage.items()]
    #ordered_perc = sorted(ordered_perc, reverse = True)

    bar_chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        bar_chart += str(i).rjust(3) + "| "
        for (x, y) in ordered_perc:
            if x >= i:
                bar_chart += "o" + " " * 2
            else:
                bar_chart += " " * 3
        bar_chart += "\n"

    bar_chart += (" " * 4) + ("-" * 10) + "\n"

    labels = []
    max_label = 0
    for categor in categories:
        labels.append(categor.name)
        x = len(categor.name)
        if x > max_label:
            max_label = x
    for j in range(len(labels)):
        labels[j] = labels[j].ljust(max_label)

    for k in range(max_label):
        bar_chart += " " * 5
        for label in labels:
            bar_chart += label[k] + " " * 2
        bar_chart += "\n"
    
    return bar_chart
