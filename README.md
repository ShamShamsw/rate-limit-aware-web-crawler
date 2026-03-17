# Beginner Project 24: Rate-Limit-Aware Web Crawler

**Time:** 4-6 hours  
**Difficulty:** Intermediate Beginner  
**Focus:** Web crawling fundamentals, robots.txt compliance, retry/backoff strategies, URL deduplication, and SQLite persistence

---

## Why This Project?

Web crawling appears simple at first: request a URL, parse links, repeat. In practice, production crawlers must be polite, resilient, and restartable.

This project teaches a professional crawling workflow where you can:

- enforce robots.txt rules before fetching,
- throttle requests per host to avoid rate-limit abuse,
- retry failed requests using exponential backoff,
- normalize and deduplicate URLs to prevent infinite loops,
- persist crawl state and page records in SQLite,
- and resume crawling from previous progress after interruption.

---

## More Projects

You can access this project and more in this separate repository:

[student-interview-prep](https://github.com/ShamShamsw/student-interview-prep.git)

---

## What You Will Build

You will build a command-line crawler that:

1. Accepts one or more seed URLs.
2. Reads and honors robots.txt rules for each target host.
3. Applies request throttling (minimum delay between requests per host).
4. Retries transient failures (timeout, 429, 5xx) with exponential backoff.
5. Extracts links from HTML pages and normalizes them.
6. Deduplicates URLs so each page is crawled once.
7. Persists fetched pages, metadata, and crawl frontier to SQLite.
8. Prints live crawl stats (queued, crawled, failed, skipped).
9. Supports resume mode using saved crawl state.

---

## Requirements

- Python 3.11+
- `requests`
- `beautifulsoup4`

Install with:

```bash
pip install -r requirements.txt
```

---

## Example Session

```text
======================================================================
   RATE-LIMIT-AWARE WEB CRAWLER
======================================================================

Configuration:
   Seed URLs: 2
   Max pages: 50
   Per-host delay: 1.00s
   Request timeout: 8.0s
   Max retries: 3
   Backoff factor: 2.0
   Resume mode: enabled

Startup:
   Existing crawl database: data/runs/crawl_state.db
   Previous run found: 18 pages already crawled
   Frontier restored: 11 pending URLs

Fetching:
   [OK]  https://example.com                      status=200 links=14
   [OK]  https://example.com/docs                 status=200 links=9
   [SKIP robots] https://example.com/private
   [RETRY 1/3 in 1.0s] https://example.com/api (429 Too Many Requests)
   [RETRY 2/3 in 2.0s] https://example.com/api (429 Too Many Requests)
   [OK]  https://example.com/api                  status=200 links=4
   [FAIL] https://example.com/old-page            status=404

Summary:
   Pages crawled: 50
   Pages failed: 3
   Pages skipped: 7
   Unique hosts: 1
   Elapsed time: 42.8s

Artifacts saved:
   Crawl database: data/runs/crawl_state.db
   Run summary:    data/runs/crawl_summary.json
```

---

## Build Order

Follow this order for clean architecture:

1. `storage.py` - SQLite schema, read/write helpers, crawl state persistence
2. `models.py` - Config and record constructors for tasks, pages, and summaries
3. `operations.py` - robots checks, throttling, retry/backoff, crawl orchestration
4. `display.py` - banners, progress lines, and final report formatting
5. `main.py` - top-level orchestration and dependency wiring

---

## Step-by-Step Instructions

### Step 1: Implement `storage.py`

Create functions to:
- create local data directories,
- initialize SQLite schema,
- insert page fetch records,
- track discovered and pending URLs,
- and save/load crawl progress for resume mode.

**Key functions:**
- `ensure_data_dirs() -> None`
- `initialize_database(db_path: str) -> None`
- `insert_page_record(db_path: str, page: dict) -> None`
- `has_visited_url(db_path: str, normalized_url: str) -> bool`
- `save_frontier_snapshot(filename: str, frontier: list) -> None`
- `load_frontier_snapshot(filename: str) -> list`

### Step 2: Implement `models.py`

Define data models and configuration:
- crawler configuration,
- URL task record,
- fetch result record,
- and run summary record.

**Key structures:**
- `create_crawler_config(...) -> dict`
- `create_url_task(...) -> dict`
- `create_fetch_result(...) -> dict`
- `create_run_summary(...) -> dict`

### Step 3: Implement `operations.py`

Build the core crawling pipeline:
- robots permission checks,
- per-host throttle control,
- retry with exponential backoff,
- link extraction and URL normalization,
- dedupe checks before queueing,
- and run summary generation.

**Key functions:**
- `is_allowed_by_robots(url: str, user_agent: str) -> bool`
- `throttle_request(host: str, host_last_request: dict, delay_seconds: float) -> None`
- `fetch_with_retries(url: str, config: dict) -> dict`
- `extract_links(base_url: str, html: str) -> list[str]`
- `normalize_url(url: str) -> str`
- `run_core_flow() -> dict`

### Step 4: Implement `display.py`

Format output for readability:
- startup banner,
- configuration block,
- per-URL progress lines,
- and final crawl summary.

**Key functions:**
- `format_header() -> str`
- `format_startup_guide(config: dict, profile: dict) -> str`
- `format_fetch_event(event: dict) -> str`
- `format_run_report(summary: dict) -> str`

### Step 5: Implement `main.py`

Orchestrate the workflow:
1. ensure data directories,
2. print header,
3. load/create config,
4. print startup info,
5. run crawler flow,
6. print final report.

---

## Done Criteria

- [ ] The project runs from `main.py` without crashes.
- [ ] robots.txt rules are checked before fetching each URL.
- [ ] Request throttling is enforced per host.
- [ ] Retry with exponential backoff works for transient failures.
- [ ] URL normalization + dedupe prevents repeat crawling.
- [ ] Crawl state can be resumed from previous run.
- [ ] Crawled page metadata is persisted to SQLite.
- [ ] Run summary is saved to `data/runs/crawl_summary.json`.
- [ ] Every function has a docstring.
- [ ] Code remains separated by concern (storage/models/operations/display/main).

---

## Stretch Goals

1. Add async crawling with `aiohttp` while preserving host-level throttling.
2. Add domain allowlist/denylist configuration.
3. Store page content hash and skip near-duplicate content.
4. Add sitemap.xml discovery for faster URL expansion.
5. Export crawl graph (page -> outlinks) as CSV/JSON for analysis.
6. Add a politeness dashboard showing request rate by host.
7. Implement checkpoint rotation and retention for long-running crawls.
