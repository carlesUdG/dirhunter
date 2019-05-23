import requests

def attack(host, wordlist, extension):
    try:
        wordlist = wordlist.split('\n')
        for word in wordlist:
            if not word.startswith('#') and not word.startswith(' '):
                response = requests.get('{0}{1}'.format(host, word), headers=None)
                print('{:<25s}{:>4d}'.format(word, response.status_code))
                if extension != None:
                    response = requests.get('{0}{1}'.format(host, word + extension), headers=None)
                    print('{:<25s}{:>4d}'.format(word + extension, response.status_code))
    except KeyboardInterrupt:
        print('\n\nBye!')

host = input('Enter the host...\n')
fileName = input('Enter the file name your wordlist (e.g. directory-list-2.3-small.txt)...\n')

if not host.endswith('/'):
    host = host + '/'

extension = '.html'

file = open(fileName, 'r')
wordlist = file.read()
attack(host, wordlist, extension)