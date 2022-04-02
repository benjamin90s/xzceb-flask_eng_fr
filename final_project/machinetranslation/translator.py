"""import libraries"""
import os
from ibm_watson import LanguageTranslatorV3 #from IBM
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator#authenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('rThbq2SZ8s2Re6QBulyKfSmjrjD31b4uQKnzIO2N1vT_')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
"""Watson language
translator URL"""
language_translator.set_service_url(
'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/e279067d-1540-4b78-aa82-94651eb0d368')
def english_to_french(english_text):
    """function to translate eng to french"""
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """function to translate french to eng"""
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
