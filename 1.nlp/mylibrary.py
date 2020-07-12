import re

# Funcion para limpiar texto (al parecer HTML)
def get_text(file):
  text = open(file).read()
  text = re.sub (r'<.*?>',' ', text)
  text = re.sub (r'\s+',' ', text)
  return text
