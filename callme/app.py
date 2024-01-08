#!/usr/bin/env python3

import requests, sys, time, argparse, urllib

from callme.utils.call_requester import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('phones', metavar='phones', type=str, nargs='+', help='A list of one or more phone numbers, separated by spaces.')
    parser.add_argument('--url_file', dest='url_file', required=True, help='File containing target URLs separated in lines.')
    parser.add_argument('--check', dest='check', action='store_true', help='Activates URL list checking and fixing.')
    parser.add_argument('--verbose', dest='verbose', action='store_true', default='store_false', help='Print also the request parameters and method.')
    args = parser.parse_args()
    phones = args.phones
    urls = [line.strip() for line in open(args.url_file, 'r') if line.strip()]
    checked_urls = []
    CommonCallSubmit.verbose = args.verbose
    if args.check:
        CommonCallSubmit.timeout = 10
        print('[i] Checking and fixing URLs...')
        for pos in range(0, len(urls)):
            if not urllib.parse.urlparse(urls[pos]).scheme:
                url = urls[pos]
                try:
                    url = 'https://'+urls[pos]
                    requests.get(url)
                    checked_urls.append(url)
                except requests.exceptions.RequestException:
                    url = 'http://'+urls[pos]
                    try:
                        requests.get(url)
                        checked_urls.append(url)
                    except Exception as e:
                        print('[!] Failed to get site "'+ urls[pos] +'" both with HTTP and HTTPS.')
            else:
                try:
                    requests.get(urls[pos])
                    checked_urls.append(urls[pos])
                except requests.exceptions.RequestException:
                    print('[!] Failed to get site "'+ urls[pos] + '".')
        print('[i] Done!')
    else:
        for url in urls:
            if not urllib.parse.urlparse(url).scheme:
                url = 'http://'+url
            checked_urls.append(url)
    urls = checked_urls
    for phone in phones:
        for url in urls:
            try:
                status_code = CommonCallSubmit.request_call(url, phone)
                if status_code == 0:
                    print('[!] Unable to get ' + url + ', missing schema in URL.')
                elif status_code == 1:
                    print('[!] No telephone number input found in ' + url + ', not sending request.')
                else:
                    print('[+] ', end = '') if status_code == 200 or status_code == 302 else print('[i] ', end = '')
                    print('Petition to ' + url + ' returned status code ' + str(status_code) + '.')
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
                print('[!] Unable to get ' + url + ', connection timeout.')
            except requests.exceptions.SSLError:
                print('[!] Unable to get ' + url + ', SSL error')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Quitting...")
        sys.exit(1)
