"""
Translator of text text from English to French and vice versa
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey=apikey)
translator = LanguageTranslatorV3(authenticator=authenticator,version='2023-05-02')
translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translates text from English to French
    """
    french_text_result = translator.translate(text=english_text,source='en', target='fr').get_result()
    french_text = french_text_result['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translates text from French to English
    """
    english_text_result = translator.translate(text=french_text,source='fr', target='en').get_result()
    english_text = english_text_result['translations'][0]['translation']
    return english_text
