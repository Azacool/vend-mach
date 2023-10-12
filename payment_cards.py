from lesson import VendingMachine
def rechargeCard(self, card_id, credit):
        if not isinstance(credit, (int, float)) or credit <= 0:
            print("Invalid credit amount. Please enter a positive number for the credit.")
            return

        if card_id in self.cards:
            self.cards[card_id] += credit
            print(f"Card {card_id} has been recharged with {credit} credits. Total credit: {self.cards[card_id]}")
        else:
            self.cards[card_id] = credit
            print(f"New card {card_id} has been issued with {credit} credits.")

def getCredit(self, card_id):
        return self.cards.get(card_id, -1.0)


vending_machine = VendingMachine()


vending_machine.rechargeCard(12, 12000)
vending_machine.rechargeCard(21, 5600)
vending_machine.rechargeCard(99, 15800)

card_id = 12
credit = vending_machine.getCredit(card_id)
if credit != -1.0:
    print(f"Card {card_id} has {credit} credits.")
else:
    print(f"Card {card_id} is not available.")

card_id = 42 
credit = vending_machine.getCredit(card_id)
if credit != -1.0:
    print(f"Card {card_id} has {credit} credits.")
else:
    print(f"Card {card_id} is not available.")