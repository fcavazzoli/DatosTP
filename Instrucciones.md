# Instrucciones

  Las siguientes instrucciones son necesarias para poder generar los archivos necesarios para luego correr
  el cualquiera de los programas de entrenamiento y prediccion que hemos utilizado. En primera instancia es
  necesario tener una carpeta Sources, que es donde se deben encontrar los archivos base y donde se
  se generaran todos los archivos necesarios

  ## Concatenar Archivos
  
    Para concatenar los diverentes archivos otorgados por navent, debemos correr el notebook Concat.ipynb
    
  ## Preparar Postulantes
  
    Corremos el notebook OrganizacionEducacion.ipynb para organizar la informaciones que tenemos sobre la 
    educacion de los postulantes para asi poder usarla de forma mas eficiente mas adelante
    
  ## Preparar Visitas
  
    Obtenemos la suma de las visitas corriendo el notebook OrganizacionVisitas.ipynb
    
  ## Preparar Avisos
  ### Obtener Mas Features
  
    Es necesario correr el notebook PostulacionesFeaturesExtra.ipynb para generar los features extras que
    se agregaran a los detalles de los avisos
    
  ### Limpiar Avisos y Agregar Features
  
    Por ultimo corremos el notebook Modificador de descripciones.ipynb
    
  ## Generar Dataset de Training
  
    Finalmente generamos el DataSet con postulaciones y no postulaciones que luego usaremos para entrenar 
    corriendo el notebook PostulacionesTraining.ipynb
    
 Una vez seguido estos pasos podremos correr cualquiera de los notebooks que entrenan los algoritmos que
 utilizamos para realizar las predicciones que subimos a Kaggle.
