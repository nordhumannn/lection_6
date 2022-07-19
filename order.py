class NegativeValue(Exception):
    
    def __init__(self, value: str | float = None, msg: str = None):
        super().__init__()
        self.value = value
        self.msg = msg
    
    def __str__(self) -> str:
        return f'{self.value}, {self.msg}'

class Product:

    def __init__(self, title: str, price: int | float):
        if not isinstance(price, int | float):
            raise TypeError()

        if price <= 0:
            raise NegativeValue(price, 'Price attribute must be positive')

        self.title = title
        self.price = price

    def __str__(self) -> str:
        return f'{self.title}, {self.price}'

class Customer:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'

class Order:

    def __init__(self, customer: Customer):
        self.customer = customer
        self.cart = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int | float):
        self.cart.append(product)
        self.quantities.append(quantity)

    def total_price(self):
        total = 0
        for i, item in enumerate(self.cart):
            total += item.price * self.quantities[i]
        return total

    def __str__(self) -> str:
        res = f'Customer: {self.customer}\n\n'
        for i, item in enumerate(self.cart):
            tmp = f'\t{item} UAH * {self.quantities[i]} = {self.quantities[i] * item.price}\n'
            res += tmp

        res += f'\nTotal price: {self.total_price()} UAH'

        return res

    def __getitem__(self, item):
        
        if isinstance(item, slice):
            result = []
            start = item.start or 0
            stop = item.stop or len(self.cart)
            step = item.step or 1

            if start < 0 or step > len(self.cart):
                raise IndexError()

            for i in range(start, stop, step):
                result.append(self.cart[i])
            return result

        if isinstance(item, int):
            if item < len(self.cart):
                return self.cart[item]
                raise IndexError()
            raise TypeError() 

    def __len__(self):
        return len(self.cart)

    def __iter__(self):
        return CartIter(self.cart)

class CartIter:

    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __iter__(self, ):
        return self

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]
        raise StopIteration

pr_1 = Product('Apple', 10)
pr_2 = Product('Banana', 20)
pr_3 = Product('Apple_2', 10)
pr_4 = Product('Banana_2', 20)

cust_1 = Customer('A', 'B')

order_1 = Order(cust_1)
order_1.add_product(pr_1, 1)
order_1.add_product(pr_2, 3)
order_1.add_product(pr_3, 1)
order_1.add_product(pr_4, 4)

print(order_1)
print(order_1[2])
print()

x = order_1[2:]
for item in x:
    print(item)

print()

for item in order_1:
    print(item)
