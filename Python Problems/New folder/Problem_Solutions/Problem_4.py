'''
Create a class called "InsurancePolicy" that represents an insurance policy in an insurance
company.
The class should have the following features:
● A constructor method that takes the policy holder's name, policy number, and premium
amount as parameters and initializes them.
● A method called "calculate_premium" that calculates and returns the premium amount
for the policy based on the policy type and other factors.
● A method called "display_policy_info" that prints the policy holder's name, policy number,
and premium amount.
Write the InsurancePolicy class and demonstrate its usage by creating an instance of the class,
calculating the premium amount, and displaying the policy information.
'''

class InsurancePolicy:
    def __init__(self,name,policy_number,premium_amount):
        self.name = name
        self.policy_number = policy_number
        self.premium_amount = premium_amount

    def calculate_premium(self,policy_type,other_factors):
        base_premium = 100
        if policy_type == "Auto":
            premium = base_premium + (other_factors * 10)
        elif policy_type == "Home":
            premium = base_premium + (other_factors * 5)
        else:
            premium = base_premium
        return premium

    def display_policy_info(self):
        print("Policy Holder's Name:",self.name)
        print("Policy Number:",self.policy_number)
        print("Premium Account:",self.premium_amount)

policy_holder_name = "Aniket Ugale"
policy_number = "ABXYC123"
premium_amount = 200

policy = InsurancePolicy(policy_holder_name, policy_number, premium_amount)

policy_type = "Auto"
other_factors = 3

calculated_premium = policy.calculate_premium(policy_type, other_factors)

policy.display_policy_info()
print("Calculated Premium Amount:", calculated_premium)

