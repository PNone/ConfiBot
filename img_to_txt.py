import cv2
import pytesseract
import json
import os
from googletrans import Translator
import re


with open('config.json', encoding='utf-8') as json_file:
    config = json.load(json_file)

src_lang = config.get('srcLanguage', None)
dst_lang = config.get('dstLanguage', None)
fixes = config.get('textFixes', None)
translator = Translator()

should_translate = src_lang is not None and dst_lang is not None


images_directory = os.path.join('out', config['profileName'])
output_file_name = os.path.join('out', f"{config['profileName']}.txt")
orig_lang_output_file_name = os.path.join('out', f"{config['profileName']}-{src_lang}.txt")
pytesseract.pytesseract.tesseract_cmd = config['tesseractExec']

texts_waiting_for_a_flush = 0


with open(output_file_name, 'w', encoding='utf-8') as output_file, \
        open(orig_lang_output_file_name, 'w', encoding='utf-8') as orig_lang_output_file:
    for dir_item in os.listdir(images_directory):
        post_dir_path = os.path.join(images_directory, dir_item)
        if not os.path.isdir(post_dir_path):
            continue

        post_original_text = ''
        post_text = ''

        for post_image in os.listdir(post_dir_path):
            img_path = os.path.join(post_dir_path, post_image)
            img = cv2.imread(img_path)
            text = pytesseract.image_to_string(img, lang=config['language'])
            post_original_text += text

        clean_txt = post_original_text.strip()
        clean_txt = ''.join(re.findall('[A-Za-z0-9א-ת\-\"\'()\s:?.,]+', clean_txt))
        if clean_txt != '' and fixes is not None:
            for fix_key, fix_val in fixes.items():
                clean_txt = clean_txt.replace(fix_key, fix_val)
        if clean_txt == '':
            post_text = ''
        elif should_translate:
            try:
                result = translator.translate(clean_txt, src=src_lang, dest=dst_lang)
                post_text = result.text
            except Exception as err:
                print(err)
                print('Bad text', clean_txt)
                print('Problematic folder', dir_item)
                post_text = ''
        else:
            post_text = post_original_text

        if post_text == '':
            continue

        output_file.write('<===============\n')
        orig_lang_output_file.write('<===============\n')
        output_file.write(post_text)
        output_file.write('\n')
        output_file.write('===============>\n')
        orig_lang_output_file.write(clean_txt)
        orig_lang_output_file.write('\n')
        orig_lang_output_file.write('===============>\n')
        texts_waiting_for_a_flush += 1
        if texts_waiting_for_a_flush % 100 == 0:
            output_file.flush()
            orig_lang_output_file.flush()
        texts_waiting_for_a_flush %= 100
