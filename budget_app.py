class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

    def get_balance(self):
      total = 0
      for item in self.ledger:
        total += item['amount']
      return total

  def withdraw(self, amount, description):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})


  def transfer(self, amount, budget_category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {budget_category.name}")
      budget_category.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False

  def __str__(self):
    output = self.name.center(30, "*") + "\n"
    for item in self.ledger:
      output += f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}\n"
    output += f"Total: {format(self.get_balance(), '.2f')}"
    return output
