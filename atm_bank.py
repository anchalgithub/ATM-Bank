print("Welcome to RBC")

class bank:
    def __init__(self,cardNo,name):
        self.cardNo=cardNo
        self.name=name
    
    def integers(self):
         print("Please choose your transaction:")
         print("1) Withdrawal 2)Deposit  3)Balance Inquiry 4) Transfers")
         activity=int(input("Enter activity number: "))
         if(activity==1):
            print("How much would you like to withdrawal:")
            print("1) $50 2) $100 3) $150 4) $200 5) $250")
            answerV=(input("Please put your choice down here: "))
            print("Thank you for working with RBC")
    

         elif(activity==2): 
            print("How much would you like to deposit:")
            print("1) $50 2) $100 3) $150 4) $200 5) $250")
            answerV=(input("Please put your choices down here: "))
            print("Thank you for working with RBC")


         elif(activity==3):
            print("You have $4000 in your account")
            
         elif(activity==4):   
              answerV=(input("Enter the card number to which you would like to transfer money: "))
              answerV2=(input("How much money would you like to transfer: "))
              print("You have just transfered "+answerV2)
    
def main():
    name=input("Enter name: ")
    card_number=input("Insert card number: ")
    print("Welcome "+name+"!")
    new_user=bank(card_number, name)

    if card_number.strip().isdigit():
        new_user.integers()
        
    else:
        print("Please only enter numbers!")
        card_number=input("Insert card number: ")
        if card_number.strip().isdigit():
            new_user.integers()

    
if __name__=="__main__":
    main()