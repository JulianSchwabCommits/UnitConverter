def convert_distance(value, input_unit, output_unit):
    # Umrechnungsfaktoren (basierend auf Meter)
    conversion_factors = {
        "meter": 1,
        "kilometer": 1000,
        "elefant": 6,  # Ein durchschnittlicher Elefant ist etwa 6 Meter lang
        "feet": 0.3048,  # 1 Fuß = 0,3048 Meter
        "gold_nugget": 0.02,  # Ein Goldnugget ist etwa 2cm lang
        "american_eagle": 0.76  # Flügelspannweite eines Weißkopfseeadlers ≈ 76cm
    }
    
    # Emoji-Zuordnung
    unit_emojis = {
        "meter": "📏",
        "kilometer": "🗺️",
        "elefant": "🐘",
        "feet": "👣",
        "gold_nugget": "💎",
        "american_eagle": "🦅"
    }
    
    # Umrechnung in Meter
    meters = value * conversion_factors[input_unit]
    
    # Umrechnung in Zieleinheit
    result = meters / conversion_factors[output_unit]
    
    return f"{result:.2f} {unit_emojis[output_unit]}"

def main():
    print("🔄 Einheitenumrechner 🔄")
    print("\nVerfügbare Einheiten:")
    print("- meter 📏")
    print("- kilometer 🗺️")
    print("- elefant 🐘")
    print("- feet 👣")
    print("- gold_nugget 💎")
    print("- american_eagle 🦅")
    
    try:
        value = float(input("\nBitte geben Sie den Wert ein: "))
        input_unit = input("Eingabeeinheit: ").lower()
        output_unit = input("Zieleinheit: ").lower()
        
        result = convert_distance(value, input_unit, output_unit)
        print(f"\nErgebnis: {value} {input_unit} = {result}")
        
    except ValueError:
        print("❌ Fehler: Bitte geben Sie eine gültige Zahl ein!")
    except KeyError:
        print("❌ Fehler: Ungültige Einheit! Bitte wählen Sie aus den verfügbaren Einheiten.")

if __name__ == "__main__":
    main()
