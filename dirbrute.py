import requests
import argparse
import sys
from concurrent.futures import ThreadPoolExecutor

# Argument handling
def get_arguments():
    if len(sys.argv) == 1:
        url = input("Target URL: ").strip()
        wordlist = input("Wordlist path: ").strip()
        threads = 20
    else:
        parser = argparse.ArgumentParser(description="Simple Directory Brute Force Tool")
        parser.add_argument("-u", "--url", required=True, help="Target URL")
        parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file")
        parser.add_argument("-t", "--threads", type=int, default=20, help="Number of threads")

        args = parser.parse_args()

        url = args.url
        wordlist = args.wordlist
        threads = args.threads

    return url.rstrip("/"), wordlist, threads


# HTTP configuration
HEADERS = {
    "User-Agent": "DirBrute/1.0 (Python Security Tool)"
}

# Valid HTTP response codes
VALID_CODES = [200, 204, 301, 302, 307, 401, 403]

# Request worker
def scan_directory(word):
    word = word.strip()

    if not word:
        return

    target = f"{BASE_URL}/{word}"

    try:
        response = requests.get(
            target,
            headers=HEADERS,
            timeout=5,
            allow_redirects=False
        )

        status = response.status_code

        if status in VALID_CODES:
            print(f"[{status}] {target}")

    except requests.exceptions.RequestException:
        pass

# Wordlist loader
def load_wordlist(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as file:
            return file.readlines()
    except FileNotFoundError:
        print("[!] Wordlist not found.")
        sys.exit(1)


# Main execution
def main():
    global BASE_URL

    BASE_URL, wordlist_path, threads = get_arguments()
    words = load_wordlist(wordlist_path)

    print("\n========== DirBrute ==========")
    print(f"Target  : {BASE_URL}")
    print(f"Threads : {threads}")
    print(f"Entries : {len(words)}")
    print("================================\n")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(scan_directory, words)

if __name__ == "__main__":
    main()