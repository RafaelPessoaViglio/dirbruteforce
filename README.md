# DirBrute — Directory Brute Force Tool

DirBrute is a multithreaded directory brute force tool written in Python, designed for security students, penetration testers, and bug bounty hunters.

The tool performs fast web directory enumeration using customizable wordlists and intelligent response filtering.

---

## Features

* Multithreaded scanning
* CLI arguments support
* Interactive mode execution
* Custom wordlist support
* HTTP status filtering
* Wildcard response detection
* Clean and minimal output
* Beginner-friendly codebase
* Designed for cybersecurity learning

---

## Requirements

* Python 3.9+
* Internet connection
* Linux, Windows or macOS

Install dependencies:

```
pip install requests
```

---

## Installation

Clone the repository:

```
https://github.com/RafaelPessoaViglio/dirbruteforce
cd dirbruteforce
```

Create a virtual environment (recommended):

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

Linux / macOS:

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

### Interactive Mode

Run without arguments:

```
python dirbrute.py
```

You will be prompted for:

* Target URL
* Wordlist path

---

### CLI Mode

```
python dirbrute.py -u https://target.com -w wordlist.txt
```

---

### Optional Arguments

```
-t, --threads     Number of concurrent threads (default: 20)
```

Example:

```
python dirbrute.py -u https://target.com -w wordlist.txt -t 50
```

---

## Example Output

```
========== DirBrute ==========
Target  : https://target.com
Threads : 20
Entries : 500
================================

[200] https://target.com/admin
[403] https://target.com/private
[301] https://target.com/login
```

---

## Project Structure

```
dirbrute/
│
├── dirbrute.py
├── wordlist.txt
├── requirements.txt
└── README.md
```

---

## How It Works

1. Loads a wordlist.
2. Generates HTTP requests concurrently.
3. Filters irrelevant responses.
4. Detects wildcard responses automatically.
5. Displays only meaningful findings.

---

## Educational Purpose

This project was created for:

* Cybersecurity learning
* Networking understanding
* Web enumeration practice
* Python multithreading study

---

## Legal Disclaimer

This tool is intended **ONLY** for educational purposes and authorized security testing.

Do NOT use against systems without explicit permission.

The author is not responsible for misuse or illegal activities.

---

## Future Improvements

* Response size filtering
* Extensions fuzzing
* Progress bar
* Async scanning engine
* JSON output support
* Proxy support
* Rate limiting

---

## Author

Rafael Pessoa Viglio
Security Student & Developer
Focused on Cybersecurity and Offensive Security

---

## License

MIT License
