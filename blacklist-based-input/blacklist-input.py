import requests
import sys
import urllib3
from urllib.parse import urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def decode_admin_hostname(url):
    return


def delete_user():
    return


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
