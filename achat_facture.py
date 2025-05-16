import mysql.connector
from datetime import datetime

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="magasin"
)
cursor = conn.cursor()

facture = []
total = 0

while True:
    ref = input("Entrer la référence du produit (ou 'fin' pour terminer) : ")
    if ref.lower() == "fin":
        break
    cursor.execute("SELECT nom, prix FROM produits WHERE reference = %s", (ref,))
    result = cursor.fetchone()
    if result:
        nom, prix = result
        try:
            qte = int(input(f"Quantité de '{nom}' : "))
            sous_total = prix * qte
            total += sous_total
            facture.append(f"{nom} ({ref}) x{qte} = {sous_total:.2f} DH")
        except ValueError:
            print("Quantité invalide.")
    else:
        print("Produit non trouvé.")

cursor.close()
conn.close()

# Sauvegarde dans un fichier texte
date_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nom_fichier = f"facture_{date_now}.txt"

with open(nom_fichier, "w", encoding="utf-8") as f:
    f.write("=== FACTURE ===\n")
    for ligne in facture:
        f.write(ligne + "\n")
    f.write(f"\nTOTAL : {total:.2f} DH\n")

print(f"Facture enregistrée dans le fichier : {nom_fichier}")
