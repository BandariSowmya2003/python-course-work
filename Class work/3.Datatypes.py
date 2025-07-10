#Data Types
#1.Numeric Types
#a.int
a=15
print(a)
print(type(a))
#b.float
b=1.4
print(b)
print(type(b))
#c.complex
c=3+7j
print(c)
print(type(c))

#2.Sequence Types
#a. str
a="Python Program"
print(a)
print(type(a))
#b. list
cart_items = ["Tops", "T-shirts", "Jeans"]
print(cart_items)
print(type(cart_items))
#c. tuple
warehouse_location= (12.5628, 87.5643)
print(warehouse_location)
print(type(warehouse_location))

#3. Set Types
#a. set
available_sizes = {"S", "M", "L", "XL", "XXL"}
print(available_sizes)
print(type(available_sizes))
#b. frozenzet
frozen_tags = frozenset(["Sale", "Limited Edition", "Trending"])
print(frozen_tags)
print(type(frozen_tags))

#4. Mapping Type
#a. dict
product_details = {"name":"Wireless Mouse", "brand":"Logitech", "price":"900", "rating":"4"}
customer_profile = {"name":"Sowmya Bandari", "Email":"Sowmya@example.com", "prime_member": True}
print(product_details)
print(type(product_details))
print(customer_profile)
print(type(customer_profile))

#5. Boolean type
is_logged_in = True
is_paymet_successful = False
is_in_stock = True
print(is_logged_in)
print(is_paymet_successful)
print(is_in_stock)
print(type(is_logged_in))

#6. None Type
tracking_number = None
delivery_partner = None
print(delivery_partner)
print(type(tracking_number))