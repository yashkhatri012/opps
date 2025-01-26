class chatbook:
    def __init__(self):
        self.username= ''
        self.password=''
        self.loggedin= False
        self.menu()
    
    def menu(self):
        user_input = input("""Welcome to chatbook, How would you like to procced?
                           1.Press 1 to signup
                           2.Press 2 to signin
                           3.Press 3 to Write a post
                           4.Press 4 to msg a friend
                           5.Press any other key to exit""")
        if user_input== "1":
            pass
        elif user_input== "2":
            pass
        elif user_input== "3":
            pass
        elif user_input== "4":
            pass
        else:
            exit()




obj= chatbook()
