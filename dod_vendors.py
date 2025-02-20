import requests
import json
from colorama import init, Fore, Style

init()

def fetch_dod_vendors(page):
    url = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
    payload = {
        "filters": {
            "agencies": [{"type": "awarding", "tier": "toptier", "name": "Department of Defense"}],
            "award_type_codes": ["A"],
            "award_amount": {"gte": 25000}
        },
        "fields": ["Recipient Name", "Award Amount", "Award ID"],
        "limit": 100,
        "page": page
    }
    response = requests.post(url, json=payload, timeout=10)
    if response.status_code != 200:
        print(f"{Fore.RED}Error: {response.status_code} - {response.text}{Style.RESET_ALL}")
        return None
    data = response.json()

    return [v for v in data.get("results", []) if float(v.get("Award Amount", 0)) >= 25000]

def display_vendors(vendors, page):
    if not vendors:
        print(f"{Fore.YELLOW}No vendors found for page {page}{Style.RESET_ALL}")
        return
    
    print(f"{Fore.CYAN}{'═' * 80}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}DoD Vendors with Contracts Over $25,000 USD (Page {page} of 50){Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'═' * 80}{Style.RESET_ALL}")
    print()

    colors = [Fore.GREEN, Fore.MAGENTA, Fore.BLUE, Fore.YELLOW, Fore.CYAN]
    for i, vendor in enumerate(vendors, (page - 1) * 100 + 1):
        color = colors[i % len(colors)]
        print(f"{color}Vendor #{i}:{Style.RESET_ALL}")
        print(f"{color}  Name: {vendor.get('Recipient Name', 'N/A')}{Style.RESET_ALL}")
        print(f"{color}  Award Amount: ${float(vendor.get('Award Amount', 0)):,.2f}{Style.RESET_ALL}")
        print(f"{color}  Award ID: {vendor.get('Award ID', 'N/A')}{Style.RESET_ALL}")
        print()

def main():
    print(f"{Fore.GREEN}Starting live fetch of DoD vendors...{Style.RESET_ALL}")
    page = 1
    while page <= 50:
        print(f"{Fore.YELLOW}Fetching page {page}...{Style.RESET_ALL}")
        vendors = fetch_dod_vendors(page)
        if vendors is None:
            break
        
        display_vendors(vendors, page)
        
        if page < 50:
            print(f"{Fore.BLUE}Options:{Style.RESET_ALL}")
            choice = input(f"{Fore.BLUE}Enter 'n' for next, 'q' to quit: {Style.RESET_ALL}").lower()
            if choice == 'n':
                page += 1
            elif choice == 'q':
                print(f"{Fore.RED}Exiting...{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.YELLOW}Invalid choice, exiting{Style.RESET_ALL}")
                break
        else:
            print(f"{Fore.RED}Reached page 50{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()
