#Railway Ticket
while True:
    def railway():
        ticket_price=1000
        gender=int(input('''Select your Gender:
                          1.Male
                          2.Female'''))
        
        if gender==1:
            age=int(input("Enter your age:"))
            if age>=60:
                discount=ticket_price*(30/100)
                total_ticket_price=ticket_price-discount
                print(total_ticket_price)
            else:
                total_ticket_price=ticket_price
                print(total_ticket_price)
        elif gender==2:
            age=int(input("Enter your age:"))
            if age>=60:
                discount=ticket_price*(50/100)
                total_ticket_price=ticket_price-discount
                print(total_ticket_price)
            else:
                discount=ticket_price*(30/100)
                total_ticket_price=ticket_price-discount
                print(total_ticket_price)
    railway()
