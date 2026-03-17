"""
main.py - Entry point for Project 24: Rate-Limit-Aware Web Crawler
===================================================================

Thin-controller module that only orchestrates calls to:
    - operations.py for crawl workflow logic
    - display.py for presentation formatting
    - storage.py for persistence setup
    - models.py for configuration records
"""

from display import format_header, format_startup_guide, format_run_report
from models import create_crawler_config
from operations import load_crawl_profile, run_core_flow
from storage import ensure_data_dirs


def main() -> None:
    """Run one complete crawl session.

    Workflow:
        1. Ensure data directories exist
        2. Print header banner
        3. Build crawler config and startup profile
        4. Print startup guide
        5. Run crawl pipeline (operations.run_core_flow)
        6. Print final crawl report

    Returns:
        None

    TODO: Implement any additional orchestration needs for advanced CLI options.
    """
    # Prepare directories before any file operations.
    ensure_data_dirs()

    # Print session header.
    print(format_header())

    # Build crawler configuration.
    config = create_crawler_config()

    # Build startup profile for display.
    profile = load_crawl_profile()

    # Print startup guide.
    print(format_startup_guide(config, profile))

    # Run crawl workflow.
    summary = run_core_flow()

    # Print final report.
    print(format_run_report(summary))


if __name__ == "__main__":
    # Guard keeps imports side-effect free for tests and reuse.
    main()
