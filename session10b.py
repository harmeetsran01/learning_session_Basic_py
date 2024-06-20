#contructor

from sessio10a import FlipkartProduct

class FLipkartProduct:
    def __init__(self):  #contructor #Self could be any name, here self is standard name. which will hold the hashcode of current object
        print("Self", self)
        self.ProductId=1377
        self.Name="HP"
        self.Description="Laptops, PC etc"
        self.RelatedProducts="Dell , Acer"
        self.Review="ABC"

product1=FLipkartProduct()
print(vars(product1))

