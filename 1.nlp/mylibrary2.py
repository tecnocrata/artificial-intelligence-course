# Extraido desde https://platzi.com/comentario/1459473/
import nltk, re 
nltk.download('punkt')
from urllib import request
from nltk import word_tokenize

definstall(html2text):#Aunque no es buena práctica instalar desde el archivo, funciona con la librería subprocess 
    subprocess.check_call([sys.executable, "-m", "pip", "install", html2text])

#!pip install html2text  #Esta es la forma de instalar el script desde el entorno de ejecución de Colab
import html2text


# la funcion la podemos definir en el notebook y usar directamente
deffreq_words(url, n, encoding = 'utf8'):
  req = request.urlopen(url)
  html = req.read().decode(encoding)
  text = html2text.html2text(html)
  tokens = re.findall('\w+', text)
  tokens = [t.lower() for t in tokens]
  fd = nltk.FreqDist(tokens)
  return [t for (t, _) in fd.most_common(n)]