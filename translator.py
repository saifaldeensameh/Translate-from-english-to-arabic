from bs4 import BeautifulSoup
from googletrans import Translator
from time import sleep


def translate_text(input_file, output_file, src_lang="en", dest_lang="ar"):
   with open(input_file, "r", encoding="utf-8") as f:
       content = f.read()

   # Split on \n
   paragraphs = content.split("\n")

   translator = Translator()
   translated_paragraphs = []
   i = 1

   for paragraph in paragraphs:
       if paragraph == "":
           translated_paragraphs.append("")
           continue

       print(i)
       i += 1

       max_retries = 5  # Set maximum number of retries
       for attempt in range(max_retries + 1):
           try:
               translated_text = translator.translate(paragraph, src=src_lang, dest=dest_lang).text
               break  # Exit the loop on success
           except Exception as e:
               print(f"Error translating: {e}. Attempt {attempt}/{max_retries}")
               if attempt == max_retries:
                   translated_text = paragraph
           sleep(5)

       translated_paragraphs.append(translated_text)
       sleep(1)

   translated_content = "\n".join(translated_paragraphs)
   with open(output_file, "w", encoding="utf-8") as f:
       f.write(translated_content)


# Example usage
input_file = "input.txt"
output_file = "translated_Little_Dorrit.txt"
translate_text(input_file, output_file)

print(f"Translated paragraphs written to {output_file}")

