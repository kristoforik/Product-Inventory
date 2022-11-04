import random, sys, time
def selling_simulator(number):
        minim = number - 10
        maxim = number + 10
        production = random.randint(minim, maxim)
        return production
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.08)
def simulating(self):
        total_sold = 0
        price = self.pprice
        total_manufactured = 0
        man_cost = self.pmancost
        n = 1
        while n < 13:
            manufactured = self.pmonthlyman
            sold = selling_simulator(self.pmonthlyman)
            left_in_stock = (self.pstock + self.pmonthlyman) - sold
            print("Month", n, ':')
            print("|     Manufactured:", manufactured, 'units')
            print("|     Sold:", sold, 'units')
            print("|     Stock:", left_in_stock, 'units')
            total_sold += sold
            total_manufactured += manufactured
            self.pstock = left_in_stock
            n += 1
        net = (total_sold * price) - (total_manufactured * man_cost)
        net1 = round(net, 2)
        print('\033[1mUnits manufactured:\033[96m',total_manufactured, 'units')
        print('\u001b[0m\033[1mUnits sold:\033[96m', total_sold, 'units')
        print('\u001b[0m\033[1mNet Profit:\033[92m', net1, 'CAD\u001b[0m')
        
def check_code(code):
    tcode = str(code)
    chcode = tcode
    while chcode.isnumeric() == False:
        chcode = (input("Enter a valid code: "))
    return chcode
def check_stock(stock):
    tstock = str(stock)
    chstock = tstock
    while chstock.isnumeric() == False:
        chstock = (input("Enter a valid number of units in stock: "))
    return chstock
def check_monthlyman(monman):
    tcode = str(monman)
    chcode = tcode
    while chcode.isnumeric() == False:
        chcode = (input("Enter a valid number of estimated monthly units manufactured: "))
    return chcode
def check_name(name):
    chname = str(name)
    while chname.isalpha() == False:
        chname = input("Enter a valid product name: ")
    return chname
def check_price(price):
    chprice = price
    while True:
        try:
            float(chprice)
            return chprice
        except ValueError:
            chprice = input("Enter a valid product price: ")
def check_cost(cost):
    chcost = cost
    while True:
        try:
            float(chcost)
            return chcost
        except ValueError:
            chcost = input("Enter a valid manufacture cost: ")

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
        print('\u001b[0m Product Code:\u001b[34;1m', self.pcode)
        print('\u001b[0m Product Name:\u001b[34;1m', self.pname)
        print('\u001b[0m\n Sale Price:\u001b[34;1m', self.pprice, '\u001b[0mCAD')
        print(' Manufacture Cost:\u001b[34;1m', self.pmancost, '\u001b[0mCAD')
        print(' In Stock:\u001b[34;1m', self.pstock, '\u001b[0munits')
        print(' Monthly Production:\u001b[34;1m', self.pmonthlyman, '\u001b[0munits')
        print("-------------------------------------------------")
        simulating(self)
        
        '''n = selling_simulator(self.pmonthlyman)
        res = (self.pstock + self.pmonthlyman) - n
        print(self.pstock)
        print(self.pmonthlyman)
        print(n)
        print(res)'''

        return "-------------------------------------------------"
class Application:
    def creating(self):
            pcode = (input("Enter the product code: "))#100-1000
            pcode = int(check_code(pcode))
            pname = (input("Enter the product name: "))#name
            pname = str(check_name(pname))
            pprice = (input("Enter the product sale price: "))#Real number>0
            pprice = float(check_price(pprice))
            pmancost = (input("Enter the product manufacture cost: "))#Real number>0
            pmancost = float(check_cost(pmancost))
            pstock = (input("Enter the product stock level: "))#int>0
            pstock = int(check_stock(pstock))
            pmonthlyman = (input("Enter the estimated monthly units manufactured: "))#int>=0
            pmonthlyman = int(check_monthlyman(pmonthlyman))
            return Product(pcode, pname, pprice, pmancost, pstock, pmonthlyman).description()

product1 = Application()
print_slow("--Welcome To Programming Principles Sample Product Inventory--\n")
time.sleep(1)
start = int(input(("Type [1] to create a product: \n")))
if start == 1:
    product1.creating()


