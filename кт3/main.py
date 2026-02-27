def parsing(filename):
    res = []
    
    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
        
        header = lines[0]
        for line in lines[1:]:
            line = line.strip() 
            parts = line.split('|') 

            parts[3] = int(parts[3])
            parts[4] = float(parts[4])
            
            res.append(parts)
    
    return res

def bookfinder(books, keyword):
    res = []
    
    for book in books: 
        if keyword.lower() in book[1].lower():
            new_item = [
                book[0],                       
                book[1] + ", " + book[2],   
                book[3],                       
                book[4]                        
            ]
            res.append(new_item)
    
    return res

def counter(books):
    res = []
    
    for book in books:
        isbn = book[0]
        total = book[2] * book[3] 
        res.append((isbn, total))
    
    return res

books = parsing("books.csv")
filtered = bookfinder(books, "Python")
totals = counter(filtered)

print(totals)