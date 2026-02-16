import firebase_admin
from firebase_admin import credentials, firestore

# 1. Autenticazione (ormai sei un esperto qui)
if not firebase_admin._apps:
    cred = credentials.Certificate("chiave.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# 2. Chiediamo all'utente cosa vuole scrivere
print("--- BENVENUTO NEL TUO DATABASE CLOUD ---")
nuovo_task = input("Cosa devi fare oggi? ")
priorita = input("Che priorità ha? (Alta/Media/Bassa): ")

try:
    # 3. Salviamo il dato usando l'input dell'utente
    # Usiamo add() invece di set() così ogni volta crea un documento NUOVO
    db.collection("i_miei_task").add({
        "attivita": nuovo_task,
        "priorita": priorita,
        "stato": "da completare"
    })
    print("\n✅ Task salvato correttamente nel Cloud!")
except Exception as e:
    print(f"❌ Errore: {e}")