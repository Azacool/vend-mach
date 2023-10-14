from lesson import VendingMachine
class FillingMachine:
    def __init__(self):
        self.columns = {}

    def refillColumn(self, column_number, drink_name, number_of_cans):
        if column_number < 1 or column_number > 4:
            print("Invalid column number. Please choose a column number from 1 to 4.")
            return

        if column_number not in self.columns:
            self.columns[column_number] = {'drink_name': drink_name, 'number_of_cans': number_of_cans}
        else:
            self.columns[column_number]['drink_name'] = drink_name
            self.columns[column_number]['number_of_cans'] = number_of_cans

    def availableCans(self):
        total_cans = sum(column['number_of_cans'] for column in self.columns.values())
        return total_cans

filling_machine = FillingMachine()

filling_machine.refillColumn(1, "Coca Cola", 1)
filling_machine.refillColumn(2, "Water", 10)
filling_machine.refillColumn(3, "Pepsi", 15)
filling_machine.refillColumn(4, "Water", 20)

total_cans = filling_machine.availableCans()
print(f"Total available cans in the machine: {total_cans}")
