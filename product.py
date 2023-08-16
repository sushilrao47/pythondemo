'''

P = 1000
Dis = 15% ( 4000-5000, dis 18%, <5000,1000, dis 12%, else flat 10%)
Off= original price ka 2 per when product price is more then 1000

fine the final of product ?
'''

product_price = float(input("Pls input product price:-"))
product_dis   = float(input("Pls input product discount:-"))
flat_offer   = float(input("Pls input product offer:-"))
discount = product_price*0.20
final_discount = discount+flat_offer
final_product_price= product_price-final_discount
print("Final product price", final_product_price)



####