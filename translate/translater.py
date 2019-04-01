 # Imports the Google Cloud client library
from google.cloud import translate as google_translate
from .models import Translation

translate_client = google_translate.Client()

def translate(original, target_language):
    translations = Translation.objects.filter(target_language=target_language).filter(original=original)
    if len(translations) > 0:
        return translations[0].translation
    translation = cloud_translate(original, target_language);
    Translation.objects.create(original = original, translation = translation, target_language = target_language)
    return translation;
def cloud_translate(original, target_language):
    # The target language
    
    translation = translate_client.translate(
        original,
        target_language=target_language)
    return translation['translatedText'];
