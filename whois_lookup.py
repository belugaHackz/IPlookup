import whois
import whois
import requests

def get_geolocation(ip_address):
    try:
        # Use ipstack API c59ebf0320f9ed99cfe13911ec5cd77f
        api_key = "c59ebf0320f9ed99cfe13911ec5cd77f"
        url = f"http://api.ipstack.com/{ip_address}?access_key={api_key}"
        response = requests.get(url)
        data = response.json()
        return data.get("city"), data.get("country_name")
    except Exception as e:
        print(f"Error fetching geolocation: {e}")
        return None, None

def get_whois_and_geolocation(ip_address):
    try:
        domain_info = whois.whois(ip_address)
        print("Domain:", domain_info.domain)
        print("Registrar:", domain_info.registrar)
        print("Creation Date:", domain_info.creation_date)
        print("Expiration Date:", domain_info.expiration_date)
        print("Name Servers:", domain_info.name_servers)
        print("WHOIS Server:", domain_info.whois_server)
        print("Updated Date:", domain_info.updated_date)

        # Get geolocation details
        city, country = get_geolocation(ip_address)
        if city and country:
            print(f"City: {city}")
            print(f"Country: {country}")
        else:
            print("Geolocation details not available.")
    except whois.parser.PywhoisError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ip_address = input("Enter an IP address: ")
    get_whois_and_geolocation(ip_address)
