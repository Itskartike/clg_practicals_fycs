def TowerOfHonoi(n,from_rod,to_rod,aux_rod):
    if n==0:
        return
    TowerOfHonoi(n-1,from_rod,aux_rod,to_rod)
    print("Move disc",n,"From rod",from_rod,"To rod",to_rod)
    TowerOfHonoi(n-1,aux_rod,to_rod,from_rod)

 #Driver Code
N=3

#A,C,B are the name of rods
TowerOfHonoi(N,'A','C','B')




          
