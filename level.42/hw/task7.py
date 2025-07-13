def pop(d):
    d['age'] = 14 
    print("დამატების შემდეგ:", d)
    d.popitem()  
    print("ბოლო წაშლის შემდეგ:", d)
