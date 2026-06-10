def values() :
    
    test = input("Do you want a exemple ? y/n")
    if test == "y":
        S0 = 100
        r = 0
        sigma = 0.2
        T = 1
        I = 500
        K = 100
        M = 100
        B = 130
        dt = T/M
        
        return S0,r,sigma,T,I,K,M,B,dt
    else:
        S0 = float(input("S0").strip())
        r = float(input("r").strip())
        sigma = float(input("volatility").strip())
        T = float(input("T").strip())
        I = float(input("I").strip())
        K = float(input("K").strip())
        M = float(input("M").strip())
        B = float(input("B").strip())
        dt = T/M
        return  S0,r,sigma,T,I,K,M,B,dt

