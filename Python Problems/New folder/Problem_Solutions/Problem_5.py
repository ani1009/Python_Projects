'''
Create a class called "MobilePlan" that represents a mobile plan offered by a telecom company.
The class should have the following features:

● A constructor method that takes the plan name, data allowance, and monthly cost as
parameters and initializes them.
● A method called "check_data_usage" that takes the amount of data used by a customer
as a parameter and determines if it exceeds the data allowance of the plan.
● A method called "display_plan_details" that prints the plan name, data allowance, and
monthly cost.
Write the MobilePlan class and demonstrate its usage by creating an instance of the class,
checking data usage against the plan allowance, and displaying the plan details.
'''

class MobilePlan:
    def __init__(self,plan_name,data_allowance,monthly_cost):
        self.plan_name = plan_name
        self.data_allowance = data_allowance
        self.monthly_cost = monthly_cost

    def check_data_usage(self,data_used):
        if data_used > self.data_allowance:
            return True
        else:
            return False

    def display_plan_details(self):
        print("Plan Name:",self.plan_name)
        print("Data Allowance:",self.data_allowance,"GB")
        print("Monthly Cost: RS.",self.monthly_cost)

bsnl_plan = MobilePlan("Basic Plan",30,141.25)
data_used = 29
#data_used = 32

exceeds_data_allowance = bsnl_plan.check_data_usage(data_used)
bsnl_plan.display_plan_details()

if exceeds_data_allowance:
    print("Data Usage Exceeds the Plan Allowance.")
else:
    print("Data Usage is Within the Plan Allowance.")


