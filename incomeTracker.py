class Income:
    def __init__(self, source: str, amount: float, type: str = "salary") -> None:
        self.source = source
        self.amount = amount
        self.type = type

    def __str__(self) -> str:
        return f"{self.source}: £{self.amount}"


def get_incomes() -> list:
    incomes = []
    while True:
        source = input("Enter the source of income (type 'done' to finish): ")
        if source.lower() == "done":
            break
        amount = float(input(f"Enter income amount from {source}: "))
        incomes.append(Income(source, amount))
    return incomes


def show_incomes(incomes) -> None:
    for income in incomes:
        print("-" * 30)
        print(f"Source: {income.source}")
        print(f"Amount: {income.amount}")
    print("-" * 30)
    return


def calculate_total_income(incomes) -> float:
    return sum(income.amount for income in incomes)


def check_incomes_correct(incomes) -> bool:
    usr_in = input("Is the above income information correct? (y/n) ")
    if usr_in.lower() == "n":
        return False
    else:
        return True


def edit_entry() -> None:
    print("Which entry do you wish to edit?")

    for index, income in enumerate(incomes):
        print(f"{index + 1}. {income}")
    index = int(input()) - 1
    print(f"You selected {incomes[index]}.")
    print("\nPlease select what you wish to edit.")
    print("1. Edit the entry's source.")
    print("2. Edit the entry's amount.")

    usr_in = input()
    if usr_in == "1":
        incomes[index].source = input("Input source of the entry: ")
    elif usr_in == "2":
        incomes[index].amount = input("Input amount of the entry: ")
    return


if __name__ == "__main__":
    incomes = get_incomes()
    show_incomes(incomes)
    total_income = calculate_total_income(incomes)
    print(f"Total income: £{total_income}")
    while True:
        if check_incomes_correct(incomes) == False:
            edit_entry()
            show_incomes(incomes)
        else:
            print("Successfully Saved Incomes!")
            break
