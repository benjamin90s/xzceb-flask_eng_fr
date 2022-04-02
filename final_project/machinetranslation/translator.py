"""import libraries"""
import os
from ibm_watson import LanguageTranslatorV3 #from IBM
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator#authenticator
from dotenv import load_dotenv

load_dotenv()
"""assigns api & url."""
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('Vbm9RmMIYQW4r_KfynvnF5fNw6gGbKQcWNGcnPLtlNcn')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

"""Watson language 
translator URL"""

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/21f4fb62-358e-4191-afd7-0680eaa63285')

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
