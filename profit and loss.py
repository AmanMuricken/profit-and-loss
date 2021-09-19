def profit(costPrice,sellPrice):
    p=sellPrice-costPrice
    return p
def loss(costPrice,sellPrice):
    l=costPrice-sellPrice
    return l
if __name__=="__main__":
    costPrice=int(input("Enter the cost price:"))
    sellPrice=int(input("Enter the selling price:"))
    if(costPrice==sellPrice):
        print("No Profit No Loss")
    elif(sellPrice>costPrice):
        print("Rs.",profit(costPrice,sellPrice),"is the profit")
    else:
        print("Rs.",loss(costPrice,sellPrice),"is the loss")