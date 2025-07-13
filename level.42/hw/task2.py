def modifyset(s):
    s.add(1)
    s.add(2)       
    s.add(3)
    s.remove(2)    
    return s

print(modifyset({10, 20}))