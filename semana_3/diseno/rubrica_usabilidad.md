# Rúbrica de Autoevaluación — Usabilidad y Accesibilidad

> Usa esta rúbrica para evaluar tu propia página `/recursos/` antes de entregarla.
> También puede ser utilizada por el docente como criterio de calificación.

---

## Instrucciones

Para cada criterio, marca la columna que mejor describe el estado actual de tu página.  
Suma los puntos al final para obtener tu puntaje total (máximo 15 puntos).

---

## Tabla de Criterios

| # | Criterio | Logrado (3 pts) | En proceso (2 pts) | Falta (1 pt) |
|---|----------|-----------------|--------------------|--------------|
| 1 | **Jerarquía de encabezados** | La página tiene un único `<h1>` y los subtítulos siguen el orden correcto `<h2>`, `<h3>`. | Hay `<h1>` pero algunos subtítulos saltan niveles (p. ej., de `<h1>` a `<h4>`). | No hay encabezados semánticos; el texto usa solo `<p>` con tamaño aumentado. |
| 2 | **Contraste de texto** | Todo el texto visible supera la relación 4.5:1 contra su fondo (verificado con herramienta). | La mayoría cumple, pero algún texto secundario (p. ej., descripción en gris) falla. | El texto principal no supera 3:1; difícil de leer sin esfuerzo. |
| 3 | **Atributo `alt` en imágenes** | Todas las imágenes de contenido tienen `alt` descriptivo; las decorativas tienen `alt=""`. | La mayoría tiene `alt`, pero alguna imagen de contenido lo omite. | No hay atributo `alt` en ninguna imagen. |
| 4 | **Etiquetas `<label>` en campos** | Cada campo de entrada tiene su `<label>` con `for` e `id` correctos; el lector de pantalla los asocia. | Hay `<label>` pero sin el atributo `for`/`id`, o el texto es poco descriptivo. | Los campos no tienen `<label>` en absoluto. |
| 5 | **Navegación por teclado** | Todos los enlaces y botones son alcanzables con la tecla Tab; el foco es visible en pantalla. | La mayoría es accesible por teclado, pero algún elemento interactivo queda inaccesible. | El sitio no es navegable sin ratón; el foco está oculto o la secuencia es incoherente. |

---

## Puntaje

| Rango | Nivel |
|-------|-------|
| 13 – 15 | Excelente — listo para presentar |
| 9 – 12 | Suficiente — corrige los ítems en proceso antes de entregar |
| 5 – 8 | Insuficiente — revisa la sección de accesibilidad del wireframe y vuelve a evaluar |

---

## Próximos pasos

- Los ítems con "Falta" son los de mayor impacto; corrígelos primero.
- Usa el prompt de Cursor AI de la semana para obtener sugerencias específicas de código.
- Guarda una captura de pantalla del resultado del escáner axe/WAVE junto con esta rúbrica.
