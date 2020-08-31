# YOLOv3模型剪枝

## 一、数据处理

- 将标注数据放入data/Annotations,图片数据放入data/images
- 运行modify.py文件，避免因图片问题导致标注文件中图片的长宽为
0的问题
-将voc_label.py中classes修改为自己的训练类别，并分别运行maketxt.py、voc_label.py

## 二、模型剪枝
###  1.正常训练

- [x] 对应自己的训练数据修改data/voc.data以及voc.name
- [x] 同时修改yolov3.cfg中yolo层对应的filters以及classes  

          filters=3*(classes+5)
```bash
python3 train.py --data data/voc.data --batch-size 16 --accumulate 1 --weights weights/yolov3.weights --cfg cfg/yolov3.cfg
```
### 2.稀疏化训练

- [x] `-sr`开启稀疏化，`--s`指定稀疏因子大小，`--prune`指定稀疏类型。

其中：

`--prune 0`为正常剪枝和规整剪枝的稀疏化

`--prune 1`为极限剪枝的稀疏化

`--prune 2`为Tiny剪枝的稀疏化

```bash
python3 train.py --data data/voc.data --batch-size 16 --accumulate 1 --weights weights/yolov3.weights --cfg cfg/yolov3.cfg -sr --s 0.001 --prune 0 
```


|剪枝方式|<center>优点</center>|<center>缺点</center> |
| --- | --- | --- |
| 正常剪枝 |不对shortcut剪枝，拥有可观且稳定的压缩率，无需微调。  |压缩率达不到极致。  |
| 极限剪枝 |极高的压缩率。  |需要微调。  |
| 规整剪枝 |专为硬件部署设计，剪枝后filter个数均为8的倍数，无需微调。 | 为规整牺牲了部分压缩率。 |
| Tiny剪枝 |稳定的压缩率。  |由于Tiny本来已很小，压缩率中规中矩。  |



### 3.模型剪枝

- [x] 正常剪枝
```bash
python3 normal_prune.py
```
- [x] 规整剪枝
```bash
python3 regular_prune.py
```
- [x] 极限剪枝
```bash
python3 shortcut_prune.py
```
- [x] Tiny剪枝
```bash
python3 prune_tiny_yolo.py
```
这里需要在对应的.py文件内，将opt内的cfg和weights变量指向第2步稀疏化后生成的cfg文件和weights文件。
此外，可通过增大代码中percent的值来获得更大的压缩率。（若稀疏化不到位，且percent值过大，程序会报错。）
## 三、环境搭建


- [x]  `numpy`
- [x] `torch >= 1.1.0`
- [x] `opencv-python`
- [x] `tqdm`


## 四、原作者链接
- [x] https://github.com/Lam1360/YOLOv3-model-pruning
- [x] https://github.com/coldlarry/YOLOv3-complete-pruning










