import pandas as pd
from tt_gutenberg.transform import get_data


def list_authors(by_languages=False, alias=False):
    """Return a list of Project Gutenberg authors."""
    author_works = get_data()

    languages = pd.read_csv(
        'https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/'
        'data/2025/2025-06-03/gutenberg_languages.csv'
    )

    author_languages = pd.merge(
        author_works,
        languages,
        on="gutenberg_id"
    )

    if by_languages:
        if alias:
            language_counts = (
                author_languages
                .groupby("alias")["language_y"]
                .nunique()
                .sort_values(ascending=False)
            )
            return language_counts.index.tolist()