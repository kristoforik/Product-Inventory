
class Product:
    def __init__(self, code, name, price, mancost, stock, monthlyman):
        self.pcode = code
        self.pname = name
        self.pprice = price
        self.pmancost = mancost
        self.pstock = stock
        self.pmonthlyman = monthlyman
    def __str__(self):
        return self.pcode + self.pname + self.pprice + self.pmancost + self.pstock + self.pmonthlyman


class Application:
    def creating(self):
        pcode = int(input("Enter the product code: "))#100-1000
        pname = str(input("Enter the product name: "))#name
        pprice = int(input("Enter the product sale price: "))#Real number>0
        pmancost = int(input("Enter the product manufacture code: "))#Real number>0
        pstock = int(input("Enter the product stock level: "))#int>0
        pmonthlpyman = int(input("Enter the estimated monthly units manufactured: "))#int>=0
        return Product(pcode, pname, pprice, pmancost, pstock, pmonthlpyman)
