
import requests
def get_public_ip(): 
    try: 
        response = requests.get('https://api.ipify.org') 
        if response.status_code == 200: 
            return response.text 
        else: 
            return "Error: Unable to retrieve public IP address" 
    except Exception as e: 
        return f"Error: {e}" 
 
# Example usage 
public_ip = get_public_ip() 
print("Your public IP address is:", public_ip) 
