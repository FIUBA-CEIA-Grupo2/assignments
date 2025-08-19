# Consigna QDA

**Notación**: en general notamos

* $k$ la cantidad de clases
* $n$ la cantidad de observaciones
* $p$ la cantidad de features/variables/predictores

**Sugerencia:** combinaciones adecuadas de `transpose`, `stack`, `reshape` y, ocasionalmente, `flatten` y `diagonal` suele ser más que suficiente. Se recomienda *fuertemente* explorar la dimensionalidad de cada elemento antes de implementar las clases.

## Tensorización

En esta sección nos vamos a ocupar de hacer que el modelo sea más rápido para generar predicciones, observando que incurre en un doble `for` dado que predice en forma individual un escalar para cada observación, para cada clase. Paralelizar ambos vía tensorización suena como una gran vía de mejora de tiempos.

### 1) Diferencias entre `QDA`y `TensorizedQDA`

1. **¿Sobre qué paraleliza `TensorizedQDA`? ¿Sobre las $k$ clases, las $n$ observaciones a predecir, o ambas?**

    Paraleliza sobre las k clases, porque a pesar de formar un tensor de dimensiones $(k, p, p)$ para la matriz de covarianzas y uno de $(k, p, 1)$ para el tensor de medias de las features, de todas formas cada observación se evalua individualmente con el método `_predict_one`.

2. **Analizar los shapes de `tensor_inv_covs` y `tensor_means` y explicar paso a paso cómo es que `TensorizedQDA` llega a predecir lo mismo que `QDA`.**
    
    Los shapes de los tensores son: 
    * `tensor_inv_covs`: $(k, p, p)$
    * `tensor_means`: $(k, p, 1)$
  
    La predicción se realiza de forma equivalente porque: 

### 2) Optimización

Debido a la forma cuadrática de QDA, no se puede predecir para $n$ observaciones en una sola pasada (utilizar $X \in \mathbb{R}^{p \times n}$ en vez de $x \in \mathbb{R}^p$) sin pasar por una matriz de $n \times n$ en donde se computan todas las interacciones entre observaciones. Se puede acceder al resultado recuperando sólo la diagonal de dicha matriz, pero resulta ineficiente en tiempo y (especialmente) en memoria. Aún así, es *posible* que el modelo funcione más rápido.

3. **Implementar el modelo `FasterQDA` (se recomienda heredarlo de `TensorizedQDA`) de manera de eliminar el ciclo for en el método predict.**
   
   
   Ver en [notebook](../notebooks/AMIA_2025_TP1.ipynb)
4. **Mostrar dónde aparece la mencionada matriz de $n \times n$, donde $n$ es la cantidad de observaciones a predecir.**

![alt text](../img/img_amia_tp1_1.png)

5. Demostrar que

    $$
    diag(A \cdot B) = \sum_{cols} A \odot B^T = np.sum(A \odot B^T, axis=1)
    $$
    es decir, que se puede "esquivar" la matriz de $n \times n$ usando matrices de $n \times p$. 

    También se puede usar, de forma equivalente,
    $$
    np.sum(A^T \odot B, axis=0).T
    $$
    queda a preferencia del alumno cuál usar.

    [Demostración](../docs/demostracion_amia_tp1_ej5.pdf)

6. **Utilizar la propiedad antes demostrada para reimplementar la predicción del modelo `FasterQDA` de forma eficiente en un nuevo modelo `EfficientQDA`.**

    Resuelto en notebook.

7. **Comparar la performance de las 4 variantes de QDA implementadas hasta ahora (no Cholesky) ¿Qué se observa? A modo de opinión ¿Se condice con lo esperado?**

    ![alttext](../img/img_amia_tp1_2_comparison.png)

    Podemos ver en estos gráficos que en Train no se ve diferencia alguna entre las implementaciones. En Test por otro lado vemos tiempos mucho mas grandes en el `QDA` baseline e incluso el `TensorizedQDA`, con el mas corto siendo el `EfficientQDA`. 

    En términos de uso de memoria `FasterQDA` es, considerablemente, el más problemático debido a su cálculo de matrices nxn. Esto se ve bastante amortiguado con la implementación realizada en `EfficientQDA`. 

    Por último, en terminos de accuracy, los 4 modelos se mueven dentro de un rango muy similar, por lo que no se destacan grandes diferencias en esto. 



### 3) Diferencias entre implementaciones de `QDA_Chol`

8. **Si una matriz $A$ tiene fact. de Cholesky $A=LL^T$, expresar $A^{-1}$ en términos de $L$. ¿Cómo podría esto ser útil en la forma cuadrática de QDA?**
    
    En QDA, la forma cuadrática es  

    $$
    (x-\mu)^\top \Sigma^{-1} (x-\mu).
    $$

    Si $\Sigma = LL^\top$, no conviene invertir $\Sigma$ explícitamente. En su lugar, resolvemos sistemas triangulares:  

    $$
    v = L^{-1}(x-\mu), \qquad
    (x-\mu)^\top \Sigma^{-1} (x-\mu) = \|v\|_2^2.
    $$

    Esto es útil porque evitamos calcular la matriz inversa de covarianzas explicitamente. 

9.  Explicar las diferencias entre `QDA_Chol1`y `QDA` y cómo `QDA_Chol1` llega, paso a paso, hasta las predicciones.



10. ¿Cuáles son las diferencias entre `QDA_Chol1`, `QDA_Chol2` y `QDA_Chol3`?



11. Comparar la performance de las 7 variantes de QDA implementadas hasta ahora ¿Qué se observa?¿Hay alguna de las implementaciones de `QDA_Chol` que sea claramente mejor que las demás?¿Alguna que sea peor?




### 4) Optimización

12. Implementar el modelo `TensorizedChol` paralelizando sobre clases/observaciones según corresponda. Se recomienda heredarlo de alguna de las implementaciones de `QDA_Chol`, aunque la elección de cuál de ellas queda a cargo del alumno según lo observado en los benchmarks de puntos anteriores.
13. Implementar el modelo `EfficientChol` combinando los insights de `EfficientQDA` y `TensorizedChol`. Si se desea, se puede implementar `FasterChol` como ayuda, pero no se contempla para el punto.
14. Comparar la performance de las 9 variantes de QDA implementadas ¿Qué se observa? A modo de opinión ¿Se condice con lo esperado?
