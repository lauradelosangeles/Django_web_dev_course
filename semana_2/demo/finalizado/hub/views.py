from django.http import HttpResponse

# ════════════════════════════════════════════════════════════
#  ZONA DE PERSONALIZACIÓN — edita solo esta sección
# ════════════════════════════════════════════════════════════

# — Información personal —
nombre_docente   = "Prof. González Silva"
iniciales        = "PGS"
materia          = "Matemáticas"
institucion      = "Colegio Dolores Sucre"
anos_experiencia = "5"
num_estudiantes  = "300+"
num_materias     = "3"
correo           = "prof.gonzalez.silva@colegio.edu"
frase_mision     = "Cada estudiante puede dominar las matemáticas con la guía correcta."

# — Textos de las cards (página de inicio) —
icono_materia      = "🖥️"
desc_card_sobre_mi = f"Mi trayectoria, filosofía docente y {anos_experiencia} años formando estudiantes en {materia}."
desc_card_materias = f"Grupos activos este semestre con materiales y actividades actualizados en {institucion}."
desc_card_recursos = "Materiales, ejercicios y sitios de referencia para reforzar el aprendizaje."

# — Etiquetas de estadísticas (se usan en inicio Y en acerca) —
stat_lbl_anos        = "Años de experiencia"
stat_lbl_estudiantes = "Estudiantes formados"
stat_lbl_materias    = "Materias activas"

# ════════════════════════════════════════════════════════════

# ── CDN (fuera del f-string para claridad) ───────────────────
_CDN = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" defer></script>
"""

# ── CSS compartido — fuera del f-string para evitar escapar {{ }} ──
_CSS_SHARED = """<style>
:root {
    --c-dark:    #070d1a;
    --c-navy:    #0f1f3d;
    --c-blue:    #1e3a6e;
    --c-orange:  #ff6b35;
    --c-amber:   #f0b429;
    --c-teal:    #00d4b1;
    --c-bg:      #f5f7fb;
    --c-surface: #ffffff;
    --c-text:    #0f172a;
    --c-muted:   #64748b;
    --c-border:  #e2e8f0;
    --shadow-sm: 0 2px 8px  rgba(15,31,61,0.08);
    --shadow-md: 0 8px 24px rgba(15,31,61,0.14);
    --shadow-lg: 0 20px 56px rgba(15,31,61,0.22);
}
* { box-sizing: border-box; }
body { background: var(--c-bg); font-family: 'Inter', system-ui, sans-serif; color: var(--c-text); margin: 0; }

/* ── NAVBAR ── */
.nb { background: rgba(7,13,26,.93); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); position: sticky; top: 0; z-index: 1000; border-bottom: 1px solid rgba(255,255,255,.07); }
.nb-brand { font-family: 'Playfair Display', serif; font-size: 1.3rem; color: #fff !important; text-decoration: none; letter-spacing: -0.01em; }
.nb-link  { color: rgba(255,255,255,.72) !important; font-weight: 500; font-size: 0.875rem; padding: 0.45rem 0.95rem; border-radius: 6px; transition: background .2s, color .2s; text-decoration: none; }
.nb-link:hover  { background: rgba(255,255,255,.08); color: #fff !important; }
.nb-link.active { color: #fff !important; border-bottom: 2px solid var(--c-orange); padding-bottom: calc(0.45rem - 2px); }

/* ── HERO ── */
.hero { background: linear-gradient(140deg, #070d1a 0%, #0f1f3d 40%, #1e3a6e 80%, #0f1f3d 100%); min-height: 94vh; display: flex; align-items: center; position: relative; overflow: hidden; }
.hero-blob-1 { position: absolute; width: 780px; height: 780px; border-radius: 50%; background: radial-gradient(circle, rgba(0,212,177,.11) 0%, transparent 65%); top: -200px; right: -180px; pointer-events: none; }
.hero-blob-2 { position: absolute; width: 520px; height: 520px; border-radius: 50%; background: radial-gradient(circle, rgba(255,107,53,.09) 0%, transparent 65%); bottom: -100px; left: -100px; pointer-events: none; }
.hero-dots   { position: absolute; inset: 0; background-image: radial-gradient(rgba(255,255,255,.045) 1px, transparent 1px); background-size: 28px 28px; pointer-events: none; }
.hero-tag    { display: inline-block; background: rgba(0,212,177,.12); color: var(--c-teal); border: 1px solid rgba(0,212,177,.25); border-radius: 100px; padding: .35rem 1.1rem; font-size: .72rem; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; margin-bottom: 1.5rem; }
.hero-title  { font-family: 'Playfair Display', serif; font-size: clamp(3.5rem, 9vw, 6.5rem); line-height: 1.04; color: #fff; letter-spacing: -.03em; }
.hero-sub    { color: var(--c-orange); font-weight: 600; font-size: 1.15rem; }
.hero-inst   { color: rgba(255,255,255,.45); font-size: .875rem; margin-top: .25rem; }
.hero-quote  { color: rgba(255,255,255,.62); font-size: 1rem; line-height: 1.85; max-width: 500px; font-style: italic; }

/* Glowing avatar */
.glow-av { width: 72px; height: 72px; border-radius: 50%; background: linear-gradient(135deg, var(--c-orange), var(--c-amber)); display: flex; align-items: center; justify-content: center; font-family: 'Playfair Display', serif; font-size: 1.5rem; color: #fff; font-weight: 700; margin: 0 auto 1.75rem; box-shadow: 0 0 0 3px rgba(0,212,177,.35), 0 0 0 6px rgba(0,212,177,.0), 0 0 28px rgba(255,107,53,.55); }

/* Buttons */
.btn-p { background: var(--c-orange); color: #fff; border: none; padding: .9rem 2.2rem; border-radius: 10px; font-weight: 700; font-size: .95rem; transition: transform .2s, box-shadow .2s; text-decoration: none; display: inline-block; box-shadow: 0 4px 20px rgba(255,107,53,.40); }
.btn-p:hover { transform: translateY(-3px); box-shadow: 0 12px 32px rgba(255,107,53,.55); color: #fff; }
.btn-s { background: transparent; color: rgba(255,255,255,.82); border: 2px solid rgba(255,255,255,.25); padding: .9rem 2.2rem; border-radius: 10px; font-weight: 600; font-size: .95rem; transition: all .2s; text-decoration: none; display: inline-block; }
.btn-s:hover { background: rgba(255,255,255,.07); border-color: rgba(255,255,255,.5); color: #fff; }

@keyframes bounce-y { 0%,100% { transform: translateX(-50%) translateY(0); } 50% { transform: translateX(-50%) translateY(9px); } }
.scroll-dot { position: absolute; bottom: 2rem; left: 50%; animation: bounce-y 2.2s ease-in-out infinite; color: rgba(255,255,255,.3); font-size: 1.6rem; line-height: 1; }

/* ── STATS BAR ── */
.stats-bar { background: var(--c-surface); border-top: 3px solid; border-image: linear-gradient(90deg, var(--c-orange), var(--c-amber), var(--c-teal)) 1; border-bottom: 1px solid var(--c-border); }
.stat-num { font-family: 'Playfair Display', serif; font-size: 3rem; font-weight: 700; line-height: 1; display: block; background: linear-gradient(135deg, var(--c-orange), var(--c-amber)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.stat-lbl { font-size: .7rem; font-weight: 700; text-transform: uppercase; letter-spacing: .12em; color: var(--c-muted); display: block; margin-top: 5px; }

/* ── SECTION ── */
.section-tag   { display: inline-block; background: rgba(255,107,53,.1); color: var(--c-orange); border: 1px solid rgba(255,107,53,.2); border-radius: 100px; padding: .3rem 1rem; font-size: .7rem; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; margin-bottom: .75rem; }
.section-title { font-family: 'Playfair Display', serif; font-size: 2.4rem; color: var(--c-navy); line-height: 1.18; letter-spacing: -.025em; }

/* ── CARDS ── */
.card-f { border: 1px solid var(--c-border); border-radius: 18px; padding: 2.25rem 2rem; background: var(--c-surface); transition: transform .28s ease, box-shadow .28s ease; text-decoration: none; display: block; color: var(--c-text); height: 100%; position: relative; overflow: hidden; }
.card-f::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--c-orange), var(--c-teal)); transform: scaleX(0); transform-origin: left; transition: transform .32s ease; border-radius: 18px 18px 0 0; }
.card-f:hover { transform: translateY(-8px); box-shadow: var(--shadow-lg); color: var(--c-text); }
.card-f:hover::before { transform: scaleX(1); }
.card-f.dark { background: linear-gradient(145deg, var(--c-navy), var(--c-blue)); border-color: rgba(255,255,255,.07); color: #fff; }
.card-f.dark:hover { color: #fff; }
.card-icon-box { width: 52px; height: 52px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 1.6rem; margin-bottom: 1.4rem; }
.card-icon-box.light { background: rgba(255,107,53,.1); }
.card-icon-box.dark-icon { background: rgba(0,212,177,.12); }
.card-ttl { font-family: 'Playfair Display', serif; font-size: 1.28rem; font-weight: 700; margin-bottom: .5rem; }
.card-txt { font-size: .875rem; line-height: 1.7; }
.card-arrow { font-size: .82rem; font-weight: 700; margin-top: 1.25rem; display: inline-block; color: var(--c-teal); letter-spacing: .02em; }

/* ── QUOTE SECTION ── */
.qs { background: linear-gradient(140deg, #070d1a 0%, #0f1f3d 45%, #1e3a6e 100%); }
.qs-mark { font-family: 'Playfair Display', serif; font-size: 12rem; color: var(--c-teal); line-height: .65; display: block; opacity: .15; }
.qs-text { font-family: 'Playfair Display', serif; font-size: 1.65rem; font-style: italic; color: rgba(255,255,255,.92); line-height: 1.65; }
.qs-by   { color: var(--c-orange); font-weight: 700; font-size: .9rem; letter-spacing: .04em; }

/* ── PAGE HEADER ── */
.ph { background: linear-gradient(140deg, #070d1a 0%, #0f1f3d 45%, #1e3a6e 100%); padding: 5rem 0 4rem; position: relative; overflow: hidden; }
.ph::before { content: ''; position: absolute; inset: 0; background-image: radial-gradient(rgba(255,255,255,.04) 1px, transparent 1px); background-size: 28px 28px; pointer-events: none; }
.ph-glow { position: absolute; width: 600px; height: 600px; border-radius: 50%; background: radial-gradient(circle, rgba(255,107,53,.08) 0%, transparent 65%); top: -200px; right: -100px; pointer-events: none; }

/* ── GLOWING AVATAR (large) ── */
.av-lg { width: 110px; height: 110px; border-radius: 50%; background: linear-gradient(135deg, var(--c-orange), var(--c-amber)); display: flex; align-items: center; justify-content: center; font-family: 'Playfair Display', serif; font-size: 2.5rem; color: #fff; font-weight: 700; margin: 0 auto; box-shadow: 0 0 0 4px rgba(0,212,177,.3), 0 0 0 8px rgba(0,212,177,.0), 0 0 40px rgba(255,107,53,.5); }

/* Pills */
.pill { background: rgba(15,31,61,.07); color: var(--c-navy); border-radius: 100px; padding: .35rem 1rem; font-size: .78rem; font-weight: 600; display: inline-block; margin: 3px; border: 1px solid rgba(15,31,61,.1); }

/* Blockquote */
.bq { border-left: 4px solid var(--c-teal); background: linear-gradient(135deg, #f0f5ff, #ecfdf8); border-radius: 0 12px 12px 0; padding: 1.4rem 1.6rem; font-style: italic; font-size: 1.05rem; line-height: 1.78; color: var(--c-navy); }

/* Info rows */
.ir { background: var(--c-surface); border-radius: 10px; padding: 1rem 1.25rem; border-left: 3px solid var(--c-orange); margin-bottom: .75rem; box-shadow: var(--shadow-sm); }
.ir-lbl { font-size: .67rem; font-weight: 700; text-transform: uppercase; letter-spacing: .12em; color: var(--c-muted); display: block; margin-bottom: 3px; }
.ir-val { font-weight: 600; font-size: .97rem; color: var(--c-text); }

/* Mini stat cards */
.sm-card { background: var(--c-surface); border-radius: 14px; padding: 1.5rem 1rem; text-align: center; border: 1px solid var(--c-border); box-shadow: var(--shadow-sm); }
.sm-num { font-family: 'Playfair Display', serif; font-size: 2.2rem; font-weight: 700; display: block; line-height: 1; background: linear-gradient(135deg, var(--c-orange), var(--c-amber)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.sm-lbl { font-size: .7rem; color: var(--c-muted); font-weight: 700; text-transform: uppercase; letter-spacing: .08em; display: block; margin-top: 6px; }

/* Outline button */
.btn-outline-nv { border: 2px solid var(--c-navy); color: var(--c-navy); background: transparent; padding: .7rem 1.75rem; border-radius: 10px; font-weight: 700; font-size: .9rem; transition: all .2s; text-decoration: none; display: inline-block; }
.btn-outline-nv:hover { background: var(--c-navy); color: #fff; }

/* ── FOOTER ── */
.ft { background: #070d1a; color: rgba(255,255,255,.42); font-size: .85rem; }
.ft-brand { font-family: 'Playfair Display', serif; color: #fff; font-size: 1.2rem; display: block; margin-bottom: .2rem; }
.ft-sub   { font-size: .8rem; color: rgba(255,255,255,.38); }
.ft-link  { color: rgba(255,255,255,.42); text-decoration: none; transition: color .2s; }
.ft-link:hover { color: var(--c-teal); }
.ft-divider { border-color: rgba(255,255,255,.07); margin: 1.5rem 0; }
</style>"""


def _nav(active="inicio"):
    ini_cls = "nb-link" + (" active" if active == "inicio" else "")
    aca_cls = "nb-link" + (" active" if active == "acerca" else "")
    return f"""
<nav class="nb py-2">
  <div class="container d-flex align-items-center justify-content-between">
    <a href="/" class="nb-brand">{nombre_docente}</a>
    <div class="d-flex gap-1">
      <a href="/"        class="{ini_cls}">Inicio</a>
      <a href="/acerca/" class="{aca_cls}">Acerca</a>
    </div>
  </div>
</nav>"""


def _footer():
    return f"""
<footer class="ft py-5">
  <div class="container">
    <div class="row align-items-start mb-4">
      <div class="col-md-5 mb-4 mb-md-0">
        <span class="ft-brand">{nombre_docente}</span>
        <span class="ft-sub">Docente de {materia} &middot; {institucion}</span>
      </div>
      <div class="col-md-4 mb-3 mb-md-0">
        <p class="mb-1" style="color:rgba(255,255,255,.28);font-size:.7rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;">Navegación</p>
        <a href="/"        class="ft-link d-block mb-1">Inicio</a>
        <a href="/acerca/" class="ft-link d-block">Acerca</a>
      </div>
      <div class="col-md-3">
        <p class="mb-1" style="color:rgba(255,255,255,.28);font-size:.7rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;">Contacto</p>
        <a href="mailto:{correo}" class="ft-link" style="font-size:.82rem;">{correo}</a>
      </div>
    </div>
    <hr class="ft-divider">
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-center gap-2">
      <small>Construido con <strong style="color:rgba(255,255,255,.65);">Python</strong> y <strong style="color:rgba(255,255,255,.65);">Django</strong></small>
      <small style="color:var(--c-teal);opacity:.7;">Hub Personal del Docente</small>
    </div>
  </div>
</footer>"""


def inicio(request):
    return HttpResponse(f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{nombre_docente} &mdash; Hub Docente</title>
  {_CDN}
  {_CSS_SHARED}
</head>
<body>

{_nav("inicio")}

<!-- ══════════════════════════════════════════════════════ HERO -->
<section class="hero">
  <div class="hero-blob-1"></div>
  <div class="hero-blob-2"></div>
  <div class="hero-dots"></div>

  <div class="container position-relative text-center py-5" style="z-index:1;">

    <div class="glow-av">{iniciales}</div>

    <div class="hero-tag">Docente &middot; Hub Personal</div>

    <h1 class="hero-title mb-3">{nombre_docente}</h1>

    <p class="hero-sub mb-1">{icono_materia} Docente de {materia}</p>
    <p class="hero-inst mb-4">{institucion}</p>

    <p class="hero-quote mx-auto mb-5">
      &ldquo;{frase_mision}&rdquo;
    </p>

    <div class="d-flex gap-3 justify-content-center flex-wrap">
      <a href="/acerca/" class="btn-s">Acerca de m&iacute; &rarr;</a>
    </div>
  </div>

  <span class="scroll-dot">&#8964;</span>
</section>

<!-- ══════════════════════════════════════════════════════ STATS -->
<section class="stats-bar py-5">
  <div class="container">
    <div class="row g-0 text-center">
      <div class="col-4" style="border-right: 1px solid var(--c-border);">
        <span class="stat-num">{anos_experiencia}</span>
        <span class="stat-lbl">{stat_lbl_anos}</span>
      </div>
      <div class="col-4" style="border-right: 1px solid var(--c-border);">
        <span class="stat-num">{num_estudiantes}</span>
        <span class="stat-lbl">{stat_lbl_estudiantes}</span>
      </div>
      <div class="col-4">
        <span class="stat-num">{num_materias}</span>
        <span class="stat-lbl">{stat_lbl_materias}</span>
      </div>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════════════════════════ CARDS -->
<section style="background: var(--c-bg); padding: 5.5rem 0;">
  <div class="container">

    <div class="text-center mb-5">
      <span class="section-tag">Mi espacio digital</span>
      <h2 class="section-title mt-1">Todo lo que necesitan<br>mis estudiantes</h2>
    </div>

    <div class="row g-4">
      <div class="col-md-4">
        <a href="/acerca/" class="card-f">
          <div class="card-icon-box light">👨‍🏫</div>
          <p class="card-ttl" style="color: var(--c-navy);">Sobre m&iacute;</p>
          <p class="card-txt" style="color: var(--c-muted);">{desc_card_sobre_mi}</p>
          <span class="card-arrow">Ver perfil &rarr;</span>
        </a>
      </div>

      <div class="col-md-4">
        <div class="card-f dark">
          <div class="card-icon-box dark-icon">{icono_materia}</div>
          <p class="card-ttl">{materia}</p>
          <p class="card-txt" style="color: rgba(255,255,255,.68);">{desc_card_materias}</p>
          <span class="card-arrow">Mis materias &rarr;</span>
        </div>
      </div>

      <div class="col-md-4">
        <div class="card-f">
          <div class="card-icon-box light">🔗</div>
          <p class="card-ttl" style="color: var(--c-navy);">Recursos</p>
          <p class="card-txt" style="color: var(--c-muted);">{desc_card_recursos}</p>
          <span class="card-arrow">Disponible en Semana 3 &rarr;</span>
        </div>
      </div>
    </div>

  </div>
</section>

<!-- ══════════════════════════════════════════════════════ QUOTE -->
<section class="qs" style="padding: 5.5rem 0;">
  <div class="container text-center" style="max-width: 740px;">
    <span class="qs-mark">&ldquo;</span>
    <p class="qs-text mt-n3 mb-4">{frase_mision}</p>
    <span class="qs-by">&mdash; {nombre_docente} &middot; {materia}</span>
  </div>
</section>

{_footer()}
</body>
</html>""")


def acerca(request):
    return HttpResponse(f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Acerca &mdash; {nombre_docente}</title>
  {_CDN}
  {_CSS_SHARED}
</head>
<body>

{_nav("acerca")}

<!-- ══════════════════════════════════════════════════════ PAGE HEADER -->
<header class="ph">
  <div class="ph-glow"></div>
  <div class="container text-center text-white position-relative" style="z-index:1;">
    <div class="hero-tag mb-3">Perfil del Docente</div>
    <h1 style="font-family:'Playfair Display',serif; font-size: clamp(2.2rem,5vw,3.4rem); font-weight:700; letter-spacing:-.025em; color:#fff; margin-bottom:.6rem;">
      {nombre_docente}
    </h1>
    <p style="color: var(--c-orange); font-weight:600; margin:0;">
      Docente de {materia} &middot; {institucion}
    </p>
  </div>
</header>

<!-- ══════════════════════════════════════════════════════ MAIN CONTENT -->
<div class="container py-5" style="max-width: 860px;">
  <div class="row g-5 align-items-start">

    <!-- COLUMNA IZQUIERDA -->
    <div class="col-md-4 text-center">

      <div class="av-lg mb-4">{iniciales}</div>

      <h5 style="font-family:'Playfair Display',serif; color:var(--c-navy); margin-bottom:4px; font-size:1.2rem;">
        {nombre_docente}
      </h5>
      <p style="color:var(--c-muted); font-size:.875rem; margin-bottom:1.4rem;">
        Docente de {materia}
      </p>

      <div class="mb-3">
        <span class="pill">{institucion}</span>
        <span class="pill">{materia}</span>
        <span class="pill">{anos_experiencia} a&ntilde;os exp.</span>
      </div>

      <a href="mailto:{correo}"
         style="font-size:.82rem; color:var(--c-teal); font-weight:600; text-decoration:none;">
        &#9993; {correo}
      </a>

    </div>

    <!-- COLUMNA DERECHA -->
    <div class="col-md-8">

      <h2 style="font-family:'Playfair Display',serif; color:var(--c-navy); font-size:2.1rem; letter-spacing:-.025em; margin-bottom:1.5rem;">
        Acerca del Docente
      </h2>

      <blockquote class="bq mb-4">
        &ldquo;{frase_mision}&rdquo;
      </blockquote>

      <div class="ir">
        <span class="ir-lbl">Nombre completo</span>
        <span class="ir-val">{nombre_docente}</span>
      </div>
      <div class="ir">
        <span class="ir-lbl">Instituci&oacute;n</span>
        <span class="ir-val">{institucion}</span>
      </div>
      <div class="ir">
        <span class="ir-lbl">&Aacute;rea de ense&ntilde;anza</span>
        <span class="ir-val">{materia}</span>
      </div>
      <div class="ir">
        <span class="ir-lbl">Trayectoria</span>
        <span class="ir-val">{anos_experiencia} a&ntilde;os formando estudiantes</span>
      </div>
      <div class="ir">
        <span class="ir-lbl">Contacto</span>
        <span class="ir-val">{correo}</span>
      </div>

      <a href="/" class="btn-outline-nv mt-4">&larr; Volver al inicio</a>

    </div>
  </div>

  <!-- MINI STATS -->
  <hr style="border-color: var(--c-border); margin: 3.5rem 0;">

  <div class="row g-3 text-center">
    <div class="col-4">
      <div class="sm-card">
        <span class="sm-num">{anos_experiencia}</span>
        <span class="sm-lbl">A&ntilde;os de experiencia</span>
      </div>
    </div>
    <div class="col-4">
      <div class="sm-card">
        <span class="sm-num">{num_estudiantes}</span>
        <span class="sm-lbl">Estudiantes formados</span>
      </div>
    </div>
    <div class="col-4">
      <div class="sm-card">
        <span class="sm-num">{num_materias}</span>
        <span class="sm-lbl">Materias activas</span>
      </div>
    </div>
  </div>

</div>

{_footer()}
</body>
</html>""")
