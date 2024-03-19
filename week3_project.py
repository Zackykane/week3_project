class RentalProperty:
    def __init__(self, cost_of_investment, annual_income, annual_expenses):
        self.cost_of_investment = cost_of_investment
        self.annual_income = annual_income
        self.annual_expenses = annual_expenses

    def calculate_net_income(self):
        return self.annual_income - self.annual_expenses

    def calculate_roi(self):
        net_income = self.calculate_net_income()
        roi = (net_income / self.cost_of_investment) * 100
        return roi

class PropertyPortfolio:
    def __init__(self):
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

    def calculate_total_roi(self):
        total_roi = 0
        for property in self.properties:
            total_roi += property.calculate_roi()
        return total_roi / len(self.properties)

def main():
    portfolio = PropertyPortfolio()

    while True:
        print("\n1. Add a property")
        print("2. Calculate total ROI")
        print("3. Remove a property")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            cost_of_investment = float(input("Enter the cost of investment: $"))
            annual_income = float(input("Enter the annual income from the rental property: $"))
            annual_expenses = float(input("Enter the annual expenses for the rental property: $"))
            property = RentalProperty(cost_of_investment, annual_income, annual_expenses)
            portfolio.add_property(property)
        elif choice == 2:
            if len(portfolio.properties) == 0:
                print("No properties added yet. Please add a property first.")
        elif choice == 3:
            index = int(input("Enter the index of the property to remove: "))
            if portfolio.remove_property(index):
                print("Property removed successfully.")
            else:
                print("Invalid index. No property was removed.")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()