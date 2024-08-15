# Server-Side Request Forgery (SSRF)

This repository is dedicated to exploring Server-Side Request Forgery (SSRF) vulnerabilities, providing examples of common SSRF attacks and payloads, and offering strategies for prevention. This learning path is inspired by content from [web-security-academy.net](https://portswigger.net/web-security) and [Rana Khalil](https://ranakhalil.com/), and it aims to enhance your understanding of SSRF.

## Introduction to SSRF

Server-Side Request Forgery (SSRF) is a security vulnerability that allows an attacker to make requests from the server-side application to internal or external services. The attacker manipulates the server to send crafted requests, which can lead to unauthorized access to internal systems, data exfiltration, or further exploitation of the network.

## Common SSRF Attack Scenarios

1. **Accessing Internal Services**: An attacker uses SSRF to interact with internal services that are not exposed to the public, such as databases, cloud metadata services, or admin panels.
2. **Bypassing Firewalls**: An attacker can bypass firewall rules by sending requests from the vulnerable server to restricted network locations.
3. **Enumerating Internal Networks**: An attacker exploits SSRF to discover internal network infrastructure by probing different IP addresses and ports.
4. **Data Exfiltration**: An attacker leverages SSRF to extract sensitive data from internal systems or third-party services.

## Example Payloads

### Accessing Internal Services

```bash
# HTTP request crafted by an attacker to access an internal service
GET /fetch?url=http://127.0.0.1:8080/admin HTTP/1.1
Host: vulnerable-website.com
```
