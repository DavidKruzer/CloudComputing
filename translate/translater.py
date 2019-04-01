 # Imports the Google Cloud client library
from google.cloud import translate as google_translate
from .models import Translation

translate_client = google_translate.Client()

def translate(original):
    translations = Translation.objects.filter(original=original)
    if len(translations) > 0:
        return translations[0].translation
    translation = cloud_translate(original);
    Translation.objects.create(original = original, translation = translation)
    return translation;
def cloud_translate(original):
    # The target language
    target = 'en'
    
    translation = translate_client.translate(
        original,
        target_language=target)
    return translation['translatedText'];
