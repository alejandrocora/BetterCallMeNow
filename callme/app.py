#!/usr/bin/env python3

import requests, sys, time, argparse

from callme.utils.call_requester import CommonCallSubmit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('phones', metavar='phones', type=str, nargs='+', help='A list of one or more phone numbers, separated by spaces.')
    parser.add_argument('--url_file', dest='url_file', required=True, help='File containing target URLs separated in lines.')
    args = parser.parse_args()
    phones = args.phones
    urls = open(args.url_file, 'r').read().split('\n')
    for phone in phones:
        for url in urls:
            status_code = CommonCallSubmit.request_call(url, phone)
            if status_code == 0:
                print('[!] Unable to get ' + url + '.')
            else:
                print('[+] ', end = '') if status_code == 200 else print('[i] ', end = '')
                print(url + ' returned status code ' + str(status_code) + '.')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Quitting...")
        sys.exit(1)
