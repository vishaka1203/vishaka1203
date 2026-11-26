"""Build the profile illustrations from local design tokens and metrics."""
import base64
import json
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "data/design-tokens.json").read_text())
METRICS = json.loads((ROOT / "data/github-metrics.json").read_text())


def font(name):
    data = (ROOT / "assets/fonts" / f"{name}.woff2").read_bytes()
    return base64.b64encode(data).decode("ascii")


def svg(path, title, height, colors, body, styles=""):
    paper = colors["paper"]
    ink = colors["ink"]
    path.write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title">
  <title id="title">{escape(title)}</title>
  <style>text{{font-family:Arial,sans-serif}}{styles}</style>
  <rect width="960" height="{height}" rx="16" fill="{paper}"/>
  <g fill="{ink}">{body}</g>
</svg>
''')


def hero(theme, colors):
    ink, muted, accent, champagne = (colors[k] for k in ("ink", "muted", "accent", "champagne"))
    jade = accent if theme == "light" else colors["soft"]
    line = colors["paper"] if theme == "light" else accent
    styles = (
        f"@font-face{{font-family:Manrope;src:url(data:font/woff2;base64,{font('manrope')}) format('woff2');font-weight:200 800}}"
        f"@font-face{{font-family:Cormorant;src:url(data:font/woff2;base64,{font('cormorant-garamond')}) format('woff2');font-style:italic;font-weight:300 700}}"
        "text{font-family:Manrope,Arial,sans-serif}.editorial{font-family:Cormorant,Georgia,serif;font-style:italic}"
    )
    body = f'''
    <path d="M648 0H944Q960 0 960 16V336Q960 352 944 352H648Z" fill="{jade}"/>
    <g fill="none" stroke="{line}" stroke-width="2">
      <path d="M688 280V152L784 88L880 152V280Z"/>
      <path d="M720 280V168L784 128L848 168V280M752 280V184L784 168L816 184V280"/>
      <path d="M784 88V280M688 216H880"/>
    </g>
    <circle cx="784" cy="216" r="7" fill="{colors['champagne'] if theme == 'dark' else colors['paper']}"/>
    <text x="56" y="80" font-size="36" fill="{accent}" font-weight="800">vp.</text>
    <text x="56" y="128" font-size="21" fill="{muted}" font-weight="700" letter-spacing="2">SOFTWARE DEVELOPER</text>
    <text x="53" y="203" class="editorial" font-size="83" fill="{ink}">Vishaka Parab</text>
    <text x="56" y="253" font-size="25" fill="{champagne}" font-weight="700">Engineering with intent.</text>
    <text x="56" y="301" font-size="21" fill="{muted}">React · Next.js · TypeScript · Data visualisation</text>
  '''
    svg(ROOT / f"assets/banners/hero-{theme}.svg", "Vishaka Parab, software developer", 352, colors, body, styles)


def chart(theme, colors):
    labels = [("Public repos", "public_repositories"), ("Merged on own repos", "merged_in_own_repositories"),
              ("Merged on other repos", "merged_in_other_repositories")]
    values = [METRICS[key] for _, key in labels]
    date = escape(METRICS["as_of_utc"])
    rows = [f'<text x="40" y="54" font-size="30" font-weight="700">Public GitHub activity</text>',
            f'<text x="40" y="91" font-size="22" fill="{colors["muted"]}">Snapshot · {date} UTC</text>']
    for i, ((label, _), value) in enumerate(zip(labels, values)):
        x = 40 + 306 * i
        rows.append(f'<rect x="{x}" y="120" width="268" height="112" rx="12" fill="{colors["surface"]}"/>')
        rows.append(f'<text x="{x+20}" y="171" font-size="41" font-weight="700" fill="{colors["accent"]}">{value}</text>')
        rows.append(f'<text x="{x+20}" y="207" font-size="20">{label}</text>')
    rows.append('<text x="40" y="294" font-size="27" font-weight="700">Repository language bytes</text>')
    counts = list(METRICS["language_bytes"].items())
    total = sum(count for _, count in counts)
    groups = counts[:4]
    if remainder := sum(count for _, count in counts[4:]):
        groups.append(("Other", remainder))
    for i, (label, count) in enumerate(groups):
        y = 342 + i * 48
        percent = 100 * count / total
        rows.append(f'<text x="40" y="{y+16}" font-size="23">{escape(label)}</text>')
        rows.append(f'<rect x="226" y="{y}" width="568" height="20" rx="4" fill="{colors["soft"]}"/>')
        if width := round(568 * count / total, 2):
            rows.append(f'<rect x="226" y="{y}" width="{width}" height="20" rx="4" fill="{colors["accent"]}"/>')
        rows.append(f'<text x="915" y="{y+16}" text-anchor="end" font-size="23" fill="{colors["champagne"]}">{percent:.1f}%</text>')
    year_heading = 370 + len(groups) * 48
    rows.append(f'<text x="40" y="{year_heading}" font-size="27" font-weight="700">Project repositories created</text>')
    years = METRICS["project_repositories_created"]
    maximum = max(years.values(), default=1)
    for i, (year, count) in enumerate(years.items()):
        y = year_heading + 32 + i * 48
        rows.append(f'<text x="40" y="{y+16}" font-size="23">{escape(year)}</text>')
        rows.append(f'<rect x="226" y="{y}" width="{568*count/maximum:.2f}" height="20" rx="4" fill="{colors["accent"]}"/>')
        rows.append(f'<text x="915" y="{y+16}" text-anchor="end" font-size="23" fill="{colors["champagne"]}">{count}</text>')
    height = year_heading + 56 + len(years) * 48
    svg(ROOT / f"assets/charts/github-{theme}.svg", "Public GitHub counts, language bytes, and projects created by year", height, colors, "\n    ".join(rows))


def tools_map(theme, colors):
    groups = (
        ("Interfaces", "React · Next.js · TypeScript"),
        ("UI systems", "Ant Design · Tailwind CSS · Material UI"),
        ("Data", "REST · MySQL · ApexCharts · ECharts"),
        ("Delivery", "Git · Docker · CI/CD · Jest"),
    )
    rows = ['<text x="40" y="54" font-size="32" font-weight="700">Frontend engineering toolkit</text>']
    for i, (label, detail) in enumerate(groups):
        x, y = 40 + (i % 2) * 456, 88 + (i // 2) * 96
        rows.append(f'<rect x="{x}" y="{y}" width="424" height="80" rx="12" fill="{colors["surface"]}"/>')
        rows.append(f'<text x="{x+16}" y="{y+30}" font-size="23" font-weight="700" fill="{colors["accent"]}">{label}</text>')
        rows.append(f'<text x="{x+16}" y="{y+58}" font-size="19">{escape(detail)}</text>')
    svg(ROOT / f"assets/charts/toolkit-{theme}.svg", "Frontend engineering toolkit", 296, colors, "\n    ".join(rows))


def performance_chart(theme, colors):
    data = json.loads((ROOT / "data/performance.json").read_text())
    rows = ['<text x="40" y="54" font-size="31" font-weight="700">Portfolio · mobile lab audit</text>']
    for i, (label, score) in enumerate(data["scores"].items()):
        y = 96 + i * 48
        rows.append(f'<text x="40" y="{y+19}" font-size="23">{escape(label)}</text>')
        rows.append(f'<rect x="228" y="{y}" width="568" height="22" rx="4" fill="{colors["soft"]}"/>')
        rows.append(f'<rect x="228" y="{y}" width="{568*score/100:.2f}" height="22" rx="4" fill="{colors["accent"]}"/>')
        rows.append(f'<text x="914" y="{y+19}" text-anchor="end" font-size="23" fill="{colors["champagne"]}">{score}/100</text>')
    svg(ROOT / f"assets/charts/performance-{theme}.svg", "Lighthouse mobile category scores", 296, colors, "\n    ".join(rows))


def architecture(theme, colors):
    accent = colors["accent"]
    panel = colors["surface"]
    body = f'''
    <text x="40" y="54" font-size="31" font-weight="700">URL Shortener · request flow</text>
    <g fill="{panel}" stroke="{accent}" stroke-width="2">
      <rect x="40" y="88" width="240" height="56" rx="8"/><rect x="352" y="88" width="240" height="56" rx="8"/>
      <rect x="40" y="184" width="240" height="56" rx="8"/><rect x="352" y="184" width="240" height="56" rx="8"/>
      <rect x="672" y="88" width="248" height="56" rx="8"/><rect x="672" y="184" width="248" height="56" rx="8"/>
    </g>
    <g fill="none" stroke="{accent}" stroke-width="3">
      <path d="M296 116H336m-7-6 7 6-7 6M608 116H656m-7-6 7 6-7 6M296 212H336m-7-6 7 6-7 6M608 212H656m-7-6 7 6-7 6"/>
      <path d="M472 184V164H796V144m-6 7 6-7 6 7"/>
    </g>
    <g font-size="22" text-anchor="middle">
      <text x="160" y="124">Submit long URL</text><text x="472" y="124">POST /api/shorten</text><text x="796" y="124">MySQL urls</text>
      <text x="160" y="220">Follow short link</text><text x="472" y="220">Dynamic route</text><text x="796" y="220">Original destination</text>
    </g>
    '''
    svg(ROOT / f"assets/architecture/url-shortener-{theme}.svg", "URL Shortener creation and redirect paths", 280, colors, body)


for theme in ("light", "dark"):
    colors = TOKENS[theme]
    hero(theme, colors)
    chart(theme, colors)
    tools_map(theme, colors)
    performance_chart(theme, colors)
    architecture(theme, colors)
