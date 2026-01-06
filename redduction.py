try:
    prix_initial = float(input("Prix du produit (€) : "))
except ValueError:
    print("Saisie invalide pour le prix.")
    exit(1)

statut = input("Êtes-vous étudiant ? (o/n) : ").strip().lower()
fidelite_str = input("Fidélité (en années) : ").strip()

try:
    fidelite = int(fidelite_str)
except ValueError:
    print("Saisie invalide pour la fidélité.")
    exit(1)

reduction = 0.0

if statut == "o":
    reduction += prix_initial * 0.10


if fidelite >= 5:
    reduction += prix_initial * 0.15


if prix_initial > 100:
    reduction += 5.0


prix_final = prix_initial - reduction


if prix_final < 0:
    prix_final = 0.0

print("-" * 30)
print(f"Réduction totale : {reduction:.2f} €")
print(f"Prix final à payer : {prix_final:.2f} €")