
from dbfread import DBF
from pandas import DataFrame


def load_dbf_into_pd(FILENAME):
    table = DBF(FILENAME, load=True)
    return DataFrame(iter(table))

def convert_frame_to_csv(dataframe, CSV_FILENAME):
    dataframe.to_csv(CSV_FILENAME)

if __name__ == '__main__':
    FILENAME = 'ffc.dbf'
    CSV_FILENAME = 'ffc-dbf.csv'
    print('Starting to convert ', FILENAME)
    convert_frame_to_csv(
        load_dbf_into_pd(FILENAME),
        CSV_FILENAME
    )
    print('    File exported to ', CSV_FILENAME)

