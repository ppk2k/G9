import requests
import time
import logging
from stem import Signal
from stem.control import Controller

# Setup logging
logging.basicConfig(filename='logs/tor_connection.log', level=logging.DEBUG)

# Function to connect to Tor
def connect_to_tor():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            time.sleep(5)
        logging.info("Successfully connected to Tor network.")
    except Exception as e:
        logging.error(f"Error connecting to Tor: {e}")
        raise

# Function to access .onion site
def access_onion_site(url):
    try:
        session = requests.Session()
        session.proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
        response = session.get(url, timeout=10)
        return response.text
    except requests.exceptions.Timeout:
        logging.error(f"Timeout while accessing {url}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed for {url}: {e}")
        return None

# Main execution
if __name__ == "__main__":
    connect_to_tor()
    onion_url = "http://example.onion"  # Replace with actual .onion URL
    page_content = access_onion_site(onion_url)
    if page_content:
        logging.info(f"Page content from {onion_url}: {page_content[:100]}...")  # Log first 100 chars
