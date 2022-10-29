import random
def selling_simulator(number):
        minim = number - 10
        maxim = number + 10
        production = random.randint(minim, maxim)
        return production

def simulating(self):
        n = 1
        while n < 13:
            manufactured = self.pmonthlyman
            sold = selling_simulator(self.pmonthlyman)
            left_in_stock = (self.pstock + self.pmonthlyman) - sold
            print("Month", n, ':')
            print("     Manufactured:", manufactured, 'units')
            print("     Sold:", sold, 'units')
            print("     Stock:", left_in_stock, 'units')
            self.pstock = left_in_stock
            n += 1
        
class Product:
    def __init__(self, code, name, price, mancost, stock, monthlyman):
        self.pcode = code
        self.pname = name
        self.pprice = price
        self.pmancost = mancost
        self.pstock = stock
        self.pmonthlyman = monthlyman
    def description(self):
        print("\n--Programming Principles Sample Stock Statement--\n")
        print('\u001b[0m Product Code:\033[92m', self.pcode)
        print('\u001b[0m Product Name:\033[92m', self.pname)
        print('\u001b[0m\n Sale Price:\033[92m', self.pprice, '\u001b[0mCAD')
        print(' Manufacture Cost:\033[92m', self.pmancost, '\u001b[0mCAD')
        print(' In Stock:\033[92m', self.pstock, '\u001b[0munits')
        print(' Monthly Production:\033[92m', self.pmonthlyman, '\u001b[0munits')
        print("-------------------------------------------------")

        
        '''n = selling_simulator(self.pmonthlyman)
        res = (self.pstock + self.pmonthlyman) - n
        print(self.pstock)
        print(self.pmonthlyman)
        print(n)
        print(res)'''

        return "-------------------------------------------------"
class Application:
    def creating(self):
        pcode = int(input("\u001b[0mEnter the product code: "))#100-1000
        pname = str(input("Enter the product name: "))#name
        pprice = float(input("Enter the product sale price: "))#Real number>0
        pmancost = float(input("Enter the product manufacture cost: "))#Real number>0
        pstock = int(input("Enter the product stock level: "))#int>0
        pmonthlpyman = int(input("Enter the estimated monthly units manufactured: "))#int>=0
        return Product(pcode, pname, pprice, pmancost, pstock, pmonthlpyman).description()
product1 = Application()
product2 = Product(100, 'BALL', 50, 20, 100, 100)
simulating(product2)
'''start = ("Enter [1] to create a product: ")
if start == 1:
    product1.creating()'''