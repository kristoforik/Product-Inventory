
class Product:
    def __init__(self, code, name, price, mancost, stock, monthlyman):
        self.pcode = code
        self.pname = name
        self.pprice = price
        self.pmancost = mancost
        self.pstock = stock
        self.pmonthlyman = monthlyman
    def description(self):
        print("-------------------------------------------------")
        print('The product code is:', self.pcode)
        print('The product name is:', self.pname)
        print('The product price is:', self.pprice)
        print('The product manufacture cost is:', self.pmancost)
        print('The product stock level is:', self.pstock)
        print('The estimated monthly units manufacture is:', self.pmonthlyman)
        return "-------------------------------------------------"
class Application:
    def creating(self):
        pcode = int(input("Enter the product code: "))#100-1000
        pname = str(input("Enter the product name: "))#name
        pprice = int(input("Enter the product sale price: "))#Real number>0
        pmancost = int(input("Enter the product manufacture cost: "))#Real number>0
        pstock = int(input("Enter the product stock level: "))#int>0
        pmonthlpyman = int(input("Enter the estimated monthly units manufactured: "))#int>=0
        return Product(pcode, pname, pprice, pmancost, pstock, pmonthlpyman).description()
product1 = Application()
product1.creating()