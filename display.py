"""
display.py - Presentation helpers for Project 24: Rate-Limit-Aware Web Crawler
===============================================================================

Formats:
    - Header banner
    - Startup configuration/profile block
    - Per-request event lines
    - Final run summary report
"""

from typing import Dict, Any


def format_header() -> str:
    """Return an ASCII banner for the crawl session.

    Returns:
        str: Header text with decorative separators.

    TODO: Implement styled banner formatting.
    """
    pass


def format_startup_guide(config: Dict[str, Any], profile: Dict[str, Any]) -> str:
    """Format startup configuration and resume profile details.

    Parameters:
        config (dict): Crawler configuration.
        profile (dict): Startup profile loaded from persisted state.

    Returns:
        str: Multiline startup guide string.

    TODO: Implement startup section formatting.
    """
    pass


def format_fetch_event(event: Dict[str, Any]) -> str:
    """Format one crawl event line for console output.

    Parameters:
        event (dict): Fetch result record.

    Returns:
        str: Human-readable single-line status output.

    Example output:
        [OK] https://example.com status=200 links=12

    TODO: Implement event rendering for ok/retry/fail/skip states.
    """
    pass


def format_run_report(summary: Dict[str, Any]) -> str:
    """Format the final crawl summary.

    Parameters:
        summary (dict): Run summary from models.create_run_summary.

    Returns:
        str: Full formatted summary including artifact paths.

    TODO: Implement report formatting.
    """
    pass
