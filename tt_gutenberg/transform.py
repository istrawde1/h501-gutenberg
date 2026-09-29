import pandas as pd


def get_data():
    """Return merged Project Gutenberg data."""
    authors = pd.read_csv(
        'https://raw.githubusercontent.com/rfordatascience/tidytuesday/main'
        '/data/2025/2025-06-03/gutenberg_authors.csv'
    )
    metadata = pd.read_csv(
        'https://raw.githubusercontent.com/rfordatascience/tidytuesday/main'
        '/data/2025/2025-06-03/gutenberg_metadata.csv'
    )
    languages = pd.read_csv(
        'https://raw.githubusercontent.com/rfordatascience/tidytuesday/main'
        '/data/2025/2025-06-03/gutenberg_languages.csv'
    )

    author_works = pd.merge(
        authors,
        metadata,
        on="gutenberg_author_id"
    )

    author_languages = pd.merge(
        author_works,
        languages,
        on="gutenberg_id"
    )

    return author_languages
