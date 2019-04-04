 # Imports the Google Cloud client library
from google.cloud import translate as google_translate
from .models import Translation

translate_client = google_translate.Client()

def translate(original, source_language, target_language):
    if source_language == "":
        translations = Translation.objects.filter(target_language=target_language).filter(original=original)
    else:
        translations = Translation.objects.filter(source_language=source_language).filter(target_language=target_language).filter(original=original)
    if len(translations) > 0:
        return {"text" : translations[0].translation, "language" : translations[0].source_language}
    translation = cloud_translate(original, source_language, target_language);
    Translation.objects.create(original = original, translation = translation['text'], target_language = target_language, source_language = translation['language'])
    return translation
def cloud_translate(original, source_language, target_language):  
    if source_language == "":
        translation = translate_client.translate(
        original,
        target_language=target_language)
        source_language = translation['detectedSourceLanguage']
    else:
        translation = translate_client.translate(
        original,
        target_language=target_language,
        source_language=source_language)
    return {'text' : translation['translatedText'], 'language' : source_language};
