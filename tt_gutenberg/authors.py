from tt_gutenberg.transform import get_data


def list_authors(by_languages=False, alias=False):
    """Return a list of Project Gutenberg authors."""
    author_languages = get_data()

    if by_languages:
        if alias:
            language_counts = (
                author_languages
                .groupby("alias")["language_y"]
                .nunique()
                .sort_values(ascending=False)
            )
            return language_counts.index.tolist()
        