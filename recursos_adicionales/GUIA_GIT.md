# Guía de Control de Versiones con Git

> Git registra el historial de cambios del proyecto, como las versiones numeradas
> de un documento Word, pero de forma automática y sin duplicar archivos.
> Esta guía sigue el flujo recomendado para el curso de 5 semanas.

---

## 1. Convención de commits

Cada mensaje de commit sigue el formato `tipo: descripción breve`.
Esto facilita leer el historial y entender qué cambió en cada paso.

| Tipo | Cuándo usarlo | Ejemplo |
|------|---------------|---------|
| `feat:` | Nueva funcionalidad | `feat: agregar vista contacto con formulario POST` |
| `fix:` | Corrección de error | `fix: corregir URL de recursos en urls.py` |
| `docs:` | Solo documentación | `docs: actualizar README semana 4` |
| `test:` | Añadir o corregir pruebas | `test: agregar test de creación de Recurso` |
| `style:` | Formato, indentación (sin lógica) | `style: indentar views.py` |
| `refactor:` | Reestructura sin cambiar comportamiento | `refactor: mover lógica del ORM a función auxiliar` |

**Regla de oro:** el mensaje debe completar la frase  
*"Si aplico este commit, el proyecto quedará con ___."*

---

## 2. Una rama por semana

Trabaja cada semana en su propia rama para mantener `main` siempre funcional.

```bash
# Crear y cambiar a la rama de la semana
git checkout -b semana-04

# Ver en qué rama estás
git branch

# Cambiar de vuelta a main cuando termines
git checkout main

# Fusionar la semana terminada en main
git merge semana-04
```

| Semana | Nombre de rama sugerido |
|--------|-------------------------|
| 1 | `semana-01` |
| 2 | `semana-02` |
| 3 | `semana-03` |
| 4 | `semana-04` |
| 5 | `semana-05` |

---

## 3. Comandos esenciales del flujo diario

```bash
# 1. Ver qué archivos cambiaron
git status

# 2. Ver los cambios concretos antes de agregar
git diff

# 3. Agregar archivos específicos al área de preparación (staging)
git add hub/views.py hub/models.py

# 4. Agregar todos los cambios rastreados (úsalo con cuidado)
git add .

# 5. Crear el commit con mensaje descriptivo
git commit -m "feat: conectar recursos_view() al ORM con Recurso.objects.all()"

# 6. Subir la rama al repositorio remoto (GitHub)
git push origin semana-04
```

> **Precaución:** nunca hagas `git add .` si tienes archivos `.env` con contraseñas.
> Verifica que `.gitignore` los excluya antes.

---

## 4. Entregar el historial de commits

Al final de cada semana, el docente puede pedir una captura del historial como
evidencia de trabajo incremental.

```bash
# Ver historial resumido (una línea por commit)
git log --oneline

# Ver los últimos 10 commits
git log --oneline -10

# Ver historial con ramas en formato gráfico
git log --oneline --graph --all
```

**Ejemplo de salida esperada:**
```
a3f1c2e test: agregar RecursoModelTest con 2 casos
8b4d9f1 feat: registrar Recurso y Mensaje en admin.py
2c7e5a0 feat: definir modelos Recurso y Mensaje en models.py
0d1b3f9 feat: agregar plantillas herencia base.html semana 3
```

Toma una captura de pantalla de esta salida y adjúntala a tu entrega.

---

## 5. Archivo `.gitignore` recomendado

Asegúrate de que el proyecto tiene un `.gitignore` que excluya:

```
# Variables de entorno (nunca al repositorio)
.env

# Base de datos local
db.sqlite3

# Caché de Python
__pycache__/
*.pyc

# Archivos estáticos generados
staticfiles/
```

---

## Recursos adicionales

- [Pro Git Book (español)](https://git-scm.com/book/es/v2) — referencia completa y gratuita
- [GitHub Docs](https://docs.github.com/es) — guías para repositorios remotos
