# Content verification

Reviewed November 26, 2026.

| Profile content | Evidence and treatment |
| --- | --- |
| Professional identity, roles, dates, and education | The [deployed portfolio](https://vishaka-parab-portfolio.vercel.app/) and its [profile content](https://github.com/vishaka1203/vishaka-parab-portfolio/blob/main/src/content/profile.ts). Employment and education are portfolio-reported. Oracle credentials are attributed to the portfolio. |
| Earlier README and interests | [Existing GitHub profile](https://github.com/vishaka1203). Preserved freelance work, the design and functionality focus, collaboration interests, learning goals, LinkedIn, and Instagram. Earlier badge-only tools are grouped under additional tools. |
| Portfolio links and location | GitHub listed Goa and linked the older Netlify portfolio. The newer portfolio says Mumbai and uses Vercel. The README uses Vercel as the main portfolio, retains Netlify under earlier work, and leaves location to the portfolio profile. |
| Visual identity | [Portfolio source](https://github.com/vishaka1203/vishaka-parab-portfolio) and deployed CSS. Exact tokens and font sources are recorded in the design system. |
| Project selection | Public GitHub metadata, READMEs, public implementation files, and all five published portfolio case studies. Details appear in the [engineering notes](CASE-STUDIES.md). Wushu Goa returned a deployment 404 during verification, so the entry links to source and case study. A live hospital deployment could not be independently verified. Fursaahr’s description establishes scope only. |
| Project screenshots | Captured the deployed portfolio, Curating Frames, and the URL Shortener homepage in isolated headless Chrome on November 26, 2026 at 1200 × 740 CSS pixels. The URL Shortener capture shows its idle interface. |
| Public GitHub metrics | [Counts and limitations](METRICS-METHODOLOGY.md). Two merged PRs were in the profile owner’s hospital repositories. GitHub metadata supplied no licence for those repositories. |
| React contribution | [Issue #38351](https://github.com/react/react/issues/38351), [fork commit](https://github.com/vishaka1203/react/commit/66a4856ee5), and [upstream comment](https://github.com/react/react/pull/38352#issuecomment-7172209660). The upstream PR was opened by another contributor. |
| Contact and privacy | Links to the portfolio contact section and established social channels. Phone numbers and the email address remain on the portfolio. |

Company work is summarised at the publicly described responsibility level. Personal usage, team outcomes, employer architecture, independent certification verification, and project performance beyond the recorded audit are outside the available evidence.

## Preview and link checks

The local preview used GitHub-style Markdown CSS and GitHub Flavored Markdown parsing. Headless Chrome loaded the expected light and dark image assets at desktop width (1120 px) and mobile width (375 px), with no page-level horizontal overflow. The published GitHub profile still serves the original README. GitHub’s actual rendering, image proxy, and Mermaid integration can be checked after the draft is published.

Relative references resolved in the checkout. Of 33 distinct public destinations checked, 32 returned HTTP 200. LinkedIn returned HTTP 999 to the automated request. The retained URL matches both the portfolio and the previous profile README.
