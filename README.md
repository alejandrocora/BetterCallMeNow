<img src="BCMN.png" width="75px" height="75px" align="right">

# Better Call Me Now!

Better Call Me Now! is an automated program to request phone calls from (most) of websites that allow this option, usually related to insurance or TSP companies.

It can be used to measure the quality of customer service websites, speed up contact with multiple clients or services, or test the viability of a phone line, among other uses.

## Installation

`$ git clone https://github.com/alejandrocora/BetterCallMeNow`  
`$ cd BetterCallMeNow`  
`$ pip3 install .`

## Help

```
usage: callme [-h] --url_file URL_FILE phones [phones ...]

positional arguments:
  phones               A list of one or more phone numbers, separated by spaces.

options:
  -h, --help           show this help message and exit
  --url_file URL_FILE  File containing URLs separated in lines.
```

### Disclaimer

This program is meant to be used with non-malicious intent, with the consent of the phone numbers owners/users.

The URL file should be obtained/made by the user.
