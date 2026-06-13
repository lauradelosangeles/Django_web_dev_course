# Módulo 1: Fundamentos de HTML y CSS — El Perfil Estático del Docente

---

## Diapositiva 1: ¿Qué Construiremos? Conoce el Proyecto del Curso
- **Conceptos:**
  - El proyecto hilo conductor: **Hub Personal del Docente** (perfil, recursos, contacto)
  - Recorrido semana a semana: HTML puro → Django → Plantillas → Base de datos → Formularios
  - Hoy la información está escrita a mano; al final del curso Django la servirá desde una base de datos
- **Fragmento de Código Recomendado:**
```html
<!-- Semana 1: datos escritos directamente en HTML -->
<h1 class="perfil-nombre">Prof. González Silva</h1>

<!-- Semana 4 (adelanto): Django los traerá de la BD -->
<h1>{{ docente.nombre }}</h1>
```

---

## Diapositiva 2: Variables CSS — Un Sistema de Diseño en 10 Líneas
- **Conceptos:**
  - `--nombre-variable: valor;` dentro de `:root` → disponibles en todo el archivo
  - Cambia el color una vez, se propaga a todos los elementos
  - Convención de nombres semánticos: `--azul-institucional`, `--naranja-acento`
- **Fragmento de Código Recomendado:**
```css
:root {
  --azul-institucional: #1A5F7A;
  --naranja-acento:     #E86B5F;
  --color-fondo:        #F0F5F5;
  --radio-borde:        12px;
  --sombra-tarjeta:     0 4px 20px rgba(0,0,0,0.08);
}

.boton-principal {
  background-color: var(--naranja-acento); /* reutiliza la variable */
}
```

---

## Diapositiva 3: El Reset CSS y el Box Model
- **Conceptos:**
  - Los navegadores tienen estilos por defecto distintos — el reset los unifica
  - `box-sizing: border-box` → `padding` y `border` NO aumentan el tamaño del elemento
  - `margin: 0 auto` → centra un bloque horizontalmente
- **Fragmento de Código Recomendado:**
```css
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.contenedor-centrado {
  max-width: var(--ancho-maximo); /* 900px */
  margin: 0 auto;   /* centrado horizontal */
  padding: 0 24px;
}
```

---

## Diapositiva 4: Flexbox — Navegación y Layouts en Fila
- **Conceptos:**
  - `display: flex` → los hijos se alinean en fila por defecto
  - `justify-content: space-between` → empuja elementos a los extremos
  - `align-items: center` → alinea verticalmente al centro
  - `flex-wrap: wrap` → los elementos se reorganizan solos en pantallas pequeñas
- **Fragmento de Código Recomendado:**
```css
/* Logo a la izquierda, menú a la derecha */
.barra-navegacion .contenedor-centrado {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Los enlaces del menú van en fila con espacio entre ellos */
.menu-principal {
  display: flex;
  gap: 28px;
}
```

---

## Diapositiva 5: Tarjetas con Hover — CSS sin una Línea de JavaScript
- **Conceptos:**
  - `transition: transform 0.2s` → animación suave al pasar el cursor
  - `transform: translateY(-5px)` → la tarjeta "sube" al hacer hover
  - `flex: 1 1 180px` → la tarjeta crece, se encoge, con base de 180px (responsive automático)
- **Fragmento de Código Recomendado:**
```css
.tarjeta-materia {
  flex: 1 1 180px;
  max-width: 220px;
  border-top: 4px solid var(--naranja-acento);
  transition: transform 0.2s;
}

.tarjeta-materia:hover {
  transform: translateY(-5px); /* sube 5px al pasar el mouse */
}
```

---

## Diapositiva 6: Diseño Responsivo con Media Queries
- **Conceptos:**
  - `@media (max-width: 600px)` → los estilos dentro aplican **solo** en pantallas ≤ 600px
  - Un solo "punto de quiebre" es suficiente para proyectos pequeños
  - `display: none` en el menú → lo ocultamos en móvil para no saturar
- **Fragmento de Código Recomendado:**
```css
@media (max-width: 600px) {

  .menu-principal { display: none; } /* menú oculto en móvil */

  .perfil-nombre  { font-size: 1.75rem; }

  /* Las tarjetas ocupan todo el ancho disponible */
  .tarjeta-materia { max-width: 100%; }
  .tarjeta-recurso { max-width: 100%; }
}
```

---

## Diapositiva 7: El "Puente" hacia Django — Lo que Cambia la Semana Próxima
- **Conceptos:**
  - Hoy los datos están **escritos a mano** en el HTML → frágil, no escala
  - Django separa los **datos** (Python/BD) de la **presentación** (HTML)
  - Los comentarios `← Django: {{ ... }}` ya anticipan la sintaxis futura
- **Fragmento de Código Recomendado:**
```html
<!-- HOY (HTML estático):         SEMANA 2 (Django dinámico): -->

<h1>Prof. González Silva</h1>  →  <h1>{{ docente.nombre }}</h1>
<span>10</span>                →  <span>{{ docente.anos }}</span>

<!-- 3 tarjetas escritas a mano  →  loop automático -->
<!-- {% for m in materias %}
       <article class="tarjeta-materia">{{ m.nombre }}</article>
     {% endfor %} -->
```

---

## Diapositiva 8: Demo en Vivo — Recorrido del Archivo `perfil.html`
- **Conceptos:**
  - Archivo de referencia: `semana_1/demo/finalizado/perfil.html`
  - La sesión recorre las secciones en orden: Navbar → Hero → Estadísticas → Materias → Recursos → Contacto → Footer
  - Cada bloque tiene comentarios explicativos que guían la lectura del código
- **Fragmento de Código Recomendado:**
```html
<!-- Estructura completa del demo — 6 secciones -->
<header class="barra-navegacion">…</header>
<main>
  <section class="seccion-hero"         id="inicio">…</section>
  <section class="seccion-estadisticas">…</section>
  <section class="seccion-contenido"    id="acerca">…</section>
  <section class="seccion-contenido fondo-alterno" id="materias">…</section>
  <section class="seccion-contenido"    id="recursos">…</section>
  <section class="seccion-contenido fondo-alterno" id="contacto">…</section>
</main>
<footer class="pie-pagina">…</footer>
```

---

## Diapositiva 9: Trabajo en Clase — Personaliza tu Perfil (20 min)
- **Conceptos:**
  - Archivo de trabajo: `semana_1/ejercicio_clase/plantilla/ejercicio.html`
  - Abre el demo en una pestaña y el ejercicio en otra para comparar mientras trabajas
  - Los `TODO` están numerados del ① al ③ — trabaja en orden
- **Fragmento de Código Recomendado:**
```html
<!-- EJERCICIO 1 (6 cambios) → Personaliza los datos del docente -->
<!-- Busca "TODO EJ1" en el archivo -->
<title>Prof. ??? — ??? | Perfil Docente</title>
<span class="logo-nombre">Prof. González Silva</span> <!-- → tu nombre -->
<div class="perfil-avatar">PG</div>                   <!-- → tus iniciales -->

<!-- EJERCICIO 2 (4 bloques) → Completa secciones vacías -->
<!-- Estadística 3, texto Acerca, cita, tercera tarjeta de materia -->

<!-- EJERCICIO 3 (2 bloques) → Agrega tus recursos favoritos -->
<!-- Copia la tarjeta-recurso completa y cambia URL, emoji y texto -->
```

---

## Diapositiva 10: Tarea y Entregables
- **Conceptos:**
  - Archivo de tarea: `semana_1/tarea/plantilla_tarea/tarea.html`
  - A diferencia del ejercicio, aquí construyes **todas las secciones desde cero**
  - Usa el demo como referencia visual, pero escribe tu propio contenido
- **Fragmento de Código Recomendado:**
```
TAREA 1 → Completa TODAS las secciones del HTML
          Busca "TAREA 1" — 15 puntos en el archivo
          (navbar, hero, estadísticas, acerca, materias, recursos, contacto)

TAREA 2 → Personaliza la paleta de colores en :root
          Cambia --azul-institucional y --naranja-acento
          Herramienta sugerida: https://coolors.co

──────────────────────────────────────────────────
ENTREGA:  tarea.html funcionando en el navegador
          con tu información real y tu paleta propia

CRITERIO: ¿Aparece tu nombre? ¿3 estadísticas?
          ¿3 materias? ¿3 recursos? ¿Colores propios?
```
