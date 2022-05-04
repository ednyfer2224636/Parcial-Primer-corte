h=int(input("Ingrese la hora: "))
m=int(input("Ingrese los minutos: "))
s=int(input("Ingrese los segundos: "))


if s == 59:
    
    if m == 59:
        s = 0
        m += 1
        
        if h == 23:
            m = 0
            s = 0
            h = 0
            print(h, m, s)
        else:
            m = 0
            s = 0
            h += 1
            print(h, m, s)

    else:
        m += 1
        s = 0
        print(h, m , s)
            
else:
   s += 1
   print(h, m, s) 
            
