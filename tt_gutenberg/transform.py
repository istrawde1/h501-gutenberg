import pandas as pd


DATA = {
    "authors": (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/"
        "data/2025/2025-06-03/gutenberg_authors.csv"
    ),
    "metadata": (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/"
        "data/2025/2025-06-03/gutenberg_metadata.csv"
    ),
}


def get_data():
    """Return merged Project Gutenberg author and metadata data."""
    sources = list(DATA.values())

    authors = pd.read_csv(sources[0])
    metadata = pd.read_csv(sources[1])

    author_works = pd.merge(
        authors,
        metadata,
        on="gutenberg_author_id"
    )

    return author_works