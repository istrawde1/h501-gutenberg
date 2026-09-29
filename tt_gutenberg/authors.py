from tt_gutenberg.transform import get_data


def list_authors(by_languages=False, alias=False):
    """Return a list of Project Gutenberg authors."""
    data = get_data()

    if by_languages and alias:
        language_counts = (
            data
            .groupby("alias")["language"]
            .nunique()
            .sort_values(ascending=False)
        )

        return language_counts.index.tolist()