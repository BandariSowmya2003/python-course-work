#Class,Objects,Attributes,Methods
class shopping:
    discount=10
    def __init__(self,name):
        self.name=name
        self.order=[]

    def myorder(self,order):
        self.order.append(order)
        print(f"{self.name}!\nYour {self.order} is successfully placed")

    @classmethod
    def updateDiscount(cls,newdiscount):
        cls.discount=newdiscount
        print(f'\nUpdated discount: {cls.discount}')

    @staticmethod
    def Welcome():
        print("\nWelcome to Meesho.Have a great shopping time.")

Jyothsna=shopping('Jyothsna')
Madhavi=shopping('Madhavi')
Akshaya=shopping('Akshaya')

Jyothsna.myorder('Laptop')
Madhavi.myorder('Saree')
Akshaya.myorder('Handbag')
Jyothsna.myorder('Mobile')
Akshaya.myorder('Headset')


shopping.updateDiscount(15)
shopping.Welcome()

#Output:
'''
Jyothsna!
Your ['Laptop'] is successfully placed
Madhavi!
Your ['Saree'] is successfully placed
Akshaya!
Your ['Handbag'] is successfully placed
Jyothsna!
Your ['Laptop', 'Mobile'] is successfully placed
Akshaya!
Your ['Handbag', 'Headset'] is successfully placed

Updated discount: 15

Welcome to Meesho.Have a great shopping time.

'''
#2.
class shopping:
    def __init__(self,username,phonenumber,password):
        self.username=username
        self.phonenumber=phonenumber
        self.password=password
        self.fav=[]
        self.orders=[]
        self.mycart=[]
        print(f"\nWelcome to Flipcart {self.username}.Enjoy the shopping")


Sowmya=shopping('Sowmya','6726328928','Sowmya@1234')

#Output:
'''
Welcome to Flipcart Sowmya.Enjoy the shopping

'''
