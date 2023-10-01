# collect the necessary input : principal , apr , years 
# calculate the monthly payment 
# show that to user

def main():
    print("This is monthly payment loan calculator")
    print("")
    
    
    principal = float(input("Enter the principal amount : "))
    apr = float(input("Enter the annual percentage rate : "))
    years = int(input("Enter the number of years : "))
    
    
    monthly_payment = calculate_monthly_payment(principal, apr, years)
    
    
    print("")
    print("The monthly payment is : ", monthly_payment)
    
    
def calculate_monthly_payment(principal, apr, years):
    monthly_rate = apr / 12 / 100
    
    
    monthly_payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** (-years * 12))
    
    
    return monthly_payment
    
    
main()