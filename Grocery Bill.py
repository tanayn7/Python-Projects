class store:
    _name = []
    _item_code = []
    _price = []

    def get_data(self):
        for i in range(5):
            self._name.append(str(input("Enter the name of item :")))
            self._item_code.append(int(input("Enter the code of item :")))
            self._price.append(int(input("Enter the price of item :")))

    def display_data(self):
        print("Item name \t Item Code \t Price")
        for i in range(5):
            print(self._name[i],"\t\t",self._item_code[i],"\t\t",self._price[i])

    def calculate_bill(self,quant):
        total_amount=0
        for i in range(5):
            total_amount = total_amount+self._price[i]*quant[i]
        print("************************BILL****************************")
        print("Item name \t Item \t Price \t Quantity \t Subtotal")
        for i in range(5):
            print(self._name[i], "\t\t",self._item_code[i], "\t" ,self._price[i], "\t" ,quant[i], "\t\t" ,quant[i]*self._price[i], "\t")
        print("***********************************************")
        print("Total =", total_amount)


s = store()
s.get_data()
s.display_data()
q =[]
print("Enter the quantity of each item :")
for i in range(5):
    q.append(int(input()))
s.calculate_bill(q)
