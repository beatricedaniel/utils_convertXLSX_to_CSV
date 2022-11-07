import os

# Modules à installer
import pandas as pd 

def getFilename():
    try:
        name = input('Entrez le nom du fichier : ')
        extension = '.xlsx'
        filename = name + extension
        return filename
    except ValueError as err:
        print(err)
        return str(err)

def getSheetName():
    try:
        sheetname = input('Entrez le nom de la feuille : ')
        return sheetname
    except ValueError as err:
        print(err)
        return str(err)

def convertXLSXFileToDataframe():
    try:
        filename = getFilename()
        sheetname = getSheetName()
        converted_df = pd.read_excel(filename,
                                    sheet_name=sheetname,
                                    header=0)
        return filename, sheetname, converted_df
    except ValueError as err:
        print(err)
        return str(err) 

def checkIfPathExists(file):
    if os.path.exists(file):
        os.remove(file)
        print('Ancien fichier écrasé')

def convertDataframeToCSV():
    try:
        filename, sheetname, converted_df = convertXLSXFileToDataframe()
        name = name = filename[:-5]
        csv_filename = name + '_' + sheetname + ".csv"
        print(csv_filename)
        checkIfPathExists(csv_filename)
        csv_file = converted_df.to_csv(csv_filename,
                                    sep=';',
                                    encoding='UTF-8')
        return
    except ValueError as err:
        print(err)
        return str(err) 

# Exécution
convertDataframeToCSV()