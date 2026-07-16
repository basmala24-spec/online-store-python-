class reservation :
    def __init__(self,name,phone,date,guest_number,table_number):
        self.name=name
        self.phone=phone
        self.date=date
        self.guest_number=guest_number
        self.table_number=table_number
        self.reserv=True

    def __str__(self):
        status='reserved' if self.reserv else 'not reserved'
        return( f'reservation for: {self.name}\n'
            f'phone: {self.phone}\n'
            f'date: {self.date}\n'
            f'guest_number: {self.guest_number}\n'
            f'table_number: {self.table_number}\n'
            f'status: {status}')
    
class system:
    def __init__(self):
        self.reservations=[]

    def new_reservation(self,reserv):
        self.reservations.append(reserv)

        with open ('reservation.txt','a')as file:
            file.write(str(reserv)+'\n')
            file.write('-'*20+'\n')

        print(f'table {reserv.table_number} is reserved for {reserv.name}')

    def cancel_reservation(self,namer):
        self.reservations=[r for r in self.reservations if r.name!=namer]


        updated=[]


        
        try:
            with open ('reservation.txt','r')as file:
                lines=file.readlines()

                skip=False
                for line in lines:
                    if skip:
                        skip=False
                        continue
                    if f'reservation for {namer}' in line:
                        skip=True
                        continue
                    updated.append(line)
            with open ('reservation.txt','w')as file:
                file.writelines(updated)
            print(f'{namer}s reservations has been removed')
        except FileNotFoundError:
            print('file not found')


    def reservation_flow(self):
        
        while True:
            print("\n--- Reservation Menu ---")
            print("1. Add Reservation")
            print("2. Cancel Reservation")
            print("3. Exit")

            choice = input("Choose option: ")

       
            if choice == "1":
                try:
                    name = input('enter your name: ')
                    phone = int(input('enter your phone number: '))
                    date = input('enter the date: ')
                    guestnum = int(input('how many guests: '))
                    tablenum = int(input('enter table number: '))
                except ValueError:
                    print('invalid input, please try again')
                    continue

                r = reservation(name, phone, date, guestnum, tablenum)
                self.new_reservation(r)

            
            elif choice == "2":
                remove_reserv = input('enter name to cancel reservation: ')
                self.cancel_reservation(remove_reserv)

            
            elif choice == "3":
                print("Exiting reservation system...")
                break

            else:
                print("Invalid option!")

if __name__ == "__main__":
    s=system()
    s.reservation_flow()