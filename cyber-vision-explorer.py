import mccast, credvarseparated, credvar, findkevs, securitydetails, securityinsights
import sys
import time

print("Welcome to the Cyber Vision Explorer")
print(" ")
print("Please enter your credentials below")
print(" ")

center_token = input("Please enter your Cyber Vision API Token: ")
center_ip = input("Please enter your Cyber Vision IP Address: ")
print(" ")

print("Here are the different reports we can generate:")
print(" ")
print("1: Credentials and Variables Report (non-separated)")
print("2: Credentials and Variables Report (where the device and component values are in separate sheets)")
print("3: KEV (Known Exploited Vulnerability) Report")
print("4: MCCAST Inventory Report")
print("5: Security Insights Report")
print("6: Security Insights with Component Details Report")
print("7: Exit program")
print("8: Display options again")
print(" ")

choice = int(input("Please input which report you'd like to generate: "))

while choice != 7:
    if choice == 8:
        print("Welcome to the Cyber Vision Explorer")

        print("Here are the different reports we can generate:")
        print("1: Credentials and Variables Report (non-separated)")
        print("2: Credentials and Variables Report (where the device and component values are in separate sheets)")
        print("3: KEV (Known Exploited Vulnerability) Report")
        print("4: MCCAST Inventory Report")
        print("5: Security Insights Report")
        print("6: Security Insights with Component Details Report")
        print("7: Exit program")
        print("8: Display options again")
        print(" ")
        choice = int(input("Please input which report you'd like to generate: "))
    elif choice == 6:
        securitydetails.get_security_details(center_token, center_ip)
        print(" ")
        choice = int(input("Please input which report you'd like to generate: "))
    elif choice == 5:
        securityinsights.get_security_insights(center_token, center_ip)
        print(" ")
        choice = int(input("Please input which report you'd like to generate: "))
    elif choice == 4:
        mccast.generate_mccast_inventory(center_token, center_ip)
        print(" ")
        choice = int(input("Please input which report you'd like to generate: "))
    elif choice == 3:
        findkevs.generate_kev_report(center_token, center_ip)
        print(" ")
        choice = int(input("Please input which report you'd like to generate: "))
    elif choice == 2:
        credvarseparated.get_cred_var_separated(center_token, center_ip)
        print(" ")
        choice = int(input("Please input which report you'd like to generate: "))
    elif choice == 1:
        credvar.get_creds_and_vars(center_token, center_ip)
        print(" ")
        choice = int(input("Please input which report you'd like to generate: "))

print("Exiting program...")
time.sleep(2)