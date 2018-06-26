 # clustering dataset
# determine k using elbow method

from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import adjusted_rand_score
import pandas as pd
from sklearn import preprocessing

stopwords = "el la los les las de del a ante con en para por y o u tu te ti le que al ha un han lo su una estas esto este es tras suya a acá ahí ajena ajenas ajeno ajenos al algo algún alguna algunas alguno algunos allá alli allí ambos ampleamos ante antes aquel aquella aquellas aquello aquellos aqui aquí arriba  asi atras aun aunque bajo bastante bien cabe cada casi cierta ciertas cierto ciertos como cómo con conmigo conseguimos conseguir consigo consigue consiguen consigues contigo contra cual cuales cualquier cualquiera cualquieras cuancuán cuando cuanta cuánta cuantas cuántas cuanto cuánto cuantos cuántos de dejar del demás demas demasiada demasiadas demasiado demasiados  dentro desde donde dos el él ella ellas  ello ellos empleais emplean emplear empleas empleo en encima entonces entre era eramos eran eras eres es esa esas ese eso esos esta estaba estado estais estamos estan estar estas este esto estos estoy etc fin fue fueron fui fuimos gueno ha hace haceis hacemos hacen hacer haces hacia"
stopwords = stopwords + "haago hasta incluso intenta intentais intentamos intentan intentar intentas intento ir jamás junto juntos la largo las lo los mas más me menos mi mía mia mias mientras mio mío mios mis misma mismas mismo mismos modo mucha muchas muchísima muchísimas muchísimo muchísimos mucho muchos muy nada ni ningun ninguna ningunas ninguno ningunos no nos nosotras nosotros nuestra nuestras nuestro nuestros nunca os otra otras otro otros para parecer pero poca pocas poco pocos podeis podemos poder podria podriais podriamos podrian podrias por por qué porque primero primero desde puede pueden puedo pues que qué querer quien quién quienes quienes quiera quienquiera quiza quizas sabe sabeis sabemos saben saber sabes se segun ser si sí siempre siendo sin sín sino so sobre sois solamente solo somos soy sr sra sres esta su sus suya suyas suyo suyos tal tales también tambien tampoco tan tanta tantas tanto tantos te teneis tenemos tener tengo ti tiempo tiene tienen toda todas todo todos tomar trabaja"
stopwords = stopwords +  "trabajais trabajamos trabajan trabajar trabajas trabajo tras tú tu tus tuya tuyo tuyos ultimo un una unas uno unos usa usais usamos usan usar usas uso usted ustedes va vais valor vamos van varias varios vaya verdad verdadera vosotras vosotros voy vuestra vuestras vuestro vuestros y ya yo como cómo hacer se tengo"

stopwords = stopwords.split(' ')


df = pd.read_csv('Sources/test_kmeans_post.csv')
le = preprocessing.LabelEncoder()
for col in df.columns:
    if not df[col].dtype == 'O': continue
    df[col] = df[col].fillna('na')
    le.fit(df[col])
    df[col] = le.transform(df[col])

df.fillna(-1)

# k means determine k
dispercion = []
K = range(10,300,10)
for k in K:
    print(k)
    kmeanModel = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1, n_jobs=-1)
    dispercion.append(kmeanModel.fit(df).inertia_/df.shape[0])

# Plot the elbow
plt.plot(K, dispercion, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()

