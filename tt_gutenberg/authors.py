import pandas as pd
from tt_gutenberg.data import load_data


def list_authors(by_languages=False, alias=False):
    authors = load_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main'
                        '/data/2025/2025-06-03/gutenberg_authors.csv'
    )
    metadata = load_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main'
                         '/data/2025/2025-06-03/gutenberg_metadata.csv'
    )
    languages = load_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main'
                          '/data/2025/2025-06-03/gutenberg_languages.csv'
    )

    author_works = pd.merge(authors, metadata, on="gutenberg_author_id")
    author_languages = pd.merge(author_works, languages, on="gutenberg_id")

    if by_languages:
        if alias:
            language_counts = (
                author_languages
                .groupby("alias")["language_y"]
                .nunique()
                .sort_values(ascending=False)
            )
            return language_counts.index.tolist()



