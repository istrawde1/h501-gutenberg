import pandas as pd


DATA = (
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/"
    "data/2025/2025-06-03/"
)


def get_data():
    """Return merged Project Gutenberg author and metadata data."""
    authors = pd.read_csv(DATA + "gutenberg_authors.csv")
    metadata = pd.read_csv(DATA + "gutenberg_metadata.csv")

    author_works = pd.merge(
        authors,
        metadata,
        on="gutenberg_author_id"
    )

    return author_works