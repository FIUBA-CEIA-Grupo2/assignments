# Trabajo Práctico N°2 - Introducción a Inteligencia Artificial | Regresión del valor de valor medio de casas en distritos de California

## Enunciado:

Se requiere construir un modelo de regresión que permita predecir el valor medio de las casas en distintos distritos de California, EE. UU. (medido en cientos de miles de dólares, es decir, $100,000). Este conjunto de datos proviene del censo de EE. UU. de 1990, donde cada observación corresponde a un bloque. Un bloque es la unidad geográfica más pequeña para la cual la Oficina del Censo de EE. UU. publica datos de muestra, y típicamente tiene una población de entre 600 y 3.000 personas.

Los atributos, en el orden en que se presentan en el conjunto de datos, son:

- MedInc: Ingreso medio en el bloque
- HouseAge: Edad mediana de las casas en el bloque
- AveRooms: Número promedio de habitaciones por hogar
- AveBedrms: Número promedio de dormitorios por hogar
- Population: Población del bloque
- AveOccup: Número promedio de personas por hogar
- Latitude: Latitud del bloque
- Longitude: Longitud del bloque

El target es:

- MedHouseVal: Mediana del valor de las casas en el bloque (en unidades de $100,000)

## Tareas y preguntas a resolver:

1. Obtener la correlación entre los atributos y entre los atributos y el target.
    1. ¿Qué atributo tiene mayor correlación lineal con el target?
    ![Correlaciones de feature y target](../img/tp2_correlacion_target_features.png)
    El atributo con más correlación es **MedInc** (el ingreso medio en el bloque), seguido por bastante diferencia por **AveRooms** (Promedio de habitaciones por hogar) y luego **Latitude**. 
    
    2. ¿Cuáles atributos parecen estar más correlacionados entre sí? Se pueden calcular los coeficientes de correlación o representarlos gráficamente mediante un mapa de calor.
    ![Mapa de calor de features](../img/tp2_heat_map.png)
    Los atributos mas correlacionados entre si son: **Latitude y Longitude** geográficas, luego la **cantidad promedio de habitaciones (AveRooms) y la de dormitorios (AveBedrms)**, la **cantidad de habitaciones (AveRooms) y el ingreso promedio del bloque (MedInc)**. 
    Podemos además ver estas distribuciones en un pairplot: 
    ![Pairplot de features](../img/tp2_pairplot_kde.png)
2. Graficar los histogramas de los distintos atributos y del target. 
    1. ¿Qué forma presentan los histogramas?
    ![Histogramas](../img/tp2_histogramas.png)
    Por feature: 
        - **MedInc**: Distribución aproximadamente normal con leve sesgo a la derecha. Caben destacar algunos outliers muy pronunciados. 
        - **HouseAge**: Distribución aproximadamente normal con picos muy pronunciados en determinados rangos. 
        - **AveRooms, AveBedrms, Population, AveOccup**: distribuciones muy concentradas. 
        - **Latitude y Longitud**: Distribuciones con cierta aproximación a la bimodal con un pico muy pronunciado en cada una de ellas. 
        - **MedHouseVal**: Distribución sesgada a la derecha, con un pico muy pronunciado que debe analizarse si es outlier. 
    2. ¿Alguno muestra una distribución similar a una campana que sugiera una distribución gaussiana, sin necesidad de realizar pruebas de hipótesis?
    
        Como se mencionó: **MedInc y MedHouseVal** tienen distribuciones similares a la gaussiana, con la salvedad de que MedHouseVal ademas tiene un pico muy pronunciado en sus valores mas altos. 

3. Calcular una regresión lineal utilizando todos los atributos. 
    1. Con el conjunto de entrenamiento, calcular la varianza total de los datos y la varianza explicada por el modelo. 
    2. ¿Está el modelo capturando adecuadamente el comportamiento del target? Fundamente su respuesta.
4. Calcular las métricas de MSE, MAE y R² sobre el conjunto de evaluación.
5. Crear una regresión de Ridge. 
    1. Usar validación cruzada de 5 folds y tomar como métrica el MSE.
    2. Buscar el mejor valor de α en el rango [0, 12.5].
    3. Graficar el MSE en función de α.
6. Comparar los resultados obtenidos entre la regresión lineal y la mejor regresión de Ridge, evaluando el conjunto de prueba.
    1. ¿Cuál de los dos modelos obtiene mejores resultados en términos de MSE y MAE? ¿Poseen suficiente diferencia como para indicar si uno es mejor que el otro?
    2. ¿Qué tipo de error podría haberse reducido?