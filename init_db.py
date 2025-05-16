import mysql.connector

# Connexion à MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = conn.cursor()

# Créer la base de données
cursor.execute("CREATE DATABASE IF NOT EXISTS magasin")
cursor.execute("USE magasin")

# Créer la table produits
cursor.execute("""
CREATE TABLE IF NOT EXISTS produits (
    reference VARCHAR(10) PRIMARY KEY,
    nom VARCHAR(100),
    rayon VARCHAR(50),
    prix FLOAT
)
""")

# Ajouter des produits
produits = [
    ("P001", "Lait", "Alimentaire", 7.5),
    ("P002", "Savon", "Hygiène", 3.2),
    ("P003", "Pâtes", "Alimentaire", 5.0),
    ("P004", "Stylo", "Papeterie", 2.5),
]

cursor.executemany("INSERT IGNORE INTO produits (reference, nom, rayon, prix) VALUES (%s, %s, %s, %s)", produits)

conn.commit()
cursor.close()
conn.close()
print("Base de données initialisée.")
