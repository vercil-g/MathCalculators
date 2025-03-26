# (c) 2025 Vercil Gestiada and Precious Lomod
# B. Material Strength Calculation for Steel

def main():
    Yield_Force = float(input("What is the Force applied to the beam (N)?"))
    Area = float(input("What is the cross-sectional area of the beam (mm2)?"))
    conversion = Area / 1000000 
    
    Yield_Stress = Yield_Force / Area
    
    print(f"\nSo, the stress on the beam is {Yield_Stress:,.2f} Pa.")
    
if __name__ == "__main__":
 main()