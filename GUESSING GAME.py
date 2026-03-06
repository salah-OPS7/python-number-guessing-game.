print("🔮 Je vais deviner ton nombre entre 1 et 100 en 5 essais max !")
input("Pense à un nombre... puis appuie sur Entrée.")

min_val, max_val = 1, 100
essais = 5
while min_val <= max_val:
    essais += 1
    guess = (min_val + max_val) // 2
    print(f"\n👉 Est-ce que c’est {guess} ?")
    reponse = input("[+ pour plus / - pour moins / = pour gagné] : ").strip()

    if reponse == "=":
        print(f"\n🎉 J’ai gagné en {essais} essai(s) !")
        break
    elif reponse == "+":
        min_val = guess + 1
    elif reponse == "-":
        max_val = guess - 1
    else:
        print("⚠️ reponds avec  +, - ou =")
        essais -= 1  # ne compte pas l'erreur
else:
    print("\n🤔 Tu as triché ? Je n’ai pas trouvé...")
    
    
    
    
    



