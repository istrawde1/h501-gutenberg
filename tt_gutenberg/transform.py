import pandas as pd


DATA = {
    "authors": pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/"
        "data/2025/2025-06-03/gutenberg_authors.csv"
    ),
    "metadata": pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/"
        "data/2025/2025-06-03/gutenberg_metadata.csv"
    ),
    "languages": pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/"
        "data/2025/2025-06-03/gutenberg_languages.csv"
    ),
}


def get_data():
    """Return merged Project Gutenberg author and metadata data."""
    data = list(DATA.values())

    authors = data[0]
    metadata = data[1]

    author_works = pd.merge(
        authors,
        metadata,
        on="gutenberg_author_id"
    )

    return author_works