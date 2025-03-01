import os
import glob
import pandas as pd


def read_orbital_elements_file(filepath):
    """
    Reads a .dat file containing time-series orbital elements.
    Columns (in order):
      1. epoch (days from JD2000 noon)
      2. semimajor axis (km)
      3. eccentricity
      4. inclination (deg)
      5. mean_anomaly (deg)
      6. arg_perigee (deg)
      7. raan (deg)
    Returns a pandas DataFrame.
    """
    col_names = [
        'epoch', 'sma', 'ecc', 'inc',
        'mean_anomaly', 'arg_perigee', 'raan'
    ]
    df = pd.read_csv(filepath, sep=r'\s+', names=col_names, header=None)
    return df


def read_labels_train(filepath):
    """
    Reads labels_train.dat, returning a DataFrame:
        Index: '001', '002', ...
        Columns: [sat_id, area_mass_ratio, gen_epoch, gen_sma, gen_ecc, gen_inc, gen_M, gen_omega, gen_raan].
    """
    data_rows = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        parts = line.strip().split()
        sat_id = parts[0]
        area_mass_ratio = float(parts[1])
        gen_epoch = float(parts[2])
        gen_sma = float(parts[3])
        gen_ecc = float(parts[4])
        gen_inc = float(parts[5])
        gen_M = float(parts[6])
        gen_omega = float(parts[7])
        gen_raan = float(parts[8])

        row_dict = {
            'sat_id': sat_id,
            'area_mass_ratio': area_mass_ratio,
            'gen_epoch': gen_epoch,
            'gen_sma': gen_sma,
            'gen_ecc': gen_ecc,
            'gen_inc': gen_inc,
            'gen_M': gen_M,
            'gen_omega': gen_omega,
            'gen_raan': gen_raan
        }
        data_rows.append(row_dict)

    df_labels = pd.DataFrame(data_rows)
    df_labels.index = [f"{i+1:03d}" for i in range(len(df_labels))]
    return df_labels


def get_debris_file_list(deb_folder='deb_train'):
    """
    Returns a sorted list of debris .dat files in deb_folder.
    Example: ["deb_train/eledebtrain001.dat", ...]
    """
    pattern = os.path.join(deb_folder, 'eledebtrain*.dat')
    files = glob.glob(pattern)
    files.sort()
    return files
