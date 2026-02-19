import logging
import time
import timeit
from docx import Document
from docx.shared import Inches
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import Levenshtein
from rapidfuzz.distance.metrics_cpp import levenshtein_distance


def extract_text_from_docx(filename):
    doc = Document(filename)
    return '\n'.join([paragraph.text for paragraph in doc.paragraphs])
text1 = extract_text_from_docx('text1.docx')
text2 = extract_text_from_docx('text2.docx')

logging.basicConfig(
    level=logging.INFO,
    filename="f1.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s %(levelname)s %(message)s"
)
def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

# start = time.time()
# str1 = 'boss'
# str2 = 'loshara'
# print(levenstein(str1, str2))
# logging.info(f"Call def levenstein with str {str1,str2}")
# end = time.time()
# logging.info(f'Time:{end - start}')


start = time.time()
print(levenstein(text1, text2))
logging.info(f"Call def levenstein with docx {text1,text2}")
end = time.time()
logging.info(f'Time:{end - start}')


start = time.time()
num = fuzz.ratio(text1,text2)
print(num)
logging.info(f"Call fuzz.ratio with docx {text1,text2}")
end = time.time()
logging.info(f'Time:{end - start}')

start = time.time()
num = levenshtein_distance(text1,text2)
print(num)
logging.info(f"Call levenshtein_distance with docx {text1,text2}")
end = time.time()
logging.info(f'Time:{end - start}')