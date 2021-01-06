m1=float(input("Enter the mass of first object (kg): "))
m2=float(input("Enter the mass of second object (kg): "))
r=float(input("Enter the distance between the center of the masses (m): "))
G=6.673*(10**-11) #value of gravitational constant(G)
F=(G*m1*m2)/(r**2) #formula for calculating gravitational force
print("The Gravitational Force acting between two objects is:",round(F,3),"N")