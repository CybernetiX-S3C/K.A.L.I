import os

def get_username():
    try:
        username = os.getlogin()
    except OSError:  # If running with root privileges, get the effective user
        import pwd
        username = pwd.getpwuid(os.geteuid()).pw_name
    return username

def greet_user():
    username = get_username()
    print(f"K.A.L.I. - Kali's Assistant for Learning and Investigations: Hello, {username}! I'm here to help you with your security and penetration testing inquiries on Kali Linux. How can I assist you today?")

def format_tool_manpage(tool_name, tool_description):
    print(f"\n== {tool_name.upper()} ==\n")
    print("DESCRIPTION:")
    print(tool_description)
    print("\nUSAGE:")
    print(f"To use {tool_name}, you can follow the command below:")
    print(f"$ {tool_name} [options]\n")

def search_tool(tool_name):
    kali_tools = {
        "nmap": "Nmap is a powerful network scanner used to discover hosts and services on a computer network.",
        "gobuster": "Gobuster is a tool used to brute-force URIs (directories and files) in web sites and DNS subdomains (with wildcard support).",
        "hydra": "Hydra is a fast and flexible password-cracking tool that can perform rapid dictionary attacks against more than fifty protocols.",
        "nikto": "Nikto is a web server scanner that performs comprehensive tests against web servers for multiple items, including dangerous files and outdated versions of software.",
        "sqlmap": "Sqlmap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection vulnerabilities.",
        "metasploit": "Metasploit Framework is a powerful open-source tool used to develop, test, and execute exploit code against a remote target.",
        "burpsuite": "Burp Suite is a graphical tool used for web application security testing, including intercepting and modifying HTTP traffic, and finding security vulnerabilities.",
        "dirb": "Dirb is a URL bruteforcer for directories and files on a web server.",
        "enum4linux": "Enum4linux is a tool for enumerating information from Windows machines, such as user and group details, shares, and more.",
        "john": "John the Ripper is a fast password cracker, available for many operating systems, which supports various password encryptions.",
        "aircrack-ng": "Aircrack-ng is a network software suite consisting of a detector, packet sniffer, WEP and WPA/WPA2-PSK cracker, and analysis tool for 802.11 wireless LANs.",
        "wireshark": "Wireshark is a popular network protocol analyzer that captures and inspects packets on a network in real-time.",
        "hashcat": "Hashcat is a fast and advanced password recovery tool that supports various algorithms and attack modes.",
        "wpscan": "Wpscan is a black box WordPress vulnerability scanner.",
        "maltego": "Maltego is an open-source intelligence (OSINT) and graphical link analysis tool.",
        "seclists": "Seclists is a collection of multiple types of lists used during security assessments.",
        "snort": "Snort is an open-source intrusion detection and prevention system (IDS/IPS) used for network security monitoring.",
        "hping3": "Hping3 is a command-line network tool used for packet crafting, firewall testing, and other purposes.",
        "golismero": "Golismero is a web application and website vulnerability scanner.",
        "recon-ng": "Recon-ng is a full-featured web reconnaissance framework.",
        "netcat": "Netcat is a versatile networking utility that reads and writes data across network connections.",
        "zenmap": "Zenmap is the official Nmap Security Scanner GUI.",
        "bettercap": "Bettercap is a powerful, easily extensible, and portable framework for network attacks and man-in-the-middle attacks.",
        "mitmproxy": "Mitmproxy is an interactive, SSL-capable man-in-the-middle proxy for HTTP with a console interface.",
        "unicornscan": "Unicornscan is a stateless and fast network scanning utility.",
        "hyena": "Hyena is a password-cracking tool for offline password cracking.",
        "cherrytree": "CherryTree is a hierarchical note-taking application, featuring rich text and syntax highlighting.",
        "setoolkit": "Setoolkit is a toolkit for social engineering attacks, including phishing campaigns and website clones.",
        "routersploit": "Routersploit is an open-source exploitation framework dedicated to embedded devices.",
        "beef-xss": "Beef-XSS (Browser Exploitation Framework) is a powerful penetration testing tool used for targeting web browsers.",
    }

    if tool_name in kali_tools:
        format_tool_manpage(tool_name, kali_tools[tool_name])
    else:
        print(f"Sorry, '{tool_name}' is not a recognized tool in Kali Linux. Please check the name and try again.")

if __name__ == "__main__":
    greet_user()
    while True:
        tool_name = input("\nPlease enter the name of the tool you want to learn about (or 'exit' to quit): ").lower()
        if tool_name == "exit":
            print("Thank you for using K.A.L.I. Have a great day!")
            break
        search_tool(tool_name)
        
