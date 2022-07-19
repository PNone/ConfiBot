# ConfiBot
Auto fetch and generate posts based on confessions

To run, make sure to:
create a config.json file with the name of the profile you want to download from,
and your instagram credentials in it:
Don't forget a tesseract.exe location
You can also fix and translate the results.
Use a gpt3 token to generate more data.
```
{
  "username": "Your Instagram username",
  "password": "Your Instagram password",
  "profileName": "instagram_profile_to_fetch_from",
  "tesseractExec": "absolutePathToExec",
  "language": "original_language_pytesseract_format",
  "srcLanguage": "original_language_google_translate_format",
  "dstLanguage": "destination_language_google_translate_format",
  "openAiToken": "tokenToUseWithGPT3",
  "textFixes": {
    "original_phrase": "fixed_phrase",
    "original_phrase2": "fixed_phrase2",
    ...
  }
}
```
run:
pip install -r requirements.txt

Note:
googletrans may require python:
3.6<=version<=3.8
