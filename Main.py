def add():
    print("cool")
class Product:
    def __init__(self, code, name, price, mancost, stock, monthlyman):
        self.pcode = code
        self.pname = name
        self.pprice = price
        self.pmancost = mancost
        self.pstock = stock
        self.pmonthlyman = monthlyman
    def description(self):
        print('The product code is:', self.pcode)
        print('The product name is:', self.pname)
        print('The product price is:', self.pprice)
        print('The product manufacture cost is:', self.pmancost)
        print('The product stock level is:', self.pstock)
        print('The estimated monthly units manufacture is:', self.pmonthlyman)
    def __str__(self):
        #return str(self.pcode) + self.pname + str(self.pprice) + str(self.pmancost) + str(self.pstock) + str(self.pmonthlyman)
        return add()
class Application:
    def creating(self):
        pcode = int(input("Enter the product code: "))#100-1000
        pname = str(input("Enter the product name: "))#name
        pprice = int(input("Enter the product sale price: "))#Real number>0
        pmancost = int(input("Enter the product manufacture cost: "))#Real number>0
        pstock = int(input("Enter the product stock level: "))#int>0
        pmonthlpyman = int(input("Enter the estimated monthly units manufactured: "))#int>=0
        print(Product(pcode, pname, pprice, pmancost, pstock, pmonthlpyman))
product1 = Product(100, 'Ball', 50, 20, 100, 10)
product1.description()