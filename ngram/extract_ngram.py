from nltk.data import load
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize
import itertools
import mysql.connector
import sys
import codecs

def extract_n_grams(sentences, n):
    tokenizer = load('file:C:/nltk_data/tokenizers/punkt/portuguese.pickle')
    treebank_word_tokenize = TreebankWordTokenizer().tokenize
    textNgrams = []
    for sent in sentences:
        subSentToken = []
        
        for subSent in tokenizer.tokenize(sent):
            subSentToken.extend([token for token in treebank_word_tokenize(subSent)])

        #wordToken.append(subSentToken)

        n_grams = ngrams(subSentToken, n)
        textNgrams=itertools.chain(textNgrams,n_grams)
    
    return textNgrams
   
tv=int(sys.argv[1])
encod = 'utf-8'   #'utf-8' or other encoding like '1252'
if len(sys.argv) < 4:
    print("Número de parâmetros incorretos: n-grama, arquivo texto, id-autor, id-obra")
    exit(1)

input_file      = sys.argv[2]
cnx = mysql.connector.connect(user='bdd', password='bdduff!!',
                                    host='50.62.209.195',
                                    database='edusmil_bdd',connection_timeout=300,buffered=True)
cursor = cnx.cursor(buffered=True)
select_search="select 1 from nlp_corpus_ngram where nlp_n_gram=" + str(sys.argv[1]) + " and  id_autor=" + str(sys.argv[3]) +" and id_obra_autor="+str(sys.argv[4])+" limit 0,10;"
cursor.execute(select_search)

if cursor.rowcount > 0:
    cnx.close()
    print("autor/obra já carregado")
    exit(1)
else:
    cnx.close()
try:
    f1 = codecs.open(input_file,  "rU", encoding = encod)

    #text="Maio findava, haviam já começado a soprar as monções de sudoeste, mas naquele entardecer mormacento fizera-se uma súbita calmaria em toda a região. Era como se a abóbada celeste, emborcada como uma ventosa sobre a terra, tivesse sugado quase todo o ar de um largo trato de planície, montanha e mar. E a velha cidade imperial, de tão ilustres palácios, templos e tumbas, ali plantada sobre ambas as margens do rio, parecia um organismo vivo, palpitante e intumescido, a sufocar à míngua de oxigênio."
    frase=f1.read()
    sent_tokenize_list = sent_tokenize(frase)
    print("Número de frases:" + str(len(sent_tokenize_list)))
    vn_gramas = extract_n_grams(sent_tokenize_list,tv)
    n_gramas = [ ' '.join(grams) for grams in vn_gramas]
    print("Total de " + str(tv)+"-gramas:" + str(len(n_gramas)))
    
    insert_ngram= "insert into nlp_corpus_ngram (nlp_corpus_ngram, nlp_n_gram, id_autor, id_obra_autor, timestamp) values "
    values_gram =""
    for i in n_gramas:
        values_gram = values_gram + "('" + str(i).replace("'","\\'") + "'," + sys.argv[1] + "," + sys.argv[3] + "," + sys.argv[4] +",now()),"

    if values_gram != "":
        values_gram = values_gram[:len(values_gram)-1]
    cnx = mysql.connector.connect(user='bdd', password='bdduff!!',
                                    host='50.62.209.195',
                                    database='edusmil_bdd',connection_timeout=300,buffered=True)
    cursor = cnx.cursor()
    insert_search= insert_ngram + values_gram + ";"
                                                                    
    cursor.execute(insert_search)
    cnx.close()
    f1.close()
except IOError as e:
    print(output_file + "I/O error({0}): {1}".format(e.errno, e.strerror))
    exit(1)