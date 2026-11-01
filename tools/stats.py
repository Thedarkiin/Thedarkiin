"""Generate overview.svg from live GitHub data.

Usage: GITHUB_TOKEN=... USERNAME=... python tools/stats.py <output_dir>
The image has a transparent background and reads on light and dark themes.
A failed API call stops the run: the previous image stays in place rather than
being replaced by empty numbers.
"""
import json
import os
import sys
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

TEXT, ACCENT, GRID = "#7d8590", "#14a098", "#7d859055"
FONT = 'ui-monospace, SFMono-Regular, Menlo, Consolas, "DejaVu Sans Mono", monospace'

QUERY = """
query($login: String!, $after: String) {
  user(login: $login) {
    followers { totalCount }
    repositories(ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC, first: 100, after: $after) {
      totalCount
      pageInfo { hasNextPage endCursor }
      nodes { stargazerCount forkCount }
    }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      contributionCalendar { totalContributions }
    }
  }
}
"""


def graphql(token, login, after=None):
    body = json.dumps({"query": QUERY, "variables": {"login": login, "after": after}}).encode()
    request = urllib.request.Request("https://api.github.com/graphql", data=body, headers={
        "Authorization": f"bearer {token}", "Content-Type": "application/json", "User-Agent": "profile-stats"})
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    if payload.get("errors"):
        raise RuntimeError(f"GitHub API error: {payload['errors']}")
    return payload["data"]["user"]


def fetch(token, login):
    user = graphql(token, login)
    repos = list(user["repositories"]["nodes"])
    page = user["repositories"]["pageInfo"]
    while page["hasNextPage"]:
        more = graphql(token, login, page["endCursor"])["repositories"]
        repos += more["nodes"]
        page = more["pageInfo"]
    collection = user["contributionsCollection"]
    return {
        "stars": sum(r["stargazerCount"] for r in repos),
        "forks": sum(r["forkCount"] for r in repos),
        "repos": user["repositories"]["totalCount"],
        "followers": user["followers"]["totalCount"],
        "contributions": collection["contributionCalendar"]["totalContributions"],
        "commits": collection["totalCommitContributions"],
        "prs": collection["totalPullRequestContributions"],
    }


def overview(data):
    rows = [
        ("Stars", data["stars"]), ("Public repositories", data["repos"]),
        ("Contributions, last year", data["contributions"]),
        ("Commits, last year", data["commits"]),
    ]
    width, height = 340, 40 + 26 * len(rows)
    body = []
    for i, (label, value) in enumerate(rows):
        y = 44 + 26 * i
        body.append(
            f'<text class="r" style="animation-delay:{i * 0.12:.2f}s" x="14" y="{y}" fill="{TEXT}">{escape(label)}</text>'
            f'<text class="r" style="animation-delay:{i * 0.12:.2f}s" x="{width - 14}" y="{y}" text-anchor="end" font-weight="700" fill="{ACCENT}">{value:,}</text>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="GitHub statistics">
<style>
text {{ font-family: {FONT}; font-size: 13px; }}
.r {{ opacity: 0; animation: show .4s ease-out forwards; }}
@keyframes show {{ to {{ opacity: 1; }} }}
@media (prefers-reduced-motion: reduce) {{ .r {{ animation: none; opacity: 1; }} }}
</style>
<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="8" fill="none" stroke="{GRID}"/>
<text x="14" y="22" font-weight="700" fill="{ACCENT}">GitHub statistics</text>
{"".join(body)}
</svg>
'''


def main():
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    data = fetch(os.environ["GITHUB_TOKEN"], os.environ["USERNAME"])
    (out / "overview.svg").write_text(overview(data), encoding="utf-8")
    print(data)


if __name__ == "__main__":
    main()
