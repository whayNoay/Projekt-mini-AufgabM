def bmiRechner():
    bmiverlauf = []  
    anzahl = int(input("Wie viele BMI-Werte möchtest du berechnen? "))  
    
    for i in range(anzahl):
        print(f"Berechnung {i + 1}:")
        gewicht = float(input("Gib dein Gewicht in kg ein: "))
        groesse = float(input("Gib deine Größe in cm ein: "))
        bmi = gewicht / (groesse ** 2)
        bmi = bmi * 10000
        bmiverlauf.append(bmi)  
        print(f"BMI:{bmi:.2f}")
        
    print("\nDeine BMI-Werte:")
    for wert in bmiListe:
        print(f" {wert:.2f}")
    
    

bmiRechner()




