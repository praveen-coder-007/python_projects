import random

def generate_random_ip():
    return f"10.91.82.{random.randint(0,20)}"

def check_firewall_rule(ip_adress, firewall_rules):
    if ip_adress in firewall_rules:
        return firewall_rules[ip_adress]
    return "allow"

def main():

    firewall_rules = {
        "10.91.82.1" : "block",
        "10.91.82.6" : "block",
        "10.91.82.3" : "block",
        
          }

    for i in range(12):
        ip_adress = generate_random_ip()
        action = check_firewall_rule(ip_adress, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f" Ip adress: {ip_adress}, action: {action}, random: {random_number}")

main()