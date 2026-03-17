"""
storage.py - Persistence layer for Project 24: Rate-Limit-Aware Web Crawler
=============================================================================

Handles:
    - Local data directory setup
    - SQLite database initialization and writes
    - Crawl frontier snapshot persistence for resume mode
    - JSON run summary save/load helpers
"""

from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent / "data"
RUNS_DIR = DATA_DIR / "runs"


def ensure_data_dirs() -> None:
    """Create local data and runs directories if missing.

    Returns:
        None
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)


def initialize_database(db_path: str) -> None:
    """Create SQLite tables required for crawl persistence.

    Parameters:
        db_path (str): Path to SQLite database file.

    Returns:
        None

    Suggested tables:
        - pages(url PRIMARY KEY, status_code, fetched_at, content_hash, title, depth, error)
        - frontier(url PRIMARY KEY, depth, discovered_from, discovered_at)
        - run_events(id INTEGER PRIMARY KEY AUTOINCREMENT, event_type, payload_json, created_at)

    TODO: Implement sqlite3 schema creation with CREATE TABLE IF NOT EXISTS.
    """
    pass


def insert_page_record(db_path: str, page_record: dict) -> None:
    """Insert or update one crawled page record in SQLite.

    Parameters:
        db_path (str): SQLite database path.
        page_record (dict): Normalized page record to persist.

    Returns:
        None

    TODO: Implement UPSERT for page rows.
    """
    pass


def has_visited_url(db_path: str, normalized_url: str) -> bool:
    """Return whether a normalized URL already exists in the pages table.

    Parameters:
        db_path (str): SQLite database path.
        normalized_url (str): Canonicalized URL string.

    Returns:
        bool: True if URL is already persisted as crawled.

    TODO: Implement URL existence check query.
    """
    pass


def save_frontier_snapshot(filename: str, frontier: list) -> None:
    """Persist crawl frontier queue to JSON in runs directory.

    Parameters:
        filename (str): Snapshot filename.
        frontier (list): Serializable queue of URL task records.

    Returns:
        None

    TODO: Implement JSON snapshot save.
    """
    pass


def load_frontier_snapshot(filename: str):
    """Load crawl frontier snapshot from runs directory.

    Parameters:
        filename (str): Snapshot filename.

    Returns:
        list: Previously saved frontier queue, or empty list if unavailable.

    TODO: Implement snapshot load with fallback.
    """
    pass


def save_run_summary(filename: str, summary: dict) -> None:
    """Save final crawl summary as JSON in runs directory.

    Parameters:
        filename (str): Output summary filename.
        summary (dict): Summary record.

    Returns:
        None

    TODO: Implement JSON serialization with indentation.
    """
    pass


def load_json(filename: str):
    """Load JSON data from data directory.

    Parameters:
        filename (str): JSON filename in data directory.

    Returns:
        object: Parsed JSON, or empty list if file missing.
    """
    ensure_data_dirs()
    path = DATA_DIR / filename
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))
