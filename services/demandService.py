import pandas as pd
import os 
import glob
from entities.demandEntity import demandEntity
from glob import glob

class demandService:
    def getData(self):
        path = os.environ['USERPROFILE'] + '\Downloads'
        print(f'obtendo demandas do arquivo {path}')
        files = glob(path + '\demand_download*')

        if not any(files):
            print('nenhum arquivo de demanda localizado')
            return        

        fileDict = {}

        for file in files:
            fileDict[file] = os.path.getmtime(file)

        newestTimestamp = max(fileDict.values())

        file = ""
        for (key,value) in fileDict.items():
            if (value == newestTimestamp):
                file = key  

        dataframe = pd.read_excel(file)
        content = dataframe.values.tolist()

        list = []

        for row in content:
            list.append(demandEntity(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18]))

        return list
