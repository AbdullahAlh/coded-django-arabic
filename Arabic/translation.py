from modeltranslation.translator import TranslationOptions, translator
from Arabic.models import TransModel


class TransModelTranslationOpt(TranslationOptions):
    fields = ('title', 'info')

translator.register(TransModel, TransModelTranslationOpt)