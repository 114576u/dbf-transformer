
import os

from dbfread import DBF
from pandas import DataFrame


def load_dbf_into_pd(FILENAME):
    # print('load_dbf_into_pd: ', FILENAME)
    table = DBF(FILENAME, load=True)
    # print('load_dbf_into_pd table created')
    return DataFrame(iter(table))

def convert_frame_to_csv(dataframe, CSV_FILENAME):
    dataframe.to_csv(CSV_FILENAME)
    print('          File converted succesfully:', CSV_FILENAME)

def apply_conversion(filename):
    dbf_file_name = filename
    csv_file_name = str(dbf_file_name).replace(".dbf", ".csv")
    convert_frame_to_csv(
        load_dbf_into_pd(dbf_file_name),
        csv_file_name
    )

def all_dbf_in_folder(directory):
    # move to directory as working folder
    os.chdir(directory)
    for file_name in os.listdir(directory):
        if file_name.endswith(".dbf"):
            print('  Converting file:', file_name)
            apply_conversion(file_name)

if __name__ == '__main__':
    directory = r'C:\Users\Administrador\PycharmProjects\dbf-transformer\multiple-dbf'
    print('Starting to convert files from folder ', directory)
    all_dbf_in_folder(directory)
    print('Conversion for all files in folder completed')
