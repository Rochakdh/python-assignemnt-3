import csv
class Acedamy:

    @staticmethod
    def cource():
        list_cource=['Python','JS','PHP','JAVA','Deno']
        return list_cource

    def inquire(self,check_cource):
        if check_cource in self.cource():
            return True
        else:
            return False
    
    def register(self,data_collect):
        print(data_collect)
        with open('profile.csv','w', newline='') as file:
            writer=csv.writer(file)
            writer.writerow(['Name', 'Cource'])
            writer.writerow([data_collect[0],data_collect[1]])
            

            

        
        




if __name__ == "__main__":
    while True:
        print('-----------------------------------------------------')
        print('Press 1 to view cource of study')
        print('Press 2 to inquire about cource')
        print('Press 3 to register for the cource')
        print('press 4 Display Student Record')
        print('press 5 to update student information')
        print('press 6 to student depoites')
        print('preess q to quit')
        print('-----------------------------------------------------')
        print('\n')
        take_ip=input('Choose Option')
        if take_ip=='1':
            obj=Acedamy()
            list_check=obj.cource()
            print('Cources Available are')
            for each in list_check:
                print(each)
        elif take_ip=='2':
            inquire_cource = input('Enter the Cource')
            obj=Acedamy()
            check = obj.inquire(inquire_cource)
            if check:
                print('Yes! this cource is available')
            else:
                print("No! not in the cource")
        elif take_ip=='3':
            print('---------------')
            print('register')
            print('---------------')
            name = input('Enter your Name')
            cource = input('Enter cource')
            register_data=(name,cource)
            obj=Acedamy()
            if cource in obj.cource():
                obj.register(register_data)
                print('Registration Successful')
            else:
                print('Sorry this cource is not available')



        elif take_ip=='4':
            pass
        elif take_ip=='5':
            pass
        elif take_ip=='6':
            pass
        elif take_ip=='q':
             break;
        else:
            print('invalid input')
    print('Tnak YOu See YOu SOON')




