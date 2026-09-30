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
    authors = pd.read_csv(DATA["authors"])
    metadata = pd.read_csv(DATA["metadata"])

    metadata = metadata.drop(columns="author")

    author_works = pd.merge(
        authors,
        metadata,
        on="gutenberg_author_id"
    )

    return author_works