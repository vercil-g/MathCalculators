# (c) 2025 Vercil Gestiada and Precious Lomod
# C. Concrete Volume Calculation

def main():
    Length = float(input("What is the Length of the sidewalk (m)?"))
    Width = float(input("What is the Width of the sidewalk (m)?"))
    Depth = float(input("What is the Depth of the sidewalk (m)?"))
    
    Volume = Length * Width * Depth
    
    print(f"\nSo, you need {Volume:,.2f} cubic meters of concrete.")
    
if __name__ == "__main__":
 main()