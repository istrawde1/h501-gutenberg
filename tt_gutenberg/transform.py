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
    frames = []

    for value in DATA.values():
        if isinstance(value, pd.DataFrame):
            frames.append(value)
        else:
            frames.append(pd.read_csv(value))

    authors = next(
        frame for frame in frames
        if "alias" in frame.columns
    )

    metadata = next(
        frame for frame in frames
        if "gutenberg_id" in frame.columns
        and "title" in frame.columns
    )

    return pd.merge(
        authors,
        metadata,
        on="gutenberg_author_id"
    )