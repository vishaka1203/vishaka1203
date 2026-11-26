# Metrics and methodology

## GitHub snapshot

The [snapshot data](../data/github-metrics.json) records the collection date and public counts. The public snapshot includes **12 repositories**, **one fork**, and **two authored PRs merged into repositories owned by Vishaka**. The API returned zero authored PRs merged into another repository. The React PR comment is represented separately in the README.

GitHub’s public [repository inventory](https://docs.github.com/en/rest/repos/repos#list-repositories-for-a-user), [language endpoint](https://docs.github.com/en/rest/repos/repos#list-repository-languages), and [issue and PR search](https://docs.github.com/en/rest/search/search#search-issues-and-pull-requests) are the data sources. Byte totals exclude forks, archived repositories, and the profile README repository. Aggregation is weighted by bytes. Language bytes describe detected repository contents. They can reflect styling, generated files, or vendored code and carry no proficiency rating. Private activity, commit frequency, and all-repository contribution totals are outside the snapshot.

Repository creation counts in the included project set were 6 in 2024, 1 in 2025, and 3 in 2026 at the snapshot date. Commit histories were used for source context rather than as productivity metrics. The professional timeline begins in August 2023 based on the dated career entries.

### Refresh

From the repository root, run:

```sh
python3 scripts/refresh-metrics.py
python3 scripts/generate-assets.py
git diff
```

The refresh works without authentication within GitHub’s unauthenticated limits. An optional `GH_TOKEN` can be supplied through the environment. Once the workflow file is published, **Refresh profile metrics** can be run manually in Actions. It produces downloadable data and updated charts for review. Update the prose snapshot above when accepting a new snapshot.

## Portfolio Lighthouse audit

The [recorded measurements](../data/performance.json) are from one Lighthouse 13.6.0 run on the [deployed portfolio homepage](https://vishaka-parab-portfolio.vercel.app/) on November 26, 2026, at 04:53 UTC. It ran in headless Chrome 158 on macOS with simulated mobile throttling and a 412 × 823 CSS-pixel viewport.

| Metric | Result |
| --- | ---: |
| Performance | 71 / 100 |
| Accessibility | 94 / 100 |
| Best practices | 96 / 100 |
| SEO | 100 / 100 |
| Largest Contentful Paint | 1.3 s |
| Total Blocking Time | 2,090 ms |
| Cumulative Layout Shift | 0 |

These are lab results for one page and one run. Scores can vary with device, browser, network, and page changes. Lighthouse accessibility covers automated checks and does not establish full WCAG conformance. LCP and CLS are lab observations rather than field Core Web Vitals.

To repeat with the same Lighthouse version:

```sh
npx lighthouse@13.6.0 https://vishaka-parab-portfolio.vercel.app/ --chrome-flags=--headless --output=json --output-path=portfolio-lighthouse.json
```
