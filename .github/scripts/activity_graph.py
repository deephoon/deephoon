"""Render the last 12 months of public contributions, summed per week, as an SVG line chart."""
import datetime as dt
import json
import os
import sys
import urllib.request

USER, OUT = sys.argv[1], sys.argv[2]
QUERY = """query($u:String!,$from:DateTime!,$to:DateTime!){user(login:$u){contributionsCollection(from:$from,to:$to){
contributionCalendar{weeks{contributionDays{date contributionCount}}}}}}"""

end = dt.datetime.now(dt.timezone.utc)
start = end - dt.timedelta(days=364)
request = urllib.request.Request(
    "https://api.github.com/graphql",
    data=json.dumps({"query": QUERY, "variables": {"u": USER, "from": start.isoformat(), "to": end.isoformat()}}).encode(),
    headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json"},
)
with urllib.request.urlopen(request, timeout=30) as response:
    payload = json.load(response)
if "errors" in payload:
    sys.exit(f"GraphQL error: {payload['errors']}")

weeks = payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
days = [week["contributionDays"][0] for week in weeks]
counts = [sum(day["contributionCount"] for day in week["contributionDays"]) for week in weeks]

W, H, LEFT, RIGHT, TOP, BOTTOM = 860, 320, 56, 24, 56, 44
plot_w, plot_h = W - LEFT - RIGHT, H - TOP - BOTTOM
step = max(1, (max(counts, default=0) + 3) // 4)
y_max = step * 4
x = lambda i: LEFT + i * plot_w / max(1, len(days) - 1)
y = lambda v: TOP + plot_h - v * plot_h / y_max

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
    f'aria-label="Weekly contributions over the last 12 months" font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">',
    '<defs><linearGradient id="fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#58A6FF" stop-opacity=".28"/>'
    '<stop offset="1" stop-color="#58A6FF" stop-opacity="0"/></linearGradient></defs>',
    f'<rect width="{W}" height="{H}" rx="8" fill="#161B22"/>',
    f'<text x="{W / 2}" y="30" fill="#E6EDF3" font-size="15" font-weight="600" text-anchor="middle">Last 12 months · {sum(counts)} contributions</text>',
]
for tick in range(5):
    value = step * tick
    parts.append(f'<line x1="{LEFT}" x2="{W - RIGHT}" y1="{y(value):.1f}" y2="{y(value):.1f}" stroke="#30363D"/>')
    parts.append(f'<text x="{LEFT - 10}" y="{y(value) + 4:.1f}" fill="#8B949E" font-size="11" text-anchor="end">{value}</text>')
previous_month = None
for i, day in enumerate(days):
    date = dt.date.fromisoformat(day["date"])
    if date.month != previous_month and date.month % 2 == 0:
        label = date.strftime("%b")
        parts.append(f'<text x="{x(i):.1f}" y="{H - 16}" fill="#8B949E" font-size="11" text-anchor="middle">{label}</text>')
    previous_month = date.month
points = " ".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(counts))
parts.append(f'<polygon points="{x(0):.1f},{y(0):.1f} {points} {x(len(days) - 1):.1f},{y(0):.1f}" fill="url(#fill)"/>')
parts.append(f'<polyline points="{points}" fill="none" stroke="#58A6FF" stroke-width="2.5" stroke-linejoin="round"/>')
parts += [f'<circle cx="{x(i):.1f}" cy="{y(v):.1f}" r="3" fill="#58A6FF"/>' for i, v in enumerate(counts) if v]
parts.append("</svg>\n")

with open(OUT, "w", encoding="utf-8") as output:
    output.write("".join(parts))
