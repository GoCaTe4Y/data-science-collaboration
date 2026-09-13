"""Data validation utilities for ML pipeline."""
def validate_dataset(df):
    """Validate dataset before processing.

    Checks for null values and duplicate rows. Returns a list of issues (empty if none).
    """
    issues = []

    # Check for null values
    null_counts = df.isnull().sum()
    if null_counts.any():
        issues.append(f"Null values found: {null_counts[null_counts > 0].to_dict()}")

    # Check for duplicate rows
    duplicates = int(df.duplicated().sum())
    if duplicates > 0:
        issues.append(f"Duplicate rows found: {duplicates}")

    return issues


def clean_dataset(df):
    """Basic dataset cleaning operations.

    Removes duplicate rows and fills numeric nulls with the column median.
    Returns a cleaned copy of the dataframe.
    """
    # Work on a copy
    df_clean = df.drop_duplicates().copy()

    # Fill numeric nulls with median
    numeric_columns = df_clean.select_dtypes(include=['number']).columns
    if len(numeric_columns) > 0:
        df_clean[numeric_columns] = df_clean[numeric_columns].fillna(
            df_clean[numeric_columns].median()
        )

    return df_clean