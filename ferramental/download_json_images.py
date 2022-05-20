import os.path
import requests
import json
from tqdm import tqdm

def download_images(data, diretorio):
    num_dl = 0
    cont = 0
    for i in tqdm(range(len(data))):
        if data[i]["includes"]["media"]:
            for j in tqdm(range(len(data[i]["includes"]["media"]))):
                if(data[i]["includes"]["media"][j]["type"] == "animated_gif") : continue
                if(data[i]["includes"]["media"][j]["type"] == "video") : continue
                cont += 1
                try:
                    req = requests.get(data[i]["includes"]["media"][j]["url"], timeout=10)
                except requests.exceptions.ReadTimeout:
                    print("\nReadTimeout\n")
                except requests.exceptions.Timeout:
                    print("\nTimeout\n")
                if req.status_code == 200:
                    with open(os.path.join(diretorio, os.path.basename(data[i]["includes"]["media"][j]["url"])), 'wb') as f:
                        for chunk in req:
                            f.write(chunk)
                    num_dl += 1
                req.close()
    print(cont)
    return num_dl

if __name__ == '__main__':

    datasets = ['hashtag_forabolsonaro']
    for ds in datasets:
        with open('{}.json'.format(ds)) as f:
            data = json.load(f)
        if not os.path.exists(ds):
            os.mkdir(ds)
        print('Baixando imagens do dataset {}'.format(ds))
        num_dl = download_images(data, ds)
        print('{} imagens baixadas com sucesso do dataset {}.'.format(num_dl, ds))