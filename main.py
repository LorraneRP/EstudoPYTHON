import zipfile # import the module zi  pfile
from zipfile import ZipFile #import the class
from os.path import join as pj
import os #tratar SO
import geopandas as gpd #import geopandas lê arquivos geograficos e faz operações com eles tranformando em dataframes

PATH=pj(os.getcwd()) #path to the data folder
print(os.listdir(PATH))

#open the zip file


def indigenas():
    with ZipFile(pj(PATH,'indigenous_area_legal_amazon.zip'),'r') as zip:
        zip.printdir()
        zip.extractall(PATH)
        
#indigenas() 

area_indigena=gpd.read_file(pj(PATH,'indigenous_area_legal_amazon.shp')) 
print(area_indigena.head())
print(area_indigena.columns)

area_indigena.plot()