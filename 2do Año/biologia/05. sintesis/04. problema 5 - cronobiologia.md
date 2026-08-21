# Síntesis para resolver el problema de Cronobiología

> Recorte de la Clase 4 (+ herramientas moleculares de la Clase 2) con **solo lo necesario** para responder las consignas del PDF (Problema 5 de la Guía 1).
> **El modelo:** mutantes del gen ***doubletime* (dbt)** en *Drosophila*, que alteran el **período (τ)** de la **actividad locomotora** medida en **oscuridad constante (DD)**. Alelos: **+** (wt, τ = 24 h), **dbtS** ("short", acorta τ) y **dbtL** ("long", alarga τ).

## 0. Caja de herramientas mínima (la usás en todo)

**T vs. τ (tau).** **T** = período del ritmo **manifiesto** (con señales ambientales, ≈ 24 h porque el ambiente lo fuerza). **τ** = período del ritmo **endógeno**, el del reloj funcionando **solo**, sin pistas externas. Medir τ exige **aislar** al organismo de zeitgebers.

**Por qué se mide en oscuridad constante (DD).** En DD no hay luz que sincronice, así que se observa el **ritmo endógeno (τ)**. Con un ciclo luz-oscuridad solo se vería si falla el **sistema de sincronización**, no si falla el **reloj endógeno** mismo (es la lógica del experimento de **libre curso / free-running**).

**El reloj molecular (TTFL) y dónde entra *dbt*.** Un bucle de retroalimentación transcripción–traducción de ~24 h: **CLOCK+BMAL1** (brazo activador) inducen *period (per)* y *cry*; **PER+CRY** se acumulan, entran al núcleo e **inhiben** a CLOCK/BMAL1 (retroalimentación negativa). El gen ***dbt* codifica una caseína quinasa** que **fosforila a PER y regula su acumulación/degradación**, **ajustando el período a ~24 h**. Por eso una versión "rápida" (**dbtS**) acorta τ y una "lenta" (**dbtL**) lo alarga.

**Dogma central (por qué una mutación afecta la conducta).** `ADN → ARN → proteína → función → comportamiento`. Una mutación cambia el **gen *dbt*** → cambia la **quinasa** → cambia la regulación de PER → cambia el **período del reloj** → cambia el **ritmo de actividad** (conducta). *(Ojo: "mutación" afecta el **código genético**, no es el paso de ADN a ARN.)*

**Herencia: dominancia incompleta.** Ningún alelo enmascara totalmente al otro → **cada genotipo tiene un fenotipo distinto** (un τ distinto). Por eso wt, heterocigota y homocigota se diferencian.

**Gametas y cuadro de Punnett.** Cada mosca aporta un alelo por gameta; el cuadro cruza las gametas posibles del macho × las de la hembra para dar genotipos y proporciones.

---

## 1. ¿Por qué evaluar la actividad locomotora en oscuridad constante?

Para ver los **ritmos endógenos** (el reloj corriendo en **libre curso**, con su τ). Un ciclo luz-oscuridad permitiría detectar fallas en la **sincronización**, pero **no** fallas en el **reloj endógeno**; en DD se aísla justamente el período propio del oscilador.

## 2. ¿Por qué una mutación en el ADN afecta el comportamiento? (dogma central)

`ADN → (transcripción) ARN → (traducción) proteína → función → comportamiento`. La mutación en *dbt* altera la **proteína quinasa** que ajusta a PER → cambia el **período** del reloj molecular → repercute en el **ritmo de actividad locomotora**. *(Aclaración del enunciado: la mutación afecta la **secuencia del código genético**, no el pasaje de ADN a ARN.)*

## 3. ¿Por qué wt, heterocigota y homocigota tienen fenotipos distintos?

Por **dominancia incompleta**: ningún alelo domina por completo al otro, de modo que **cada genotipo da un fenotipo diferente** (un valor de τ distinto). No hay un alelo que "tape" al otro como en la dominancia simple.

## 4. ¿Cuántos tipos de gametas produce cada mosca (respecto del gen *dbt*)?

- Mosca **dbtS/+** → **2** tipos de gametas (una **dbtS** y una **+**).
- Mosca **dbtS/dbtS** → **1** tipo de gameta (**dbtS**).

*(Regla general: un heterocigota produce 2 tipos; un homocigota, 1.)*

## 5. Cruce macho dbtS/+ × hembra dbtS/+ — fenotipos y proporciones

|  | **dbtS** | **+** |
|---|---|---|
| **dbtS** | dbtS/dbtS | dbtS/+ |
| **+** | dbtS/+ | +/+ |

Genotipos **1 : 2 : 1** → por dominancia incompleta, **tres fenotipos**:
- **25 %** dbtS/dbtS → **período muy corto (τ = 18 h)**
- **50 %** dbtS/+ → **período corto (τ = 21,5 h)**
- **25 %** +/+ → **período normal (τ = 24 h)**

## 6. Cruce macho dbtL/+ × hembra +/+ — fenotipos y proporciones

|  | **dbtL** | **+** |
|---|---|---|
| **+** | dbtL/+ | +/+ |
| **+** | dbtL/+ | +/+ |

→ **Dos fenotipos**:
- **50 %** dbtL/+ → **período largo (τ = 25 h)**
- **50 %** +/+ → **período normal (τ = 24 h)**

---

## Cierre lógico del problema (frase-resumen)

El experimento mide **τ en oscuridad constante** porque solo así se ve el **reloj endógeno**. *dbt* codifica la **quinasa que ajusta a PER** dentro del bucle **TTFL**, así que una mutación en ese gen —vía **dogma central** (gen → proteína → función → conducta)— **cambia el período del ritmo de actividad**. Como la herencia es de **dominancia incompleta**, cada genotipo (wt / heterocigota / homocigota) muestra un **τ propio**, y las proporciones de los cruces se predicen con **gametas + cuadro de Punnett**. En una frase: *el gen del reloj **causa** el ritmo conductual, y su herencia se lee con las mismas reglas mendelianas (matizadas por dominancia incompleta).*
