## Assuming a csv file has:
## Image Name (ImageID) in column 1 (line[0])
## Full Resolution URL (OriginalURL) in column 3 (line[2])
## Script permite o download de imagens presentes em um csv
## O script pode ser adaptado para funcionar com diversos csv's
## Basta a alteraçao do organizaçao das colunas que devem ser lidas
## O Dataset da VGKG tem a organização:
## Data da imagem na primeira linha (line[0]) com o formato YYYYMMDDHHMMSS 
## Url da imagem na segunda coluna (line[1])
## E link para o primeiro artigo onde a imagem foi encontrada na terceira coluna (line[2])

import sys
import urllib.request
from csv import reader
import os.path

csv_filename = "2019-vgkg-protest-image-dataset-20191030-labels"
max_images = 0

with open(csv_filename+".csv".format(csv_filename), 'r') as csv_file:
    for line in reader(csv_file):
        if os.path.isfile("dataset_images/" + line[0] + ".jpg"):
            print("Image skipped for {0}".format(line[0]))
        else:
            if line[1] != '' and line[0] != "ImageID":
                try:
                    urllib.request.urlretrieve(line[1], "dataset_images/" + line[0] + ".jpg") ##Foi necessario criar o diretorio para que as imagens fossem enviadas corretamente
                    print("Image saved for {0}".format(line[0]))
                    max_images += 1 ##Nao é a soluçao mais elegante mas posso trabalhar com ela
                    if max_images >= 50000:
                        print("Max number of {0} images has been reached".format(max_images))
                        break
                except:
                    print("Image not found for {0}".format(line[0]))
            else:
                print("No result for {0}".format(line[0]))