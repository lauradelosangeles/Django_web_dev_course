# Wireframe de la Página `/recursos/` — Semana 3

> Un **wireframe** es un boceto de baja fidelidad que muestra la distribución de
> elementos en pantalla, sin colores ni imágenes definitivas.  
> Hacerlo *antes* de programar evita iterar sobre código cuando el problema es de diseño.

---

## Opción A — Boceto en papel (recomendada para clase)

1. Dibuja un rectángulo grande = el navegador.
2. Dibuja una barra estrecha arriba = navbar (Inicio | Acerca | Recursos).
3. Debajo: un título "Mis Recursos".
4. Dibuja tres rectángulos apilados = tarjetas de recurso.
   - Línea de texto en negrita = título (enlace).
   - Línea de texto más pequeña = descripción.
5. Al pie: una barra estrecha = footer.

**Herramienta:** papel y lápiz, o la pizarra del aula.

---

## Opción B — Herramienta digital gratuita

| Herramienta | URL | Ventaja |
|-------------|-----|---------|
| Excalidraw | https://excalidraw.com | Sin registro, exporta PNG |
| draw.io / diagrams.net | https://app.diagrams.net | Plantillas de wireframe incluidas |
| Figma (plan gratuito) | https://figma.com | Colaboración en tiempo real |

**Pasos en Excalidraw:**
1. Abre el sitio.
2. Usa el rectángulo para navbar, contenido y tarjetas.
3. Usa la herramienta de texto para etiquetar cada zona.
4. Exporta como PNG y guarda en esta carpeta como `wireframe_recursos.png`.

---

## Checklist de Usabilidad y Accesibilidad

Marca cada ítem una vez que hayas terminado el diseño y su implementación HTML.

### Jerarquía visual
- [ ] Hay un único `<h1>` por página (título principal de la sección).
- [ ] Los subtítulos usan `<h2>` o `<h3>`, nunca se usan solo para cambiar tamaño.
- [ ] El elemento más importante visualmente es el primero en el orden de lectura.

### Contraste
- [ ] El texto sobre fondo claro tiene relación de contraste ≥ 4.5:1 (WCAG AA).
- [ ] El texto sobre fondo oscuro (p. ej. navbar) también cumple ≥ 4.5:1.
- [ ] Los botones e iconos tienen contraste suficiente con su fondo.

### Imágenes
- [ ] Toda imagen de contenido tiene atributo `alt` descriptivo.
- [ ] Las imágenes decorativas usan `alt=""` para que el lector de pantalla las ignore.

### Formularios y etiquetas
- [ ] Cada campo `<input>` tiene su `<label>` asociado con `for`/`id`.
- [ ] Los mensajes de error son textos visibles, no solo cambios de color.

### HTML semántico
- [ ] El nav usa `<nav>`, el contenido principal usa `<main>`, el pie usa `<footer>`.
- [ ] Las listas de recursos usan `<ul>` o `<ol>`, no `<div>` anidados genéricos.
- [ ] Los botones de acción usan `<button>`, no `<div>` con `onclick`.

### Navegación por teclado
- [ ] Se puede tabular por todos los enlaces y botones sin usar el ratón.
- [ ] El foco visible no está eliminado (no hay `outline: none` sin reemplazo).
- [ ] Los enlaces tienen texto descriptivo ("Ver recurso" > "Clic aquí").

---

## ¿Cómo verificar el contraste?

1. Instala la extensión **axe DevTools** (Chrome/Firefox) o **WAVE**.
2. Abre tu página con `python manage.py runserver`.
3. Ejecuta el análisis y revisa los ítems marcados en rojo.
