# Alineación Curricular — Bachillerato Técnico "Desarrollo de Software"
### Ministerio de Educación del Ecuador

> **Propósito de este documento:** mostrar de forma explícita y verificable cómo
> cada semana del curso "Desarrollo Web con Python y Django — Hub Personal del Docente"
> cubre las competencias, destrezas con criterio de desempeño y ejes transversales
> del currículo oficial del Bachillerato Técnico en Desarrollo de Software.
>
> Audiencia: docentes del bachillerato técnico, coordinadores académicos y asesores
> del Ministerio que necesiten evidencia de pertinencia curricular.

---

## 1. Marco curricular de referencia

El Bachillerato Técnico "Desarrollo de Software" se articula dentro del marco del
**Currículo del Sistema Nacional de Educación — Bachillerato Técnico**
(Ministerio de Educación, actualización 2022-2024). Las competencias de la figura
profesional "Desarrollo de Software" se agrupan en cuatro módulos formativos:

| Módulo | Nombre | Relación con el curso |
|--------|--------|-----------------------|
| **MF01** | Sistemas informáticos y redes | Base de entorno de desarrollo (Python, pip, localhost) |
| **MF02** | Programación orientada a objetos | Clases Python, modelos Django, ORM |
| **MF03** | Desarrollo de aplicaciones web | HTML/CSS, Django MTV, formularios, despliegue |
| **MF04** | Gestión de bases de datos | SQLite, ORM, migraciones, admin CRUD |

Adicionalmente, el currículo integra **ejes transversales** que este curso incorpora
explícitamente con los archivos de la rama `alineacion-curricular`:

- Análisis de requerimientos y diseño previo
- Control de versiones como práctica profesional
- Pruebas de software (unitarias y funcionales)
- Documentación técnica y de usuario
- Ética digital y protección de datos personales

---

## 2. Mapa de cobertura semana × competencia curricular

La siguiente tabla cruza cada semana del curso con las destrezas del currículo.
La columna **Evidencia en el repo** indica el archivo o carpeta exacta donde se
materializa la cobertura.

### Semana 1 — HTML, CSS y Programación Orientada a Objetos

| Destreza / Competencia curricular | Cobertura en el curso | Evidencia en el repo |
|-----------------------------------|-----------------------|----------------------|
| Aplica fundamentos de HTML semántico para estructurar páginas web | Construcción de `perfil.html` con etiquetas semánticas (`<header>`, `<section>`, `<footer>`) | `semana_1/demo/finalizado/docente.html` |
| Usa selectores CSS y variables de diseño para estilizar interfaces | Variables CSS `--color-primario`, Bootstrap 5 CDN, flexbox | `semana_1/demo/finalizado/estilos.css` |
| Define clases, atributos e instancias en Python (POO) | Clase `Docente` con `__init__`, `presentarse()`, `describir_materias()` | `semana_1/demo/finalizado/docente.py` |
| Comprende la diferencia entre código estático y dinámico | Progresión: HTML estático → Django dinámico (adelanto en módulo 1) | `recursos_adicionales/modulo_01_html_css.md` |

### Semana 2 — Django, Vistas y Enrutamiento

| Destreza / Competencia curricular | Cobertura en el curso | Evidencia en el repo |
|-----------------------------------|-----------------------|----------------------|
| Instala y configura un framework web en entorno virtual | `python -m venv`, `pip install Django==4.2`, `startproject`, `startapp` | `semana_2/demo/finalizado/` |
| Comprende el patrón MTV (Modelo-Template-Vista) de Django | Flujo: URL → View → HttpResponse explicado en módulo 2 | `recursos_adicionales/modulo_02_django_fundamentos.md` |
| Crea rutas HTTP con `path()` e `include()` | `hub/urls.py` + `hub_docente/urls.py` con delegación `include()` | `semana_2/demo/finalizado/hub/urls.py` |
| Produce respuestas HTTP dinámicas desde Python | Vistas `inicio()`, `acerca()` con `HttpResponse` y f-strings | `semana_2/demo/finalizado/hub/views.py` |

### Semana 3 — Plantillas Dinámicas, Diseño UI y Accesibilidad

| Destreza / Competencia curricular | Cobertura en el curso | Evidencia en el repo |
|-----------------------------------|-----------------------|----------------------|
| Aplica herencia de plantillas para reutilizar estructura HTML | `base.html` con `{% block %}` y plantillas hijas con `{% extends %}` | `semana_3/demo/finalizado/templates/base.html` |
| Usa el motor de plantillas para separar lógica de presentación | `render()`, contexto diccionario, `{{ variable }}`, `{% for %}` | `semana_3/demo/finalizado/hub/views.py` |
| **Analiza requisitos funcionales y no funcionales** *(eje transversal)* | Tabla requisitos con criterios de aceptación, 4 ejemplos y 3 filas para completar | `semana_3/diseno/requisitos.md` |
| **Diseña la interfaz antes de programar** *(eje transversal)* | Instrucciones de wireframe en papel/Excalidraw + checklist usabilidad | `semana_3/diseno/wireframe_recursos.md` |
| **Evalúa accesibilidad web** (WCAG AA, atributo alt, contraste, navegación por teclado) *(eje transversal)* | Rúbrica de autoevaluación 5 criterios × 3 niveles | `semana_3/diseno/rubrica_usabilidad.md` |
| Implementa framework CSS (Bootstrap 5) para diseño responsive | navbar, tarjetas Bootstrap, grid system | `semana_3/demo/finalizado/templates/base.html` |

### Semana 4 — Bases de Datos, ORM, Diseño de Datos y Pruebas

| Destreza / Competencia curricular | Cobertura en el curso | Evidencia en el repo |
|-----------------------------------|-----------------------|----------------------|
| Define modelos relacionales y los implementa en Python | Clases `Recurso` y `Mensaje` con campos tipados, Meta y `__str__` | `semana_4/demo/finalizado/hub/models.py` |
| Aplica el proceso migración para versionar el esquema de BD | `makemigrations` + `migrate` con flujo documentado; migración generada | `semana_4/demo/finalizado/hub/migrations/0001_initial.py` |
| Usa el ORM para operaciones CRUD sin escribir SQL | `Recurso.objects.all()`, `.create()`, `.filter()` en vistas y admin | `semana_4/demo/finalizado/hub/views.py` |
| Configura el panel de administración Django | `@admin.register()`, `list_display`, `search_fields`, `list_filter` | `semana_4/demo/finalizado/hub/admin.py` |
| **Diseña el modelo entidad-relación antes de codificar** *(eje transversal)* | Plantilla E/R con 2 tablas, tipos de dato, claves, diagrama ASCII | `semana_4/diseno/modelo_datos.md` |
| **Escribe historias de usuario** para centrar el diseño en el actor *(eje transversal)* | 3 historias "Como docente quiero…" con criterios de aceptación | `semana_4/diseno/historias_usuario.md` |
| **Escribe y ejecuta pruebas unitarias con `TestCase`** *(eje transversal)* | 2 pruebas: `test_creacion_recurso` y `test_str_devuelve_titulo` — **OK** | `semana_4/demo/finalizado/hub/tests.py` |
| **Aplica control de versiones profesional con Git** *(eje transversal)* | Convención feat/fix/docs/test, ramas por semana, `git log --oneline` | `GUIA_GIT.md` (raíz) |

### Semana 5 — Formularios POST, Ética de Datos, Pruebas Funcionales y Despliegue

| Destreza / Competencia curricular | Cobertura en el curso | Evidencia en el repo |
|-----------------------------------|-----------------------|----------------------|
| Implementa formularios seguros con validación del lado del servidor | `ContactoForm`, `is_valid()`, CSRF token, POST-Redirect-GET | `semana_5/demo/finalizado/hub/forms.py` y `views.py` |
| Gestiona variables de entorno para separar configuración de código | `.env.ejemplo`, `python-dotenv`, `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` | `semana_5/demo/finalizado/.env.ejemplo` |
| Despliega una aplicación Django en servidor de producción | `collectstatic`, WSGI, PythonAnywhere step-by-step | `README.md` raíz (Guía de Despliegue) |
| **Elabora casos de prueba funcionales** *(eje transversal)* | Tabla 3 casos (vacío, correo inválido, datos válidos) + simulación de carga | `semana_5/pruebas/casos_de_prueba.md` |
| **Conoce y aplica la LOPDP** (protección de datos personales, Ecuador) *(eje transversal)* | Principios LOPDP aplicados al formulario + aviso de privacidad en contacto.html | `semana_5/etica_datos.md` |
| **Produce documentación técnica y de usuario** *(eje transversal)* | Manual de instalación, estructura, mantenimiento y guía de 4 secciones del Hub | `MANUAL.md` (raíz) |
| **Gestiona el proyecto con tablero Kanban y publica release** *(eje transversal)* | Pasos para GitHub Projects / Trello + release v1.0 con etiqueta git | `TABLERO.md` (raíz) |

---

## 3. Matriz de cobertura por eje curricular

La siguiente matriz muestra de un vistazo qué semanas cubren cada eje del currículo.
`●` = cubierto con evidencia explícita / `○` = cubierto de forma implícita o parcial.

| Eje curricular | S1 | S2 | S3 | S4 | S5 |
|----------------|----|----|----|----|-----|
| **Fundamentos de programación** (POO, Python) | ● | ● | ○ | ○ | ○ |
| **Desarrollo web front-end** (HTML, CSS, Bootstrap) | ● | ○ | ● | ○ | ○ |
| **Frameworks web back-end** (Django MTV, URLs, vistas) | ○ | ● | ● | ● | ● |
| **Bases de datos relacionales** (ORM, migraciones, CRUD) | — | — | — | ● | ● |
| **Análisis y diseño de software** (requisitos, wireframe, E/R, historias) | — | — | ● | ● | — |
| **Pruebas de software** (unitarias TestCase, funcionales, carga) | — | — | — | ● | ● |
| **Control de versiones** (Git, convención de commits, ramas) | — | — | — | ● | ● |
| **Seguridad informática** (CSRF, SECRET_KEY, HTTPS, .env) | — | — | — | — | ● |
| **Ética y protección de datos** (LOPDP, aviso de privacidad) | — | — | — | — | ● |
| **Despliegue y producción** (servidor web, WSGI, dominio) | — | — | — | — | ● |
| **Documentación técnica** (manual, tablero kanban, release) | — | — | — | — | ● |
| **Accesibilidad web** (WCAG, contraste, alt, teclado) | — | — | ● | — | — |

---

## 4. Ejes transversales añadidos en la rama `alineacion-curricular`

Estos elementos **no existían en el curso original** y fueron añadidos para completar
la alineación con el currículo. Ninguno modifica la lógica de la aplicación; todos
son archivos nuevos o adiciones a README.

| Archivo nuevo / modificado | Eje transversal cubierto | Semana |
|----------------------------|--------------------------|--------|
| `semana_3/diseno/requisitos.md` | Análisis de requerimientos | 3 |
| `semana_3/diseno/wireframe_recursos.md` | Diseño UI / UX antes de codificar | 3 |
| `semana_3/diseno/rubrica_usabilidad.md` | Autoevaluación y accesibilidad web | 3 |
| `semana_4/diseno/modelo_datos.md` | Diseño de datos (E/R) | 4 |
| `semana_4/diseno/historias_usuario.md` | Ingeniería de requisitos centrada en el usuario | 4 |
| `semana_4/demo/finalizado/hub/tests.py` | Pruebas unitarias con TDD básico | 4 |
| `semana_4/tarea/plantilla_tarea/hub/tests.py` | Extensión guiada de pruebas | 4 |
| `semana_5/pruebas/casos_de_prueba.md` | Pruebas funcionales y de carga | 5 |
| `semana_5/etica_datos.md` | Ética digital y LOPDP Ecuador | 5 |
| `GUIA_GIT.md` (raíz) | Control de versiones profesional | 4-5 |
| `MANUAL.md` (raíz) | Documentación técnica y de usuario | 5 |
| `TABLERO.md` (raíz) | Gestión de proyectos (kanban) y release | 5 |

---

## 5. Correspondencia con competencias profesionales de la figura

El currículo del Bachillerato Técnico "Desarrollo de Software" define las siguientes
**unidades de competencia** para la figura profesional. La siguiente tabla muestra
su cobertura en el curso.

| Unidad de competencia | Descripción resumida | Cobertura en el curso |
|-----------------------|---------------------|----------------------|
| **UC1** — Desarrollar aplicaciones web del lado del servidor | Programar con frameworks web (MVC/MTV), gestionar rutas y vistas, conectar con BD | Semanas 2, 3, 4 y 5 — completa |
| **UC2** — Diseñar y gestionar bases de datos relacionales | Modelar entidades, normalizar, usar ORM, hacer CRUD | Semana 4 — completa; `modelo_datos.md` agrega el diseño previo E/R |
| **UC3** — Desarrollar interfaces web responsivas y accesibles | HTML semántico, CSS, Bootstrap, WCAG | Semanas 1, 2 y 3; `wireframe_recursos.md` y `rubrica_usabilidad.md` formalizan la accesibilidad |
| **UC4** — Aplicar metodologías de desarrollo de software | Análisis de requisitos, historias de usuario, pruebas, documentación, Git | Añadido en `diseno/`, `tests.py`, `GUIA_GIT.md`, `MANUAL.md`, `TABLERO.md` |
| **UC5** — Gestionar la configuración, seguridad y despliegue | Variables de entorno, CSRF, HTTPS, WSGI, PythonAnywhere | Semana 5 — completa |
| **UC6** — Actuar con ética profesional en entornos digitales | Protección de datos personales (LOPDP), aviso de privacidad, buenas prácticas | `semana_5/etica_datos.md` y aviso en `contacto.html` |

---

## 6. Instrucciones de uso para docentes del bachillerato

### Para presentar el curso ante autoridades educativas

1. Comparte este documento junto con el `README.md` raíz del repositorio.
2. Señala la carpeta `semana_X/diseno/` de cada semana como evidencia del
   análisis y diseño previo (UC4).
3. Muestra la ejecución de pruebas con `python manage.py test` como demostración
   de la competencia de testing (UC4).
4. El archivo `GUIA_GIT.md` es la evidencia del trabajo con control de versiones.

### Para adaptar el curso a otros contextos

- **Si tu institución usa Java o PHP:** los principios de análisis (requisitos,
  wireframe, E/R, historias de usuario) son independientes del stack.
- **Si necesitas más horas en pruebas:** amplía los casos de prueba de
  `semana_5/pruebas/casos_de_prueba.md` con pruebas de integración usando el
  cliente de prueba de Django (`self.client.get()`, `self.client.post()`).
- **Para trabajar con GitHub Classroom:** crea una organización, forkea el
  repositorio y asigna las `plantilla_tarea/` como templates de tarea.

### Para integrar evaluación por competencias (rúbrica)

Cada semana cuenta con criterios de aceptación explícitos en la tabla de actividades
del `README.md`. Para evaluación por competencias, se recomienda usar los criterios
de las historias de usuario (`semana_4/diseno/historias_usuario.md`) y la rúbrica de
usabilidad (`semana_3/diseno/rubrica_usabilidad.md`) como instrumentos formales.

---

## 7. Glosario de términos curriculares

| Término | Significado en el contexto del currículo |
|---------|------------------------------------------|
| **Destreza con criterio de desempeño** | Habilidad concreta y medible que el estudiante debe demostrar |
| **Unidad de competencia (UC)** | Agrupación de destrezas que define un rol profesional |
| **Eje transversal** | Tema que atraviesa todas las semanas (ética, ciudadanía digital, etc.) |
| **Figura profesional** | El perfil laboral específico: "Técnico en Desarrollo de Software" |
| **Situación de aprendizaje** | Proyecto práctico que contextualiza las destrezas (≈ el Hub del Docente) |
| **LOPDP** | Ley Orgánica de Protección de Datos Personales — Ecuador, 2021 |
| **WCAG** | Web Content Accessibility Guidelines — estándar W3C de accesibilidad web |

---

*Documento elaborado para el repositorio `curso_django_profesores` — rama `alineacion-curricular`.*  
*Última revisión: junio 2026.*
