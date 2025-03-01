import pandas as pd
from utils.file_io import read_orbital_elements_file, get_debris_file_list


def load_and_merge_debris_data(deb_folder, labels_df):
    """
    Loads each debris file from deb_folder (e.g., 'deb_train'),
    merges the first row of each debris file with label info (if available).
    Returns a consolidated DataFrame for EDA or modeling.
    """
    debris_files = get_debris_file_list(deb_folder=deb_folder)
    records = []

    for path in debris_files:
        filename = path.split('/')[-1]  # e.g. "eledebtrain001.dat"
        deb_id_str = filename.replace("eledebtrain", "").replace(".dat", "")  # "001"

        # Read the full time-series
        df_deb = read_orbital_elements_file(path)
        if not df_deb.empty:
            row = df_deb.iloc[0].to_dict()
            row['deb_id'] = deb_id_str

            # Attach label info if available
            if deb_id_str in labels_df.index:
                for col in labels_df.columns:
                    row[col] = labels_df.loc[deb_id_str, col]

            records.append(row)

    df_merged = pd.DataFrame(records)

    # Basic cleaning example
    # Remove duplicates, ensure eccentricity <= 1, etc.
    df_merged = df_merged[df_merged['ecc'] <= 1.0]  # sanity check
    df_merged.drop_duplicates(subset=['deb_id'], inplace=True)

    return df_merged
