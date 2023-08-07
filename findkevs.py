import requests
import sys
import csv
import pandas as pd
from datetime import datetime
import urllib3
from pathlib import Path
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def generate_kev_report(center_token, center_ip):
    center_port = 443
    center_base_url = "api/3.0"
    url = 'https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv'
    r = requests.get(url, allow_redirects=True)
    open('known_exploited_vulnerabilities.csv', 'wb').write(r.content)

    KEVs = []
    kev_titles = []
    kev_summaries = []
    kev_vendors = []

    with open("known_exploited_vulnerabilities.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                KEVs.append(row[0])
                kev_titles.append(row[3])
                kev_summaries.append(row[5])
                kev_vendors.append(row[1])
            line_count += 1

    kev_report = []

    headers = { "x-token-id": center_token }
    r_get = requests.get(f"https://{center_ip}:{center_port}/{center_base_url}/vulnerabilities",headers=headers,verify=False)
    r_get.raise_for_status() #if there are any request errors

    #raw JSON data response
    vulnerabilities = r_get.json()

    for vuln in vulnerabilities:
        if vuln in KEVs:
            kev_report.append((vuln['cve'], vuln['title'], vuln['summary']))

    now = datetime.now()

    current_time = now.strftime("%m-%d-%Y_%H-%M-%S")

    file_name = "Cyber-Vision-KEV-Report_" + current_time + ".html"

    filewriter = open(file_name,"w", encoding="utf-8")

    opening = "<html>\n<head>\n<title> \nKEV Report \
            </title>\n<link rel='stylesheet' href='styles.css'>\n</head> <body><h1>KEVs Found in Your Network</h1>"

    kev_string = "<h3>Identified KEVs on Devices or Components in Your Network</h3>\n"

    if(len(kev_report) == 0):
        kev_string += "<p>No vulnerabilities found</p>"
    else:
        kev_string += "<table>\n<tr>\n<th class='col4'>CVE Id</th>\n<th class='col5'>Title</th>\n<th class='col7'>Summary</th>\n</tr>"
        for vuln in kev_report:
            kev_string += "<tr>\n<td>" + str(vuln[0]) + "</td>\n<td>" + str(vuln[1]) + "</td>\n<td>" + str(vuln[2]) + "</td>\n</tr>\n"
        kev_string += "</table>"

    kev_string += "<br>"

    closing = "</body></html>"

    html_content = opening + kev_string + closing
    
    filewriter.write(html_content)
                
    filewriter.close()

    print("KEV Report in this directory: " + str(Path.cwd()))