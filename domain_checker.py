# domain_checker.py
import requests

def check_domain_status(domain):
    try:
        response = requests.get(f"http://{domain}")
        if response.status_code == 200:
            return "alive"
        else:
            return "dead"
    except requests.ConnectionError as e:
        # Log the full error message and trace
        print(f"Connection Error: {e}")
        return "Connection Error"