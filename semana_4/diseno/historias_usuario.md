# Historias de Usuario — Semana 4

> Una **historia de usuario** describe una funcionalidad desde el punto de vista de
> quien la usa, no desde el punto de vista técnico.
> Formato estándar: **"Como [rol] quiero [acción] para [beneficio]."**

---

## ¿Por qué escribir historias de usuario?

- Centran el diseño en la persona, no en la tecnología.
- Son fáciles de convertir en criterios de aceptación y pruebas.
- Forman parte del currículo de Bachillerato Técnico "Desarrollo de Software"
  (análisis de requerimientos con perspectiva del usuario).

---

## Historias del Hub Personal del Docente

### Historia 1 — Ver recursos

> **Como docente**, quiero **ver una lista de mis recursos educativos** en `/recursos/`
> **para** que mis estudiantes accedan fácilmente a los materiales de la materia.

**Criterios de aceptación:**
- [ ] La página muestra título, descripción y enlace de cada recurso.
- [ ] Los recursos aparecen ordenados del más reciente al más antiguo.
- [ ] Si no hay recursos, se muestra un mensaje "Aún no hay recursos disponibles."

---

### Historia 2 — Guardar recursos

> **Como docente**, quiero **agregar y editar mis recursos desde el Panel de
> Administración** (`/admin/`) **para** mantener el catálogo actualizado sin escribir
> código ni retocar la base de datos manualmente.

**Criterios de aceptación:**
- [ ] El modelo `Recurso` aparece en `/admin/` con campos editables.
- [ ] Al guardar un recurso nuevo, aparece en `/recursos/` sin reiniciar el servidor.
- [ ] El campo `url` valida que el texto ingresado sea una dirección web válida.

---

### Historia 3 — Recibir mensajes

> **Como docente**, quiero **recibir mensajes de contacto de mis estudiantes o
> colegas** a través del formulario en `/contacto/` **para** poder responderles por
> correo sin publicar mi dirección de email en la página principal.

**Criterios de aceptación:**
- [ ] El formulario guarda el mensaje en la tabla `Mensaje` de la base de datos.
- [ ] El modelo `Mensaje` aparece en `/admin/` con indicador de leído/no leído.
- [ ] Un mensaje con correo inválido no se guarda y muestra error al usuario.

---

## Cómo usar este documento en clase

1. Relaciona cada historia con los archivos de código que la implementan
   (`models.py`, `views.py`, `admin.py`).
2. Convierte los criterios de aceptación en casos de prueba (ver semana 5).
3. Al finalizar el curso, verifica que todas las historias estén completadas.
