def getBookdetails(bc):
    book1 ={
        "name":"Python Book",
        "Author":"Aasrith",
        "Price": 10000,
        "Catergory":"Programing",
    }
    if bc == 1:
        return book1
    
b1=getBookdetails(1)
print(b1)