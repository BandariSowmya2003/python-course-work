class PersonBase:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
    
    def display_info(self):
        raise NotImplementedError("Subclasses must implement display_info()")

from abc import ABC, abstractmethod

# Base class (Abstraction)
class PersonBase(ABC):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    @abstractmethod
    def display_info(self):
        pass


# User class (Encapsulation + Inheritance)
class User(PersonBase):
    total_users = 0  # Class attribute

    def __init__(self, user_id, name, usage_type, monthly_budget, preferred_features):
        super().__init__(user_id, name)
        self.usage_type = usage_type.capitalize()
        self.__monthly_budget = monthly_budget
        self.preferred_features = preferred_features
        self.selected_plan = None
        User.total_users += 1

    def get_budget(self):
        return self.__monthly_budget

    def choose_plan(self, plan):
        self.selected_plan = plan

    def display_info(self):  # Polymorphism
        print(f"\nUser: {self.name} (ID: {self.user_id})")
        print(f"Usage Type: {self.usage_type}")
        print(f"Budget: {self.__monthly_budget}")
        print(f"Preferred Features: {', '.join(self.preferred_features)}")
        if self.selected_plan:
            print(f"Selected Plan: {self.selected_plan.plan_name} (₹{self.selected_plan.get_price()})")


# Plan class
class Plan:
    def __init__(self, plan_name, plan_price, feature_tags, usage_type):
        self.plan_name = plan_name
        self.__plan_price = plan_price
        self.feature_tags = feature_tags
        self.usage_type = usage_type

    def get_price(self):
        return self.__plan_price

    def display_info(self):  # Polymorphism
        print(f"Plan: {self.plan_name} | Price: {self.__plan_price} | Features: {', '.join(self.feature_tags)}")


# Network Provider class
class NetworkProvider:
    def __init__(self, name, helpline, coverage_area):
        self.name = name
        self.helpline = helpline
        self.coverage_area = coverage_area

    def display_info(self):  # Polymorphism
        print(f"Network Provider: {self.name}, Helpline: {self.helpline}, Coverage: {self.coverage_area}")


# Manager Class
class RechargeSystem:
    def __init__(self):
        self.users = []
        self.plans = []

    def register_user(self, user):
        self.users.append(user)

    def add_plan(self, plan):
        self.plans.append(plan)

    @staticmethod
    def compare_plans(user, plans):
        affordable = [p for p in plans if p.get_price() <= user.get_budget()]
        if affordable:
            best = min(affordable, key=lambda x: x.get_price())
            return best
        return None

    def system_report(self):
        print("\n--- System Report ---")
        print(f"Total Users Registered: {len(self.users)}")
        for user in self.users:
            user.display_info()
        print("\nAvailable Plans:")
        for plan in self.plans:
            plan.display_info()


# Sample Data
provider = NetworkProvider("Jio", "198", "India")

plan1 = Plan("Plan 249", 249, ["Unlimited Calls", "1.5GB/day", "VoLTE"], "Both")
plan2 = Plan("Plan 299", 299, ["Unlimited Calls", "2GB/day", "4G"], "Both")
plan3 = Plan("Plan 349", 349, ["More Data", "Roaming Free"], "Data")

system = RechargeSystem()
system.add_plan(plan1)
system.add_plan(plan2)
system.add_plan(plan3)

user1 = User(1011, "Ganavi", "Both", 300, ["Unlimited Calls", "More Data"])
system.register_user(user1)

# Suggest a plan
best_plan = RechargeSystem.compare_plans(user1, system.plans)
if best_plan:
    user1.choose_plan(best_plan)

# Reports
user1.display_info()
provider.display_info()
system.system_report()


#Output:
'''
User: Ganavi (ID: 1011)
Usage Type: Both
Budget: 300
Preferred Features: Unlimited Calls, More Data
Selected Plan: Plan 249 (249)

Network Provider: Jio, Helpline: 198, Coverage: India

--- System Report ---
Total Users Registered: 1

User: Ganavi (ID: 1011)
Usage Type: Both
Budget: 300
Preferred Features: Unlimited Calls, More Data
Selected Plan: Plan 249 (249)

Available Plans:
Plan: Plan 249 | Price: 249 | Features: Unlimited Calls, 1.5GB/day, VoLTE
Plan: Plan 299 | Price: 299 | Features: Unlimited Calls, 2GB/day, 4G
Plan: Plan 349 | Price: 349 | Features: More Data, Roaming Free

'''
