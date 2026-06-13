# Ética y Protección de Datos Personales — Semana 5

> El formulario de contacto recopila datos personales (nombre y correo electrónico).
> Como desarrolladores y docentes, tenemos la obligación legal y ética de proteger
> esa información.

---

## La Ley Orgánica de Protección de Datos Personales (LOPDP) — Ecuador

La **LOPDP** (publicada en el Registro Oficial Suplemento N.° 459 del 26 de mayo de 2021)
es la principal norma de protección de datos personales en Ecuador. Aplica a cualquier
persona natural o jurídica que trate datos de ciudadanos ecuatorianos, incluyendo
aplicaciones web escolares o proyectos académicos.

### Principios clave aplicados al formulario de contacto

| Principio LOPDP | Cómo aplica al Hub del Docente |
|-----------------|-------------------------------|
| **Licitud** | Solo recopilamos nombre y correo porque el usuario los envía voluntariamente. | 
| **Finalidad** | Los datos se usan únicamente para que el docente pueda responder el mensaje. No se usan para publicidad ni se comparten con terceros. |
| **Minimización** | El formulario pide solo los datos necesarios (nombre, correo, mensaje). No pide fecha de nacimiento, dirección ni datos sensibles. |
| **Limitación de conservación** | En un proyecto real, se deben eliminar los mensajes después de un tiempo razonable (p. ej., 1 año). En este curso educativo, la BD es local y temporal. |
| **Seguridad** | Django usa `SECRET_KEY`, CSRF y contraseñas hasheadas. En producción, el sitio debe usar HTTPS. |
| **Transparencia** | El usuario debe saber para qué se usan sus datos. Por eso añadimos el aviso de privacidad al formulario. |

### ¿Qué pasa si no cumplimos?

La LOPDP establece sanciones económicas y puede llegar a ordenar la suspensión del
tratamiento de datos. Para proyectos educativos es importante desarrollar el hábito
de cumplimiento desde el aula.

---

## Aviso de Privacidad para el Formulario de Contacto

El siguiente texto está listo para copiar debajo del formulario en `contacto.html`.
Es breve (2-3 frases) y cumple el principio de transparencia de la LOPDP.

---

**Texto del aviso de privacidad:**

> Los datos que ingresas en este formulario (nombre y correo electrónico) son
> recopilados únicamente para que el docente pueda responder tu mensaje.
> No se comparten con terceros ni se usan con fines publicitarios,
> en cumplimiento de la Ley Orgánica de Protección de Datos Personales del Ecuador.

---

## Buenas prácticas adicionales para el Hub en producción

1. **Usa HTTPS** — el correo viaja cifrado entre el navegador y el servidor.
2. **Restringe el acceso al admin** — usa contraseñas fuertes en `createsuperuser`.
3. **No expongas `SECRET_KEY`** — mantenla en `.env`, nunca en el código.
4. **Elimina mensajes viejos** — considera una tarea programada que limpie la BD
   periódicamente.
5. **Informa el derecho de cancelación** — el usuario puede pedir que borres sus datos
   (Art. 8 LOPDP).

---

## Reflexión para el aula

> *"Un software ético no es solo aquel que funciona correctamente, sino aquel que
> respeta la dignidad y privacidad de las personas que lo usan."*

Pregunta para discusión: ¿Qué información NO deberías guardar en la base de datos
aunque el usuario te la diera voluntariamente? ¿Por qué?
