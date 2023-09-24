import os

folder_path = 'Img'
subpath = 'people'
files = os.listdir(folder_path+'/'+subpath)
for file in files:
    if file.endswith('.svg'):
        sp = file.split('.')[0].split(',')[0];
        print('{img: "'+subpath + '/' + file + '", name:"' + sp + '"},')
