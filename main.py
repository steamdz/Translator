import translate
from translate import Translator
Tran = Translator(from_lang="English",to_lang="Spanish")
Result = Tran.translate("How are you?")
print(Result)
