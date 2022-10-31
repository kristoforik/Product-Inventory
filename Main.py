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
        time.sleep(0.1)
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
            pcode = int(input("\u001b[0m\nEnter the product code: "))#100-1000
            pname = (input("Enter the product name: "))#name
            pprice = float(input("Enter the product sale price: "))#Real number>0
            pmancost = float(input("Enter the product manufacture cost: "))#Real number>0
            pstock = int(input("Enter the product stock level: "))#int>0
            pmonthlpyman = int(input("Enter the estimated monthly units manufactured: "))#int>=0
            return Product(pcode, pname, pprice, pmancost, pstock, pmonthlpyman).description()


'''class Application1:
    def creating(self):
            def getCode():
                pcode = (input("Enter the product code: "))#100-1000
                return pcode
            def getName():
                iname = (input("Enter the product name: "))
                pname = iname
                for i in pname:
                    #while ord(i) < 65 or ord(i) > 90 and ord(i) < 97 or ord(i) > 122:
                    while ord(i)<80:
                        print('cool')
            pprice = float(input("Enter the product sale price: "))#Real number>0
            
            pmancost = float(input("Enter the product manufacture cost: "))#Real number>0
            
            pstock = int(input("Enter the product stock level: "))#int>0
            
            pmonthlpyman = int(input("Enter the estimated monthly units manufactured: "))#int>=0
            getCode()
            getName()'''
            #return Product(pcode, pname, pprice, pmancost, pstock, pmonthlpyman).description()




product1 = Application()
product2 = Product(100, 'BALL', 49.99, 19.99, 100, 100)
print_slow("--Welcome To Programming Principles Sample Product Inventory--\n")
time.sleep(1)
start = int(input(("Type [1] to create a product: ")))
if start == 1:
    product1.creating()


