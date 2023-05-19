from django.shortcuts import render
import requests
import csv

# Create your views here.
def index(request):
    if request.method == "GET":
        get_devices(request.GET.get("token", ""), request.GET.get("ip", ""))
    return render(request, "index.html")

def get_devices(center_ip, center_token):
    try:
        center_port = 443
        center_base_url = "api/3.0"

        headers = { "x-token-id": center_token }
        r_get = requests.get(f"https://{center_ip}:{center_port}/{center_base_url}/devices",headers=headers,verify=False)
        r_get.raise_for_status() #if there are any request errors

        #raw JSON data response
        raw_json_data = r_get.json()

        write_to_csv(raw_json_data)

    except Exception as e:
        return f"Error when connecting: {e}"

def write_to_csv(devices):
    f = open('./test.csv', 'w', newline='')

    writer = csv.writer(f)

    writer.writerow(["Device Name", "MAC Address", "IP"])

    for device in devices:
        writer.writerow([device["label"], device["mac"][0], device["ip"][0]])

    f.close()