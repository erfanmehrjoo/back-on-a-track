# collect email from user
# split email using the @ , fist par tas the username , secounf part is gonna be as domain
# spilit domain using . , 
def main():
    print("welcome to email slicer ")
    print(" ")
    
    email_input = input("input your email address: ")
    
    (user_name , domain) = email_input.split("@")
    (domain , extions) = domain.split(".")
    
    print("Username: " , user_name)
    print("Domain :" , domain)
    print("Extions: " , extions)

while True: 
    main()

