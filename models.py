"""
models.py - Data models for Project 24: Rate-Limit-Aware Web Crawler
========================================================================

Defines:
    - Crawler configuration (timeouts, retries, throttling, limits)
    - URL task records for the frontier queue
    - Fetch result records per request attempt
    - Final run summary record for reporting and persistence
"""

from datetime import datetime
from typing import Dict, Any, Optional, List


def _utc_timestamp() -> str:
    """Return an ISO-8601 UTC timestamp string.

    Returns:
        str: UTC timestamp with trailing Z.
    """
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


def create_crawler_config(
    seed_urls: Optional[List[str]] = None,
    max_pages: int = 50,
    request_timeout_seconds: float = 8.0,
    max_retries: int = 3,
    backoff_factor: float = 2.0,
    min_delay_per_host_seconds: float = 1.0,
    user_agent: str = "StudentCrawler/1.0 (+https://example.local)",
    resume_enabled: bool = True,
) -> Dict[str, Any]:
    """Create a default crawler configuration record.

    Parameters:
        seed_urls (list[str] | None): Initial URLs to start the crawl from.
        max_pages (int): Maximum number of pages to fetch in one run.
        request_timeout_seconds (float): Timeout per HTTP request.
        max_retries (int): Number of retries for transient failures.
        backoff_factor (float): Base multiplier for exponential backoff.
        min_delay_per_host_seconds (float): Minimum delay between same-host requests.
        user_agent (str): User-Agent string sent in requests and robots checks.
        resume_enabled (bool): Whether previous crawl state should be resumed.

    Returns:
        dict: Configuration dictionary used throughout the crawl pipeline.

    TODO: Implement configuration creation with validation/default seed URLs.
    """
    pass


def create_url_task(
    url: str,
    depth: int,
    discovered_from: Optional[str] = None,
    discovered_at: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a task record for one URL in the crawl frontier.

    Parameters:
        url (str): Absolute URL to crawl.
        depth (int): Crawl depth from seed URL.
        discovered_from (str | None): Parent URL where this link was found.
        discovered_at (str | None): Timestamp when this task was discovered.

    Returns:
        dict: URL task record ready for queue/frontier storage.

    TODO: Implement URL task record creation.
    """
    pass


def create_fetch_result(
    url: str,
    status: str,
    status_code: Optional[int],
    attempt_count: int,
    elapsed_seconds: float,
    discovered_links: int,
    error_message: Optional[str] = None,
) -> Dict[str, Any]:
    """Create one fetch event/result record.

    Parameters:
        url (str): Requested URL.
        status (str): Outcome category ('ok', 'retry', 'failed', 'skipped_robots').
        status_code (int | None): HTTP status code if available.
        attempt_count (int): Number of request attempts used.
        elapsed_seconds (float): Request time for the final attempt.
        discovered_links (int): Number of links extracted from the response body.
        error_message (str | None): Optional failure details.

    Returns:
        dict: Fetch result record for logs, DB insertion, and final summary.

    TODO: Implement fetch result creation with timestamp.
    """
    pass


def create_run_summary(
    config: Dict[str, Any],
    pages_crawled: int,
    pages_failed: int,
    pages_skipped: int,
    unique_hosts: int,
    elapsed_seconds: float,
    artifacts: Dict[str, str],
) -> Dict[str, Any]:
    """Create the final crawl summary record.

    Parameters:
        config (dict): Crawler configuration snapshot.
        pages_crawled (int): Count of successful page fetches.
        pages_failed (int): Count of permanently failed URLs.
        pages_skipped (int): Count skipped by robots or dedupe policy.
        unique_hosts (int): Number of unique hosts touched during run.
        elapsed_seconds (float): Total run duration.
        artifacts (dict): Saved output paths (DB, JSON summary, etc.).

    Returns:
        dict: Complete run summary for display and persistence.

    TODO: Implement summary creation.
    """
    pass
