# Requisitos del Sistema — Semana 3

> **¿Para qué sirve este documento?**  
> Antes de escribir código, el equipo (o el docente) lista QUÉ debe hacer el sistema
> (requisitos funcionales) y CÓMO debe comportarse (requisitos no funcionales).
> Esto evita retrabajos y sirve de criterio de aceptación al final.

---

## Tabla de Requisitos

| # | Tipo | Requisito | Criterio de aceptación |
|---|------|-----------|------------------------|
| 1 | **Funcional** | Mostrar una lista de recursos educativos en `/recursos/` | La página muestra al menos un recurso con título, URL y descripción |
| 2 | **Funcional** | Cada recurso presenta un enlace que abre la URL en una pestaña nueva | El atributo `target="_blank"` está presente en todos los enlaces |
| 3 | **No funcional** | La página `/recursos/` carga en menos de 2 segundos en conexión normal | Medible con DevTools (pestaña Network) |
| 4 | **No funcional** | El contraste de texto cumple WCAG AA (relación mínima 4.5:1) | Verificable con extensión de accesibilidad del navegador |
| 5 | **Funcional** | _(Completa aquí tu requisito funcional)_ | _(Define el criterio de aceptación)_ |
| 6 | **No funcional** | _(Completa aquí tu requisito no funcional)_ | _(Define el criterio de aceptación)_ |
| 7 | **Funcional / No funcional** | _(Completa aquí)_ | _(Completa aquí)_ |

---

## Instrucciones para el docente

1. **Funcional** = lo que el sistema *hace* ("mostrar", "guardar", "enviar").
2. **No funcional** = cómo lo hace ("en menos de 2 s", "seguro", "accesible").
3. Llena las filas 5-7 antes de escribir código; compáralas al finalizar para
   confirmar que cada requisito está cumplido.

---

## Recursos de referencia

- [IEEE 830 — Especificación de Requisitos de Software](https://www.iso.org/standard/26985.html) (referencia académica)
- Currículum Bachillerato Técnico "Desarrollo de Software" — Ministerio de Educación Ecuador
