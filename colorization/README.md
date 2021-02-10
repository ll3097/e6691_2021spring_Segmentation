# colorful image colorization pytorch

* This is a pytorch implementation of paper  [Colorful Image Colorization](https://arxiv.org/pdf/1603.08511.pdf), for [EECS 6691](https://sites.google.com/site/mobiledcc/advanceddeeplearning)  course presentation.
* Notice that in the [official repo](https://github.com/richzhang/colorization), only the demo code was uploaded. Other implementation repositories contain errors in loss function, preprocessing and postprocessing, so I rewrite the code using pytorch.

## Contribution
* To my knowledge, it's the only implementation including both training and inference using pytorch
* Model can be trained on both [ImageNet](http://www.image-net.org/) and other dataset, including [coco](https://cocodataset.org/#home).

## Usage
### Train
Link to your dataset (ImageNet or other) using
```
$ mkdir data
$ cd data
$ ln -s <your_dataset_root> ./
```
Specify your target dataset in **train.py** [line 129 and line 130](https://github.com/ecbme6040/e6691_2021spring_paperreviewsrepo_shared/blob/766c447a6056e675c1454bd76ec7b6846b585b35/colorization/train.py#L129).
You should be very careful about the dataset format. Use [defined module](https://github.com/ecbme6040/e6691_2021spring_paperreviewsrepo_shared/blob/766c447a6056e675c1454bd76ec7b6846b585b35/colorization/train.py#L142) as your `Dataset`, if your dataset is constructed like ⬇️
```
|-- root
    |-- image1.jpg
    |-- image2.jpg
    |-- ...
```
Otherwise specify [ImageFolder](https://github.com/ecbme6040/e6691_2021spring_paperreviewsrepo_shared/blob/766c447a6056e675c1454bd76ec7b6846b585b35/colorization/train.py#L138) if the format is like ⬇️ 
```
|-- root
    |-- folder1
        |-- image1.jpg
        |-- image2.jpg
    |-- folder2
        |-- image1.jpg
        |-- image2.jpg
    |-- ...
```
Then you can set off to training using
```
$ python train.py
```
PS: for other configuration of training, see [argument setup](https://github.com/ecbme6040/e6691_2021spring_paperreviewsrepo_shared/blob/766c447a6056e675c1454bd76ec7b6846b585b35/colorization/train.py#L102) 


### Demo
Open **demo.ipynb**, choose either to inference with pre-saved model or your trained one.
Examples
![image](https://github.com/ecbme6040/e6691_2021spring_paperreviewsrepo_shared/blob/main/colorization/images/4611612935377_.pic_hd.jpg)

### Contributor
**Zhiyuan Ma** zm2354
**Jessie Ye** jy3114

 


