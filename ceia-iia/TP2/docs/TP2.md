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
    El atributo con más correlación es **MedInc** (el ingreso medio en el bloque), seguido por bastante diferencia por **AveRooms** (Promedio de habitaciones por hogar) y luego **Latitude**. 

        ![Correlaciones de feature y target](../img/tp2_correlacion_target_features.png)
    
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
        
        Comparación de varianza:

            Varianza total de los datos (TSS): 12458.51
            Varianza residual (RSS): 5434.81
            Varianza explicada por el modelo (ESS): 7023.69

    1. ¿Está el modelo capturando adecuadamente el comportamiento del target? Fundamente su respuesta.
        
        Para comparar el comportamiento de la varianza del modelo respecto al target utilizamos el coeficiente de Pearson (R^2) que expresa la varianza explicada por el modelo respecto a la varianza total de los datos. 
         - **Coeficiente de determinación (R^2)**: 0.5638
        
        Con un coeficiente R2 de 0.5638 podemos decir que el modelo no se ajusta correctamente a la varianza de los datos, explicando solo parcialmente estos. Se puede mejorar bastante. 

1. Calcular las métricas de MSE, MAE y R² sobre el conjunto de evaluación.

    El código y la obtención de las métricas se encuentra en el [notebook principal](../notebooks/california_housing_regression.ipynb)

        Resultados para regresión lineal:
        R²: 0.5953
        MSE: 0.3697
        MAE: 0.4602

2. Crear una regresión de Ridge. 
    1. Usar validación cruzada de 5 folds y tomar como métrica el MSE. 

        Ejecutado en código en notebook.

    2. Buscar el mejor valor de α en el rango [0, 12.5].
        
            Mejor alpha: 6.6373
            MSE promedio con mejor alpha: 0.5268
    3. Graficar el MSE en función de α.
    ![grafico de alfa](../img/tp2_alpha_search.png)
 
3. Comparar los resultados obtenidos entre la regresión lineal y la mejor regresión de Ridge, evaluando el conjunto de prueba.
    1. ¿Cuál de los dos modelos obtiene mejores resultados en términos de MSE y MAE? ¿Poseen suficiente diferencia como para indicar si uno es mejor que el otro?
    
        ![tabla de resultados](../img/tp2_result_comparison.png)
        
        Como se observa en la tabla, ambos modelos arrojan resultados similares. Si bien bastante superiores al baseline de comparación (media como aproximación), no presentan grandes diferencias entre ellos. 

    2. ¿Qué tipo de error podría haberse reducido?

        El error que se debería reducir es el MSE, ya que la búsqueda de alfa consiste en buscar el punto en el que el error por varianza y el error por sesgo intersectan, dando un MSE mínimo. Se presenta una reducción, pero es mínima. 

## Análisis adicional

Con el fin de explorar una posibilidad de mejora del modelo se evalua que pasaría utilizando los modelos pero retirando los outliers del dataset antes de entrenarlo:

![boxplot medhouse val](../img/tp2_boxplot_houseval.png)

Retirando los outliers, cambiamos el dataset a: 

    Cantidad con outliers: 20640
    Cantidad sin outliers: 19569

Con este nuevo dataset, entrenamos los modelos nuevamente, y lo ponemos a prueba contra el set de test: 

![tabla de resultados adicional](../img/tp2_result_comparison_adicional.png)

Con estos nuevos  modelos se reduce el MSE y MAE, probablemente porque, si recordamos la distribución de MedHouseVal, estamos reduciendo el impacto que tienen en la regresión los datos acumulados en el extremo superior de los valores. 

Si bien esto reduce el error del modelo, empeoraría su capacidad de predecir estos precios extremos. 
