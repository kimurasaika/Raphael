---
description: Raphael deep-research playbook — how to dig into hard/niche topics across web, X, Reddit, YouTube, GitHub. Load before any deep or multi-source research.
---

Raphael's research playbook. Follow it for any topic deeper than one lookup.
If Raphael persona is not active, still follow the method.

## Method
1. **Scope** — restate the question as 3-6 concrete sub-questions. Note the
   topic's native language (e.g. Japanese band → search in Japanese too).
2. **Wide pass** — WebSearch `standard` in parallel, one query per
   sub-question, in English AND the native language. Switch to `extended`
   only when results are thin, stale, or niche.
4. **Primary sources** — go to the origin: official site, artist/author's own
   account, paper, repo, original post. Wiki/blog = map, not proof.
5. **Cross-check** — every key fact needs 2 independent sources, or is
   marked "1 source". Record the date of each fact; prefer newest for
   anything that changes (members, prices, releases).
6. **Synthesize** — answer the sub-questions, flag conflicts and gaps,
   list sources. Never fill a gap by guessing.

## Source recipes
| Source | How |
|---|---|
| General web | WebSearch → WebFetch on best hits |
| Single X post | WebFetch `https://api.fxtwitter.com/<user>/status/<id>` |
| X profile/search, login-walled sites | Claude in Chrome (Master's logged-in session), new tab, read only |
| X search (Master logged in since 2026-10-06) | Chrome → `x.com/search?q=from:<acct> (kw1 OR kw2)&f=live`; get_page_text returns only 1 tweet → use javascript_tool to map `article` → `time[datetime]` + `[data-testid="tweetText"]`, ≤220 chars each, few scrolls per call (long loops time out at 45s) |
| Facebook (Master logged in) | Chrome → `facebook.com/search/posts?q=<name> <keyword>`; Thai idol/brand announcements are often IMAGES — scroll + `zoom` screenshot to read them, get_page_text misses them |
| Reddit | WebFetch thread/search URL + `.json` (e.g. `reddit.com/r/x/search.json?q=...&restrict_sr=1`) |
| YouTube metadata/search | `python -m yt_dlp --dump-json --skip-download "ytsearch10:<query>"` |
| YouTube transcript | `youtube_transcript_api` (`YouTubeTranscriptApi().fetch(id, languages=['ja','en'])`) |
| YouTube channel uploads | `python -m yt_dlp --flat-playlist --print "%(view_count)s %(title)s" "<channel_url>/videos"` (official MV descriptions often hold full member/credit lists — diff them across releases to spot line-up changes) |
| Fandom / MediaWiki (WebFetch gets 402) | `curl -s -A "Mozilla/5.0" "https://<wiki>.fandom.com/api.php?action=parse&page=<Page>&prop=wikitext&format=json&formatversion=2"` |
| Thai company (legal entity, capital, equity, shareholders count) | brand name ≠ legal name — find legal name first (wiki/T&C), then WebFetch `data.creden.co/company/general/<13-digit reg no>` + `curl -A "<browser UA>" dataforthai.com/company/<reg no>/` (WebFetch gets 403). Yearly P&L: Master has a dataforthai account (2026-10-06) → Chrome to the company page, then javascript_tool `Object.values(Chart.instances)` → `chart-finance-m-1/2/3` = revenue+net profit / assets / liabilities+equity, all years since registration. "(มหาชน)" absent ⇒ cannot be SET/mai-listed |
| ML workflow / winning Kaggle methods | Master's playbook: `python <playbook>/tools/search.py "<task>"` (see Method step 2) |
| GitHub | `gh` CLI / `gh api` |
| Many angles, long report | `deep-research` skill (parallel subagents) — only when Master asks for a full report |

On Windows set `PYTHONIOENCODING=utf-8` before printing non-ASCII output.

## Filters
- Down-rank info-marketing / course-selling / affiliate sources; check what
  the author sells before trusting claims.
- Fan wikis and AI-generated SEO pages: use for leads, verify elsewhere.
- No anti-bot evasion scrapers (Patchright etc.) — ToS + account-ban risk.
  Use Master's browser session instead.

## Output
Lead with the answer in Master's language (Thai), keep proper nouns in
original script + romaji/English. End with a Sources list.
