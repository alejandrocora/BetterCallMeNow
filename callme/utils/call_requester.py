import requests
import urllib
from bs4 import BeautifulSoup
import datetime

from callme.constants import *


class CommonCallSubmit:
    def get_form_parameters(soup, parsed_url):
        forms = soup.find_all('form')
        form = False
        if not forms:
            return False
        for form_element in forms: # avoids outside forms
            if not form_element.get('action'):
                form = form_element
                break
            try:
                encoded_form_url = urllib.parse.urlencode(form_element.get('action')).netloc
                if (parsed_url.netloc == encoded_form_url): # checking if the form is for the own website
                    form = form_element
                    break
            except:
                form = form_element
        request_data = {
            'method' : form.get('method'),
            'action' : form.get('action')
        }
        return [request_data, CommonCallSubmit.get_inputs(form)]

    def get_inputs(soup):
        input_parameters = {}
        for html_input in (soup.find_all('input')+soup.find_all('textarea')):
            if html_input.get('name'):
                input_parameters[html_input.get('name')] = html_input.get('value')
        for html_select in soup.find_all('select'):
            select_options = []
            for html_option in html_select.find_all('option'):
                select_options.append(html_option.get('value'))
            input_parameters[html_select.get('name')] = select_options
        return input_parameters

    def set_phone_parameter(form_data, phone_number): # perhaps include this in set_commom_parameters?
        for key in form_data.keys():
            if key:
                if any(param_name in key.lower() for param_name in COMMON_PHONE_PARAMETERS):
                    form_data[key] = phone_number
        return form_data

    def set_common_parameters(form_data): # maybe fill with something random every one that has text in it?
        COMMON_PAYLOAD['hour'] = str(datetime.datetime.now().hour+1)+':00'
        for key in form_data.keys():
            for parameter in COMMON_PARAMETERS.keys():
                if form_data[key]:
                    break
                elif any(param_name in key.lower() for param_name in COMMON_PARAMETERS[parameter]):
                    form_data[key] = COMMON_PAYLOAD[parameter]
                    break
        return form_data

    def request_call(url, phone_number):
        session = requests.Session()
        session.headers.update({
            'User-agent':DEFAULT_HEADER
        })
        try:
            html = session.get(url).text
        except requests.exceptions.MissingSchema:
            return 0
        parsed_url = urllib.parse.urlparse(url, scheme='', allow_fragments=True)
        form_parameters = CommonCallSubmit.get_form_parameters(BeautifulSoup(html, 'html.parser'), parsed_url)
        if (not form_parameters) or (not form_parameters[1]): 
            form_parameters = [{'method':'post', 'action':url}, CommonCallSubmit.get_inputs(BeautifulSoup(html, 'html.parser'))]
        pet_data = CommonCallSubmit.set_phone_parameter(form_parameters[1], phone_number) # pet is short for petition, maybe find a more suitable name
        pet_data = CommonCallSubmit.set_common_parameters(pet_data)
        if form_parameters[0]['action']:
            if urllib.parse.urlparse(form_parameters[0]['action'], scheme='', allow_fragments=True).scheme:
                action = form_parameters[0]['action']
            else:
                if parsed_url.path[-1:] == '/':
                    url = url[:-1]
                if form_parameters[0]['action'][0] == '/':
                    action = parsed_url.scheme+'://'+parsed_url.netloc+form_parameters[0]['action']
                else:
                    action = url+'/'+form_parameters[0]['action']
        else:
            action = url
        if form_parameters[0]['method'] == 'get':
            query = '?'+urllib.parse.urlencode(pet_data, doseq=False, safe='', encoding=None, errors=None)
            return session.get(action+query).status_code
        else:
            return session.post(action, pet_data).status_code