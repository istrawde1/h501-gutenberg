import pandas as pd


DATA = {
    "gutenberg_authors": (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/"
        "data/2025/2025-06-03/gutenberg_authors.csv"
    ),
    "gutenberg_metadata": (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/"
        "data/2025/2025-06-03/gutenberg_metadata.csv"
    ),
}


def get_data():
    """Return merged Project Gutenberg author and metadata data."""
    authors = pd.read_csv(DATA["gutenberg_authors"])
    metadata = pd.read_csv(DATA["gutenberg_metadata"])

    author_works = pd.merge(
        authors,
        metadata,
        on="gutenberg_author_id"
    )

    return author_works