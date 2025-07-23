# Phone Plan Chooser Application

# Task 1: Take User Preferences and Plan Info as Input

# Getting user input
user_id = int(input("Enter User ID: "))
user_name = input("Enter Your Name: ")
usage_type = input("Enter Usage Type (Talktime/Data/Both): ").capitalize()
monthly_budget = float(input("Enter Monthly Budget (in ₹): "))
preferred_features = input("Enter Preferred Features (comma-separated): ").split(',')
available_plans = input("Enter Available Plans (comma-separated): ").split(',')
plan_selected = input("Enter Selected Plan Name: ")
plan_price = float(input("Enter Selected Plan Price: ₹"))
feature_tags = set(input("Enter Feature Tags of the Plan (comma-separated): ").split(','))
network_provider = {
    "Name": input("Enter Network Provider Name: "),
    "Helpline": input("Enter Provider Helpline Number: "),
    "Coverage Area": input("Enter Main Coverage Area: ")
}

# Task 2: Display Plan Details Using Different Formatting Methods

print("\n--- Phone Plan Chooser Details ---\n")

# 1. Comma Separation
print("User ID, Name, Usage Type:", user_id, user_name, usage_type, sep=', ')

# 2. Percentage Formatting
print("Budget Usage: %.2f%% of Monthly Budget" % ((plan_price / monthly_budget) * 100))

# 3. f-strings
print(f"\nUser: {user_name}")
print(f"Selected Plan: {plan_selected}")
print(f"Plan Price: ₹{plan_price}")
print(f"Usage Type: {usage_type}")
print(f"Preferred Features: {', '.join(preferred_features)}")
print(f"Available Plans: {', '.join(available_plans)}")
print(f"Feature Tags: {', '.join(feature_tags)}")

# 4. .format() method
print("\nNetwork Provider: Name - {}, Helpline - {}, Coverage - {}".format(
    network_provider["Name"],
    network_provider["Helpline"],
    network_provider["Coverage Area"]
))

Enter User ID: 1011
Enter Your Name: Ganavi
Enter Usage Type (Talktime/Data/Both): both
Enter Monthly Budget (in ₹): 300
Enter Preferred Features (comma-separated): Unlimited calls,more data
Enter Available Plans (comma-separated): plan 249,plan299,plan349
Enter Selected Plan Name: plan299
Enter Selected Plan Price: ₹249
Enter Feature Tags of the Plan (comma-separated): VoLTE,Unlimited,4G
Enter Network Provider Name: Jio
Enter Provider Helpline Number: 198
Enter Main Coverage Area: India

--- Phone Plan Chooser Details ---

User ID, Name, Usage Type:, 1011, Ganavi, Both
Budget Usage: 83.00% of Monthly Budget

User: Ganavi
Selected Plan: plan299
Plan Price: ₹249.0
Usage Type: Both
Preferred Features: Unlimited calls, more data
Available Plans: plan 249, plan299, plan349
Feature Tags: 4G, VoLTE, Unlimited

Network Provider: Name - Jio, Helpline - 198, Coverage - India
