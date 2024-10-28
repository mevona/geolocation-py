import requests
import tkinter as tk
from tkinter import scrolledtext

def get_geolocation():
    ip_address = ip_entry.get()
    output_text.delete(1.0, tk.END)

    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        data = response.json()

        if 'error' not in data:
            output_text.insert(tk.END, f"IP Address: {data.get('ip', 'N/A')}\n")
            output_text.insert(tk.END, f"City: {data.get('city', 'N/A')}\n")
            output_text.insert(tk.END, f"Region: {data.get('region', 'N/A')}\n")
            output_text.insert(tk.END, f"Country: {data.get('country', 'N/A')}\n")
            output_text.insert(tk.END, f"Location: {data.get('loc', 'N/A')}\n")
            output_text.insert(tk.END, f"ISP: {data.get('org', 'N/A')}\n")
        else:
            output_text.insert(tk.END, f"Error: {data['error']}\n")
    except Exception as e:
        output_text.insert(tk.END, f"An error occurred: {str(e)}\n")

def get_my_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        my_ip = response.json().get('ip', 'N/A')
        ip_entry.delete(0, tk.END)
        ip_entry.insert(0, my_ip)
    except Exception as e:
        output_text.insert(tk.END, f"An error occurred while fetching your IP: {str(e)}\n")

root = tk.Tk()
root.title("IP Geolocation")

ip_label = tk.Label(root, text="Enter IP Address:")
ip_label.pack(pady=10)

ip_entry = tk.Entry(root, width=30)
ip_entry.pack(pady=10)

my_ip_button = tk.Button(root, text="My IP", command=get_my_ip)
my_ip_button.pack(pady=5)

fetch_button = tk.Button(root, text="Get Geolocation", command=get_geolocation)
fetch_button.pack(pady=10)

output_text = scrolledtext.ScrolledText(root, width=50, height=15)
output_text.pack(pady=10)

root.mainloop()
