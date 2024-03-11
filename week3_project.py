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

# Input values
cost_of_investment = float(input("Enter the cost of investment: $"))
annual_income = float(input("Enter the annual income from the rental property: $"))
annual_expenses = float(input("Enter the annual expenses for the rental property: $"))

# Create an instance of RentalProperty
property1 = RentalProperty(cost_of_investment, annual_income, annual_expenses)

# Calculate ROI
roi = property1.calculate_roi()

# Print the ROI
print(f"\nReturn on Investment (ROI) for the rental property is: {roi:.2f}%")

