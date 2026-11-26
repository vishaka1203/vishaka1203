"""Refresh public profile metrics using GitHub REST."""
import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
USER = "vishaka1203"


def get(path, **params):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "vishaka1203-profile"}
    if token := os.environ.get("GH_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    query = f"?{urlencode(params)}" if params else ""
    with urlopen(Request(f"https://api.github.com{path}{query}", headers=headers), timeout=20) as response:
        return json.load(response)


def pages(path, **params):
    for page in range(1, 11):
        payload = get(path, per_page=100, page=page, **params)
        items = payload["items"] if isinstance(payload, dict) else payload
        yield from items
        if len(items) < 100:
            return
    raise ValueError("GitHub API returned more than the supported 1,000 results")


def main():
    repos = list(pages(f"/users/{USER}/repos", type="owner"))
    originals = [repo for repo in repos if not repo["fork"] and not repo["archived"]
                 and repo["name"].lower() != USER]
    languages = Counter()
    for repo in originals:
        languages.update(get(f"/repos/{repo['full_name']}/languages"))
    prs = list(pages("/search/issues", q=f"is:pr is:public author:{USER}"))
    created = Counter(repo["created_at"][:4] for repo in originals)
    merged = [pr for pr in prs if pr["pull_request"]["merged_at"]]
    data = {
        "as_of_utc": datetime.now(timezone.utc).date().isoformat(),
        "public_repositories": len(repos),
        "public_forks": sum(repo["fork"] for repo in repos),
        "measured_project_repositories": len(originals),
        "project_repositories_created": dict(sorted(created.items())),
        "language_bytes": dict(languages.most_common()),
        "public_authored_pull_requests": len(prs),
        "merged_in_own_repositories": sum(pr["repository_url"].split("/")[-2].lower() == USER for pr in merged),
        "merged_in_other_repositories": sum(pr["repository_url"].split("/")[-2].lower() != USER for pr in merged),
        "pull_requests": [{"title": pr["title"], "url": pr["html_url"], "merged_at": pr["pull_request"]["merged_at"]} for pr in prs],
    }
    (ROOT / "data/github-metrics.json").write_text(json.dumps(data, indent=2) + "\n")


if __name__ == "__main__":
    main()
