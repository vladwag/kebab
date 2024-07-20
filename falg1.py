from mnemonic import Mnemonic
from bip44 import Wallet
from web3 import Web3

def generate_eth_wallet():
    # Générer une phrase mnémonique (seed phrase)
    mnemo = Mnemonic("english")
    seed_phrase = mnemo.generate(strength=256)

    # Générer le wallet BIP44 à partir de la seed phrase
    wallet = Wallet(seed_phrase)

    # Dériver la clé privée et la clé publique Ethereum (m/44'/60'/0'/0/0)
    private_key, public_key = wallet.derive_account("eth", account=0)

    # Créer l'adresse Ethereum
    web3 = Web3()
    account = web3.eth.account.from_key(private_key)

    # Détails du wallet
    wallet_details = {
        'seed_phrase': seed_phrase,
        'private_key': private_key.hex(),
        'public_key': public_key.hex(),
        'address': account.address
    }

    return wallet_details


# Générer et afficher les détails du wallet
wallet = generate_eth_wallet()
print(f"Seed Phrase: {wallet['seed_phrase']}")
print(f"Private Key: {wallet['private_key']}")
print(f"Public Key: {wallet['public_key']}")
print(f"Address: {wallet['address']}")

"""
Seed Phrase: seven moon suspect patient sudden junk upon snake together supreme life holiday hamster benefit hobby process spice repeat visa connect video brisk midnight sphere
Private Key: 7d74aabb8e667a9493e3cb64b8d18f9fd0e2d3fd5982088fabd53dfb8aec5d17
Public Key: 03a98a211c779ffe6fa82ddae18cb5b30849c53ed91e095a1e36759359f0bc878e
Address: 0x97C6651622857E700A6D8Bc3f6e8Bf2Fd0CC43b9
"""