class ATM:
    def __init__(self,AtmCardNumber,PinNumber):
        self.AtmCardNumber = AtmCardNumber
        self.PinNumber = PinNumber
        AtmCardNumber = 11111111
        PinNumber = 12345

    def CashWithdraw():
        print('Cash Has been Withdrawn')

    def BalanceEnquiry():
        print('You Have infinte amount of money in your account')
    
    def CashDesposit():
        print('Cash Has been Desposited')
            
def main():
    
    ATM().CashWithdraw()
    ATM().BalanceEnquiry()
    ATM().CashDesposit()

main()
