import os
import shutil
import random
import pandas as pd

IN_DIR = 'input/given/train'
TRAIN_DIR = 'input/processed/train'
VALID_DIR = 'input/processed/valid'

df = pd.read_csv('train_master.tsv', delimiter='\t')

# 色ごとのディレクトリを作成
color_id = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

for name in color_id:
	os.mkdir(os.path.join(TRAIN_DIR, name))

for name in color_id:
	os.mkdir(os.path.join(VALID_DIR, name))

for f in sorted(os.listdir(IN_DIR)):
	if not f.startswith('.') and os.path.isfile(os.path.join(IN_DIR, f)):
		i = df[df['file_name'] == f].ix[:, 1].values
		source = os.path.join(IN_DIR, f)
		dest = os.path.join(TRAIN_DIR, str(i[0]))
		
		shutil.copy(source, dest)
		continue

# 訓練データの各ディレクトリからランダムに15枚を検証データとする
for d in os.listdir(TRAIN_DIR):
    path = os.path.join('input', 'processed', 'train1', d, '*.jpg')
    files = sorted(glob.glob(path))
    random.shuffle(files)
    for f in files[:15]:
    	dest = os.path.join(VALID_DIR, d)
    	shutil.move(f, dest)
