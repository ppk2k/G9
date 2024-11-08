import requests
from stem import Signal
from stem.control import Controller

# Fungsi untuk terhubung ke Tor
def connect_to_tor():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()  # Autentikasi ke Tor
            controller.signal(Signal.NEWNYM)  # Meminta identitas baru
            print("Terhubung ke jaringan Tor dengan identitas baru.")
    except Exception as e:
        print(f"Gagal terhubung ke Tor: {e}")

# Mengakses situs .onion
def access_onion_site():
    session = requests.session()
    session.proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}

    try:
        response = session.get("http://example.onion")  # Ganti dengan alamat .onion yang valid
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Gagal mengakses situs .onion: {e}")

if __name__ == "__main__":
    connect_to_tor()
    access_onion_site()
