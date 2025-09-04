data={
    12345:{'pin':123,'balance':5000,'history':[]},
    23456:{'pin':123,'balance':5000,'history':[]},
    34567:{'pin':123,'balance':5000,'history':[]},
    45678:{'pin':123,'balance':5000,'history':[]},
    56789:{'pin':123,'balance':5000,'history':[]}
}

def Welcome():
    print('Welcome to ATM'.center(40,'*'))
    
def Menu():
    print('\n[C]heck_Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew History')
    print('[E]xit\n')

def Login():
    account_number=int(input("Enter the account number: "))
    pin=int(input("Enter the pin: "))
    global acc_num
    if account_number in data:
        if data[account_number]['pin']==pin:
            acc_num=account_number
            return True
        else:
            print("Invalid pin")
            return False
    else:
        print("Invalid account number")
        return False
              
def Check_Balance():
    if acc_num:
        print(f'\nCurrent Balance: {data[acc_num]["balance"]}')
    else:
        print("You need to login again")

def Deposit():
    if acc_num:
        amount=int(input("Enter the amount to Deposit: "))
        data[acc_num]['balance']+=amount
        data[acc_num]['history'].append(f'Deposited: ${amount}')
        print(f'${amount} is successfully Deposited!!!')
    else:
        print("You need to login again")
    
def Withdraw():
    if acc_num:
        amount=int(input("Enter the amount to withdraw: "))
        if data[acc_num]['balance']>=amount:
            data[acc_num]['balance']-=amount
            data[acc_num]['history'].append(f'Withdraw: ${amount}')
            print(f'${amount} is successfully Withdraw!!!')
        else:
            print('Insufficient Balance')
    else:
        print("You need to login again")
        

def View_History():
    if acc_num:
        if data[acc_num]['history']:
            print('Transaction History'.center(50,'-'))
            for i in data[acc_num]['history']:
                print(i)
            else:
                print("End of the history".center(50,'-'))
        else:
            print("No Transactions")
    else:
        print("You need to login again")

