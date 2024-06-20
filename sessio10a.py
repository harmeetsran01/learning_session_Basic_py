"""
Principal of OOPS:
    1. Think of an object

    FlipkartProduct:
        ProductID, ProductName, ProductImage, Description, RelatedProducts, Review

# """
# 2. Create class of object
# Below classs represents the object

class FlipkartProduct:
    pass #the remain the container use as empty 

product1 = FlipkartProduct()  #it is not an object. It's a reference. Object is created at hashcode of reference

#Write operation:

product1.ProductID = 13771
product1.Name="HP_Laptop"
product1.ProductImage = "null"
product1.Description= "SSD: 1 TB\n16GB Ram\n...."
product1.RelatedProducts = "Dell_laptop, Acer_Laptop"
product1.Review= ["abc", "yxz"]

print(vars(product1)) #Read Operation

print()

#Updating Operation

product1.ProductID = 100012
product1.Name="Water_Bottle"

print(vars(product1))  #Read Operation

product2 = product1 # reference copy, hashcode copy










