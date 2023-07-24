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

def format_tool_info(tool_name, tool_description, usage_example, additional_options):
    print(f"\n== {tool_name.upper()} ==\n")
    print("DESCRIPTION:")
    print(tool_description)
    print("\nUSAGE:")
    print(f"To use {tool_name}, you can follow the command below:")
    print(f"$ {usage_example}\n")
    print("ADDITIONAL OPTIONS:")
    print(additional_options)

def search_tool(tool_name):
    kali_tools = {
        "nmap": {
            "description": "Nmap is a powerful network scanner used to discover hosts and services on a computer network.",
            "usage_example": "nmap -sS -p 1-1000 <target>",
            "additional_options": "Refer to the man page or online documentation for more options and usage examples.",
        },
        "gobuster": {
            "description": "Gobuster is a tool used to brute-force URIs (directories and files) in web sites and DNS subdomains (with wildcard support).",
            "usage_example": "gobuster dir -u http://example.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt",
            "additional_options": "You can use different wordlists and customize the brute-force settings based on your needs.",
        },
        "hydra": {
            "description": "Hydra is a fast and flexible password-cracking tool that can perform rapid dictionary attacks against more than fifty protocols.",
            "usage_example": "hydra -l <username> -P /path/to/passwords.txt <target> <protocol>",
            "additional_options": "Hydra supports numerous protocols and attack types. Refer to the man page for detailed options.",
        },
        "nikto": {
            "description": "Nikto is a web server scanner that performs comprehensive tests against web servers for multiple items, including dangerous files and outdated versions of software.",
            "usage_example": "nikto -h <target>",
            "additional_options": "Nikto has various options to customize scans. Refer to the man page for more details.",
        },
        "sqlmap": {
            "description": "Sqlmap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection vulnerabilities.",
            "usage_example": "sqlmap -u 'http://example.com/vulnerable_page.php?id=1'",
            "additional_options": "Sqlmap offers extensive options to test different types of SQL injections. Refer to the man page for detailed usage.",
        },
        "metasploit": {
            "description": "Metasploit Framework is a powerful open-source tool used to develop, test, and execute exploit code against a remote target.",
            "usage_example": "msfconsole",
            "additional_options": "Metasploit provides a vast array of modules and payloads. Refer to the documentation for detailed usage.",
        },
        "burpsuite": {
            "description": "Burp Suite is a graphical tool used for web application security testing, including intercepting and modifying HTTP traffic, and finding security vulnerabilities.",
            "usage_example": "burpsuite",
            "additional_options": "Burp Suite has multiple modules for various web security tasks. Explore the user guide for more information.",
        },
        "dirb": {
            "description": "Dirb is a URL bruteforcer for directories and files on a web server.",
            "usage_example": "dirb http://example.com /usr/share/wordlists/dirb/big.txt",
            "additional_options": "Dirb supports various wordlists and options for directory and file bruteforcing.",
        },
        "enum4linux": {
            "description": "Enum4linux is a tool for enumerating information from Windows machines, such as user and group details, shares, and more.",
            "usage_example": "enum4linux -a <target>",
            "additional_options": "Enum4linux provides several options for enumerating Windows machine information. Refer to the man page for details.",
        },
        "john": {
            "description": "John the Ripper is a fast password cracker, available for many operating systems, which supports various password encryptions.",
            "usage_example": "john /path/to/passwords.txt",
            "additional_options": "John the Ripper can crack passwords using multiple techniques. Refer to the man page for detailed usage.",
        },
        "aircrack-ng": {
            "description": "Aircrack-ng is a network software suite consisting of a detector, packet sniffer, WEP and WPA/WPA2-PSK cracker, and analysis tool for 802.11 wireless LANs.",
            "usage_example": "aircrack-ng -w /path/to/wordlist -b <BSSID> <capture_file>.cap",
            "additional_options": "Aircrack-ng offers various options for wireless network analysis and cracking. Refer to the man page for more details.",
        },
        "wireshark": {
            "description": "Wireshark is a popular network protocol analyzer that captures and inspects packets on a network in real-time.",
            "usage_example": "wireshark",
            "additional_options": "Wireshark provides extensive filters and analysis features. Check the user guide for detailed usage.",
        },
        "hashcat": {
            "description": "Hashcat is a fast and advanced password recovery tool that supports various algorithms and attack modes.",
            "usage_example": "hashcat -a 0 -m 0 /path/to/hashes.txt /path/to/wordlist.txt",
            "additional_options": "Hashcat supports multiple attack modes and options. Refer to the man page for detailed usage.",
        },
        "wpscan": {
            "description": "Wpscan is a black box WordPress vulnerability scanner.",
            "usage_example": "wpscan --url http://example.com/",
            "additional_options": "Wpscan has various options to scan WordPress installations for vulnerabilities. Refer to the man page for details.",
        },
        "maltego": {
            "description": "Maltego is an open-source intelligence (OSINT) and graphical link analysis tool.",
            "usage_example": "maltego",
            "additional_options": "Maltego provides multiple transforms for gathering OSINT data. Explore the tool for more information.",
        },
        "seclists": {
            "description": "Seclists is a collection of multiple types of lists used during security assessments.",
            "usage_example": "No specific usage example. It contains various lists that can be used in security assessments.",
            "additional_options": "Refer to the official documentation for the available lists and their usage.",
        },
        "snort": {
            "description": "Snort is an open-source intrusion detection and prevention system (IDS/IPS) used for network security monitoring.",
            "usage_example": "snort -A console -c /etc/snort/snort.conf -i <interface>",
            "additional_options": "Snort can be configured with different rulesets and settings. Refer to the documentation for detailed usage.",
        },
        "hping3": {
            "description": "Hping3 is a command-line network tool used for packet crafting, firewall testing, and other purposes.",
            "usage_example": "hping3 -S -p 80 <target>",
            "additional_options": "Hping3 has various options for crafting custom packets and performing network tests. Refer to the man page for details.",
        },
        "golismero": {
            "description": "Golismero is a web application and website vulnerability scanner.",
            "usage_example": "golismero scan <target>",
            "additional_options": "Golismero provides different modules for web security testing. Refer to the documentation for more details.",
        },
        "recon-ng": {
            "description": "Recon-ng is a full-featured web reconnaissance framework.",
            "usage_example": "recon-ng",
            "additional_options": "Recon-ng offers various modules for OSINT gathering and web reconnaissance. Explore the framework for more information.",
        },
        "netcat": {
            "description": "Netcat is a versatile networking utility that reads and writes data across network connections.",
            "usage_example": "netcat -lvp 4444",
            "additional_options": "Netcat has multiple options for creating and handling network connections. Refer to the man page for more details.",
        },
        "zenmap": {
            "description": "Zenmap is the official Nmap Security Scanner GUI.",
            "usage_example": "zenmap",
            "additional_options": "Zenmap provides a graphical interface for Nmap scans. Check the documentation for usage details.",
        },
        "bettercap": {
            "description": "Bettercap is a powerful, easily extensible, and portable framework for network attacks and man-in-the-middle attacks.",
            "usage_example": "bettercap -iface <interface> -X",
            "additional_options": "Bettercap provides a range of options for network attacks and MITM operations. Refer to the documentation for detailed usage.",
        },
        "mitmproxy": {
            "description": "Mitmproxy is an interactive, SSL-capable man-in-the-middle proxy for HTTP with a console interface.",
            "usage_example": "mitmproxy -T --host",
            "additional_options": "Mitmproxy allows real-time interception and modification of HTTP traffic. Refer to the documentation for usage instructions.",
        },
        "unicornscan": {
            "description": "Unicornscan is a stateless and fast network scanning utility.",
            "usage_example": "unicornscan -mU -v -Iv <target>",
            "additional_options": "Unicornscan provides options for UDP, TCP, and ICMP scans. Refer to the man page for more details.",
        },
        "hyena": {
            "description": "Hyena is a password-cracking tool for offline password cracking.",
            "usage_example": "hyena -w <wordlist> -f <hashfile>",
            "additional_options": "Hyena supports various hash types and cracking modes. Refer to the man page for more details.",
        },
        "cherrytree": {
            "description": "CherryTree is a hierarchical note-taking application, featuring rich text and syntax highlighting.",
            "usage_example": "cherrytree",
            "additional_options": "CherryTree allows organizing notes hierarchically. Explore the application for more features.",
        },
        "setoolkit": {
            "description": "Setoolkit is a toolkit for social engineering attacks, including phishing campaigns and website clones.",
            "usage_example": "setoolkit",
            "additional_options": "Setoolkit provides various attack vectors for social engineering. Refer to the documentation for detailed usage.",
        },
        "routersploit": {
            "description": "Routersploit is an open-source exploitation framework dedicated to embedded devices.",
            "usage_example": "routersploit",
            "additional_options": "Routersploit contains numerous exploits targeting embedded devices. Check the documentation for usage instructions.",
        },
        "beef-xss": {
            "description": "Beef-XSS (Browser Exploitation Framework) is a powerful penetration testing tool used for targeting web browsers.",
            "usage_example": "beef-xss",
            "additional_options": "Beef-XSS provides modules for browser exploitation. Refer to the documentation for detailed usage.",
        },
    }

    if tool_name in kali_tools:
        tool_info = kali_tools[tool_name]
        format_tool_info(tool_name, tool_info["description"], tool_info["usage_example"], tool_info["additional_options"])
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
